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

class ProtoStorage:
    def __init__(self):
        proto_filename = ""
        pb2_filename = ""
        grpc_filename = ""
        source_proto_dir_path = ""
        source_stub_dir_path = ""
        source_relative_path = ""

    def pprint(self):
        print(self.__dict__)

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

def create_folders(root_path, folders):
    full_path = os.path.join(root_path, folders)
    os.makedirs(full_path, exist_ok=True)


def gather_proto_files(root_dir):

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

def copy_generated_stubs():

    logging.info("copying stubs from source to destination")
    for proto_obj in source_proto_map.values():
        print(proto_obj.pprint())    

        create_directories(proto_obj)
        # copy pb2 to destination
        logging.info("copying %s to %s", proto_obj.pb2_source_full_path, proto_obj.pb2_dest_full_path)
        shutil.copy2(proto_obj.pb2_source_full_path, proto_obj.pb2_dest_full_path)
        logging.info("File %s copied successfully.", proto_obj.pb2_source_full_path)

        # copy grpc to destination
        logging.info("copying %s to %s", proto_obj.grpc_source_full_path, proto_obj.grpc_dest_full_path)
        shutil.copy2(proto_obj.grpc_source_full_path, proto_obj.grpc_dest_full_path)
        logging.info("File %s copied successfully.", proto_obj.grpc_source_full_path)


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
    gather_proto_files(config_data["opi_api_dir"])

    source_proto_file_list = list(source_proto_map.keys())

    absolute_root_dir = get_common_prefix(source_proto_file_list)

    logging.info("Absolute root dir: %s", absolute_root_dir)

    for source_full_path in source_proto_map:
        relative_path = get_relative_path(source_full_path, absolute_root_dir)
        source_proto_map[source_full_path].source_relative_path = relative_path
        logging.info("relative path for %s : %s", source_full_path, relative_path)

    # copy the stubs
    copy_generated_stubs()

    # generate the proto_imports

    generate_proto_imports()

    # TODO: implement below code
    # # generate the protoc jsons:

    # for proto_obj in source_proto_map.values():
    #     logging.info("Generating JSON messages for : %s", proto_obj.proto_filename)
    #     command = "protoc --jsonschema_out=" + proto_obj.generated_json_proto_dir + " --jsonschema_opt=all_fields_required --proto_path=" + proto_obj.source_proto_dir_path + " " + proto_obj.proto_source_full_path

    #     logging.info("Executing command : %s", command)
    #     execute_command(command)


