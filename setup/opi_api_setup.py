import os
import glob
import logging
import json
import shutil

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

current_directory = os.getcwd()
print("Current directory:", current_directory)

dest_proto_dir = os.path.join(current_directory,"../pydpu/proto")
print(dest_proto_dir)

proto_storage = []

source_proto_map = {}
source_gen_stub_map = {}

destination_proto_file_map = {}
destination_gen_stub_map = {}

PB2 = "_pb2.py"
GRPC = "_pb2_grpc.py"

autogen_message = """# AUTO-GENERATED CODE - DO NOT MODIFY
# Modifications may be overwritten during future updates
# Copyright (c) 2024 Keysight Technologies Inc, or its subsidiaries."""

rpc_import_template = """
import grpc
from ..base import Base
from ..proto_imports.{parent_api} import *
from google.protobuf import json_format
import json
"""

# Leaf API is proto_filename but in camel case
leaf_api_class_template = """
class {leaf_api}API(Base):
    def __init__(self, parent):
        super({leaf_api}API, self).__init__(parent)
"""

leaf_api_stub_template = """self.{service_name}Stub = {proto_filename}_pb2_grpc.{service_name}Stub(self.channel)"""

leaf_api_property_message_template = """
    @property
    def {proto_filename}_message(self):
        return {proto_filename}_message
"""

leaf_api_def_template = """
    def {rpc_wrapper_name}(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, {proto_filename}_pb2.{rpc_request})
            res_obj = self.{service_name}stub.{rpc_name}(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.{proto_filename}_message.{rpc_response}().deserialize(response)
        except grpc.RpcError as e:
            print(e)
"""

parent_class_template = """
class {parent_class_name}API(Base):
    def __init__(self, parent):
        super({parent_class_name}API, self).__init__(parent)
"""

parent_class_leaf_property_template = """
    @property
    def {proto_filename}(self) -> {proto_filename}API:
        if self._{proto_filename}_api_ is None:
            self._{proto_filename}_ = {proto_filename}API(self)
        return self._{proto_filename}_
"""

parent_class_child_property_template = """
    @property
    def {child_class}(self) -> {child_class}API:
        if self._{child_class}_api_ is None:
            self._{child_class}_ = {child_class}API(self)
        return self._{child_class}_
"""


class ProtoStorage:
    def __init__(self):
        self.proto_filename = ""
        self.pb2_filename = ""
        self.grpc_filename = ""
        self.source_proto_dir_path = ""
        self.source_stub_dir_path = ""
        self.source_relative_path = ""

    def pprint(self):
        print(self.__dict__)
        print(self.proto_hierarchy_list)

    @property
    def proto_source_full_path(self):
        return os.path.join(self.source_proto_dir_path, self.proto_filename)

    @property
    def pb2_source_full_path(self):
        return os.path.join(self.source_stub_dir_path, self.pb2_filename)
    
    @property
    def grpc_source_full_path(self):
        return os.path.join(self.source_stub_dir_path, self.grpc_filename)

    @property
    def pb2_dest_full_path(self):
        return os.path.join(self.dest_dir, self.pb2_filename)
    
    @property
    def grpc_dest_full_path(self):
        return os.path.join(self.dest_dir, self.grpc_filename)

    @property
    def dest_dir(self):
        return os.path.join(dest_proto_dir, self.source_relative_path)

    @property
    def generated_json_proto_dir(self):
        return os.path.join(dest_proto_dir, self.source_relative_path, self.proto_filename.replace(".proto", ""))
    
    @property
    def proto_hierarchy_list(self):
        hierarchy = self.source_relative_path.split("/")
        filtered_hierarchy = [item for item in hierarchy if item != ""]
        return filtered_hierarchy
        
def create_folders(root_path, folders):
    full_path = os.path.join(root_path, folders)
    os.makedirs(full_path, exist_ok=True)


def gather_proto_files(root_dir):

    source_proto_map = {}
    logging.info("Gathering all proto files from: %s", root_dir)

    def gather_skln_stub(root_dir, proto_storage):
        logging.info("Gathering generated skeleton and stub from dir: %s", root_dir)
        found = False
        for dirpath, _, filenames in os.walk(root_dir):
            for filename in filenames:
                if filename == proto_storage.pb2_filename:
                    logging.info("%s found at %s. Adding to storage class", filename, dirpath)
                    proto_storage.source_stub_dir_path = dirpath
                    found = True
                    break
            if found:
                break
        
        if not found:
            logging.warn("Generated files not found!")

    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".proto"):
                logging.info("%s proto file found at %s", filename, dirpath)
                logging.info("Adding to storage class.")
                proto_storage = ProtoStorage()
                proto_storage.proto_filename = filename
                proto_storage.pb2_filename = filename.replace(".proto", "") + PB2
                proto_storage.grpc_filename = filename.replace(".proto", "") + GRPC
                proto_storage.source_proto_dir_path = dirpath

                gather_skln_stub(os.path.abspath(os.path.join(dirpath)), proto_storage)

                source_proto_map[os.path.abspath(os.path.join(dirpath, filename))] = proto_storage

    return source_proto_map

def get_common_prefix(paths):
    prefix = os.path.commonprefix(paths)
    idx = prefix.rfind(os.path.sep)
    return prefix[:idx + 1] if idx != -1 else ''

def get_relative_path(file_path, root_dir):
    parent_dir = os.path.dirname(file_path)
    relative_path = os.path.relpath(parent_dir, root_dir)
    relative_path += '/' if relative_path != '.' else ''
    return relative_path


import subprocess

def execute_command(command):
    try:
        # Execute the command
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        # Handle any errors
        logging.info("Error executing command: %s", e)

def create_directories(proto_obj):
    logging.info("Creating directory: %s", proto_obj.dest_dir)
    execute_command("mkdir -p " + proto_obj.dest_dir)
    
    # for generated_json
    logging.info("Creating directory: %s", proto_obj.generated_json_proto_dir)
    execute_command("mkdir -p " + proto_obj.generated_json_proto_dir)

def copy_generated_stubs(source_proto_map):

    logging.info("copying stubs from source to destination")
    for proto_obj in source_proto_map.values():
        # print(proto_obj.pprint())    

        create_directories(proto_obj)
        # copy pb2 to destination
        logging.info("copying %s to %s", proto_obj.pb2_source_full_path, proto_obj.pb2_dest_full_path)
        shutil.copy2(proto_obj.pb2_source_full_path, proto_obj.pb2_dest_full_path)
        logging.info("File %s copied successfully.", proto_obj.pb2_source_full_path)

        # copy grpc to destination
        logging.info("copying %s to %s", proto_obj.grpc_source_full_path, proto_obj.grpc_dest_full_path)
        shutil.copy2(proto_obj.grpc_source_full_path, proto_obj.grpc_dest_full_path)
        logging.info("File %s copied successfully.", proto_obj.grpc_source_full_path)


def generate_rpc_class_from_proto(parent_class_storage_map, proto_storage_obj):
    """
    Return the rpc generated classes
    """
    leaf_classes = ""
    # print("\"\"\"" + proto_storage_obj.proto_source_full_path + "\"\"\"" )
    # Open the file for reading
    with open(proto_storage_obj.proto_source_full_path, "r") as file:
        # Read the entire content of the file
        file_content = file.read()
        
        # Split the content into tokens
        tokens = file_content.split()
        
        leaf_class_functions = ""
        leaf_stubs = ""
        service_name = ""

        for index in range(len(tokens)):
            
            if tokens[index] == "service" and tokens[index + 2] == "{":

                # this will be the stub name
                service_name = tokens[index + 1]
                
                stack = []
                
                if tokens[index + 2] == "{":
                    stack.append("{")

                # iterate till we get '}'
                index = index + 3
                while index < len(tokens):

                    # initialize to empty
                    rpc_wrapper_name = ""
                    rpc_request = ""
                    rpc_name = ""
                    rpc_response = ""                    
                    if len(stack) == 0:
                        break
                    
                    if "{" in tokens[index] or "}" in tokens[index]:
                        # iterate the token
                        for token in tokens[index]:
                            if token == "{":
                                stack.append("{")
                            elif token == "}":
                                stack.pop()

                    elif tokens[index] == "wrapper_name":
                        rpc_wrapper_name = tokens[index + 1]

                    elif tokens[index] == "rpc":
                        rpc_name = tokens[index + 1]
                        if "(" in rpc_name and ")" in rpc_name:
                            mix_string = rpc_name.split("(")
                            rpc_name = mix_string[0]
                            rpc_request = mix_string[1].replace(")", "")
                        if rpc_request == "":
                            rpc_request = tokens[index + 2].replace("(", "").replace(")", "")
                            if tokens[index + 3] == "returns":
                                rpc_response = tokens[index + 4].replace("(", "").replace(")", "")
                                if "{" in rpc_response:
                                    stack.append("{")
                                    rpc_response = rpc_response.replace("{", "")
                                index = index + 1
                            index = index + 2
                        else:
                            if tokens[index + 2] == "returns":
                                rpc_response = tokens[index + 3].replace("(", "").replace(")", "")
                                if "{" in rpc_response:
                                    stack.append("{")
                                    rpc_response = rpc_response.replace("{", "")

                        # print("\"\"\""  + rpc_name, " " , rpc_request, " ", rpc_response + "\"\"\"" )
                        # validation:
                        if rpc_wrapper_name == "":
                            rpc_wrapper_name = rpc_name

                        leaf_class_functions = leaf_class_functions + leaf_api_def_template.format(rpc_wrapper_name=rpc_wrapper_name, proto_filename=proto_storage_obj.proto_filename.replace(".proto", ""), rpc_request=rpc_request, service_name=service_name, rpc_name=rpc_name, rpc_response=rpc_response) 
                
                    index = index + 1
            
                # generate the template
                leaf_stubs = leaf_stubs + "        " + leaf_api_stub_template.format(service_name=service_name, proto_filename=proto_storage_obj.proto_filename.replace(".proto", "")) + "\n"

        # so leaf api is nothing but proto_file_name in camel case
        # TODO: better logic for camel case
        leaf_classes = leaf_api_class_template.format(leaf_api=to_camel_case(proto_storage_obj.proto_filename.replace(".proto", "")))

        leaf_classes = leaf_classes + leaf_stubs + leaf_class_functions
        # print(leaf_classes)
    
    if proto_storage_obj.source_relative_path not in parent_class_storage_map:
        parent_class_storage_map[proto_storage_obj.source_relative_path] = [leaf_classes]
    else:
        parent_class_storage_map[proto_storage_obj.source_relative_path].append(leaf_classes)


class RpcClassHierarchy:
    def __init__(self, class_name):
        self.class_name = class_name
        self.child_classes = {}
        self.leaf_classes = []

    @property
    def classname(self):       
        return to_camel_case(self.class_name)

def to_camel_case(name):
    # return self.class_name but with _
    words = name.replace('-', '_').split('_')
    camel_case = [word.capitalize() for word in words]
    return ''.join(camel_case)


def generate_hierarchy(parent_class_storage_map):
    root = RpcClassHierarchy('root')
    for key, classes in parent_class_storage_map.items():
        current = root
        directories = key.split('/')
        for directory in directories:
            if directory != "":
                if directory not in current.child_classes:
                    current.child_classes[directory] = RpcClassHierarchy(directory)
                current = current.child_classes[directory]
        current.leaf_classes = classes
    return root

# working with a directed tree
def generate_rpc_classes(root_node):
    stack = [root_node]
    generated_classes = ""
    while stack:
        node = stack.pop()
        # generate the parent class:

        print("Generating the Parent Class: ", node.classname)

        parent_class = parent_class_template.format(parent_class_name = node.classname)
        child_property = ""
        print("Child Classes: ")
        
        for child in node.child_classes.keys():
            # generate the child classes here:
            print("Child: ", child)
            child_property = child_property + parent_class_child_property_template.format(child_class=to_camel_case(child)) + "\n"
            stack.append(node.child_classes[child])
        

        parent_class = parent_class + child_property

        if parent_class not in node.leaf_classes:
            generated_classes = ''.join(node.leaf_classes) + parent_class + generated_classes
        else:
            generated_classes = parent_class + generated_classes

    return generated_classes


def generate_proto_imports():

    proto_import_folder = "../pydpu/proto_imports"

    proto_folder = "../pydpu/proto"
    execute_command("mkdir -p " + proto_folder)

    logging.info("generating imports in %s", proto_import_folder)

    level_one_apis = [entry for entry in os.listdir(proto_folder) if os.path.isdir(os.path.join(proto_folder, entry))]

    # generate the python file with these names
    
    proto_import_template = """from ..proto.{root_api} import {python_file_name}\n"""
    for api in level_one_apis:
        # scan recursively        
        generated_proto_files = []
        for dirpath, _, filenames in os.walk(os.path.join(proto_folder, api)):
                for filename in filenames:
                    if filename.endswith(".py") and filename != "__init__.py":
                        generated_proto_files.append(filename.replace(".py", ""))
        # dump to file 
        generated_proto_template = """# SPDX-License-Identifier: Apache-2.0\n# Copyright (c) 2024 Keysight Technologies Inc, or its subsidiaries.\n"""
        for proto_file in generated_proto_files:
            generated_proto_template = generated_proto_template + proto_import_template.format(root_api=api, python_file_name=proto_file)
        
        with open(os.path.join(proto_import_folder, api + ".py"), 'w') as python_file:
            python_file.write(generated_proto_template)

if __name__ == "__main__":

    with open("config.json", "r") as config_file:
        config_data = json.load(config_file)

    logging.info("config data: %s", config_data)

    # TODO: Add config validation 

    # get all the proto files from opi_api_dir
    source_proto_map = gather_proto_files(config_data["opi_api_dir"])

    source_proto_file_list = list(source_proto_map.keys())

    absolute_root_dir = get_common_prefix(source_proto_file_list)

    logging.info("Absolute root dir: %s", absolute_root_dir)

    for source_full_path in source_proto_map:
        relative_path = get_relative_path(source_full_path, absolute_root_dir)
        source_proto_map[source_full_path].source_relative_path = relative_path
        logging.info("relative path for %s : %s", source_full_path, relative_path)

    # copy the stubs
    copy_generated_stubs(source_proto_map)

    # generate the proto_imports

    generate_proto_imports()

    # TODO: implement below code
    # # generate the protoc jsons:

    # for proto_obj in source_proto_map.values():
    #     logging.info("Generating JSON messages for : %s", proto_obj.proto_filename)
    #     command = "protoc --jsonschema_out=" + proto_obj.generated_json_proto_dir + " --jsonschema_opt=all_fields_required --proto_path=" + proto_obj.source_proto_dir_path + " " + proto_obj.proto_source_full_path

    #     logging.info("Executing command : %s", command)
    #     execute_command(command)

    parent_class_storage_map = {}
    for values in source_proto_map.values():
        generate_rpc_class_from_proto(parent_class_storage_map, values)

    # print(parent_class_storage_map)
    # parent_classes = ""
    # # generate the parent class

    # hierarchy_list = proto_storage_obj.proto_hierarchy_list
    # print(proto_storage_obj.proto_hierarchy_list)
    # child_template = ""
    # for index in range(len(hierarchy_list)-1, -1, -1):
    #     if index == len(hierarchy_list) - 1:
    #         child_template = parent_class_leaf_property_template.format(proto_filename = proto_storage_obj.proto_filename.replace(".proto", ""), leaf_api=proto_storage_obj.proto_filename.replace(".proto", ""))
    #     else:
    #         child_template = parent_class_child_property_template.format(child_class=hierarchy_list[index + 1].replace("-","_"))
    #     # TODO: better function to replace any different characters for class name
    #     parent_classes = parent_classes + parent_class_template.format(parent_class_name=hierarchy_list[index].replace("-","_")) + child_template

    # parent_classes =leaf_classes +  parent_classes 

    # print(proto_storage_obj.proto_hierarchy_list)
    # print(parent_classes)
    # return parent_classes

    root_node = generate_hierarchy(parent_class_storage_map)

    # print_classes(root_node)

    for classes in root_node.child_classes.keys():
        print(classes)
        print("values = ", root_node.child_classes[classes] )

        generated_class = generate_rpc_classes(root_node.child_classes[classes])
        
        generated_class = autogen_message + rpc_import_template.format(parent_api=classes) + generated_class
        # dump to folder

        gen_rpc_dump_folder = "../pydpu/rpc_apis"

        logging.info("generating imports in %s", gen_rpc_dump_folder)

        # generate the python file with these names
        
            
        with open(os.path.join(gen_rpc_dump_folder, classes + ".py"), 'w') as python_file:
            python_file.write(generated_class)

