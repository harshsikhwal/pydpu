import os
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

folder_name = "ipsec"

autogen_message = """# AUTO-GENERATED CODE - DO NOT MODIFY
# Modifications may be overwritten during future updates
# Copyright (c) 2024 Keysight Technologies Inc, or its subsidiaries."""

import_template = """
from typing import List
from enum import Enum
"""

enum_template = """
class {enum_name}(Enum):
{enum_entries}
"""

property_template = """
    @property
    def {property_name}(self) -> {property_type}:
        return self.{field_name}

    @{property_name}.setter
    def {property_name}(self, value: {property_type}):
        self.{field_name} = value
"""

message_class_template = """
class {message_class_name}:
{message_class_description}
    def __init__(self, {constructor_parameters}):
{class_fields}
{class_properties}
"""


"""
Class Map with class name as key and the generated class as entries
"""
generated_class_map = {}
generated_enum_map = {}

"""Dependency Graph for classes"""
from collections import defaultdict

class DependencyGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_dependency(self, source, target):
        self.graph[source].append(target)

    def reverse_topological_sort(self):
        in_degree = defaultdict(int)
        for source, targets in self.graph.items():
            for target in targets:
                in_degree[target] += 1

        queue = [node for node in self.graph if in_degree[node] == 0]
        result = []

        while queue:
            current = queue.pop(0)
            result.append(current)
            for neighbor in self.graph[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return result[::-1]

dependency_graph = DependencyGraph()

def json_reader(json_data):
    """Reads the json_data and creates classes from templates"""
    message_class_name =""
    logger.info("Reading definitions.")
    # get the definition
    definitions = json_data["definitions"]
    
    # iterate over definition
    for definition in definitions:
        generated_class_fields = ""
        constructor_parameters = ""
        message_class_description = ""
        generated_class_properties = ""
        logger.info("Definition name: %s", definition)
        """ 
        Sample: 
        "definitions": {
            "Addrs": {                                          <- definition or class name
                "properties": {                                 <- property or the field name
                    "addr": {
                        "type": "string"                        <- the type of property
                    }
                },
                "additionalProperties": true,
                "type": "object",
                "title": "Addrs",       
                "description": "IP addresses or hostanmes"      <- class description
            }
        }
        """

        # get the class name 
        if '.' in definition:
            message_class_name = definition.split(".")[-1].strip()
        else:
            message_class_name = definition

        dependency_graph.add_dependency(message_class_name, "")

        logger.info("Setting class name as %s", message_class_name)

        if "description" in definitions[definition]:
            # get the class description
            message_class_description = definitions[definition]["description"]
            logger.info("Class Description: %s", message_class_description)

        # get the class properties i.e. fields
            
        logger.info("Reading Properties.")
        if "properties" in definitions[definition]:
            properties = definitions[definition]["properties"] 
            
            for class_field_name in properties:
            
                class_field_info = properties[class_field_name]
                array_primitive_type = ""
                reference_available = False

                logger.info("Reading Class Field: %s", class_field_name)
            
                """
                Check for array here:
                """
                
                if "type" in class_field_info:
                    if class_field_info["type"] == "array":
                        if "items" in class_field_info:
                            if "enum" in class_field_info["items"]:
                                logger.info("class field type is enum array.")
                                array_primitive_type = "Enum"
                                """
                                Case: Enum

                                "definitions": {
                                    "Proposals": {                              <- message_class_name that uses enum
                                        "required": [
                                            "crypto_alg"                      
                                        ],
                                        "properties": {
                                            "crypto_alg": {                     <- class_field as per this source code
                                                "items": {
                                                    "enum": [                   <- enum entries
                                                        "VALUE_0",
                                                        0,
                                                        "VALUE_1",
                                                        1,
                                                        "VALUE_2",
                                                        2,
                                                        "VALUE_3",
                                                        3
                                                    ]
                                                },
                                                "type": "array",                <- class property of type enum
                                                "title": "ZYZ"                  <- enum name
                                            },
                                """
                                
                                enum_name = ""
                                if "title" in class_field_info:
                                    enum_name = class_field_info["title"].replace(" ", "")
                                
                                if "enum_"+enum_name not in generated_enum_map:
                                    
                                    # Get Enum Entries
                                    enum_entries = ""
                                    enum_list = class_field_info["items"]["enum"]
                                    
                                    i = 0
                                    while i < len(enum_list):
                                        enum_entries = enum_entries + "        " +  enum_list[i] + " = " + str(enum_list[i + 1]) + "\n"
                                        i = i + 2
                                    
                                    gen_enum_template = enum_template.format(enum_name=enum_name, enum_entries=enum_entries)  

                                    generated_enum_map["enum_"+enum_name] = gen_enum_template
                                
                            elif "$ref" in class_field_info["items"]:
                                array_primitive_type = class_field_info["items"]["$ref"].split('.')[-1]

                                """
                                special case:
                                add this to dependency graph 
                                TODO: may need a better logic?
                                """
                                dependency_graph.add_dependency(message_class_name, array_primitive_type)
                                logger.info("class field type is %s array.", array_primitive_type)

                            elif "type" in class_field_info["items"]:
                                if class_field_info["items"]["type"] == "string":
                                    array_primitive_type = "str"
                                    logger.info("class field type is str array.")

                                elif class_field_info["items"]["type"] == "integer":
                                    array_primitive_type = "int"
                                    logger.info("class field type is int array.")

                # the class_field_name is none other than the internal field name of the class
                # to preserve we will add _ to the field name as the properties exposed will be of the exact name as that of message struct
                            
                # class_field_information is the init method information 
                
                class_field_information = "_" + class_field_name + " = " + class_field_name
                logger.info("adding init information: %s", class_field_information)
                # keeping constructor parameters as they should be for easy object creation
                constructor_parameters = constructor_parameters + class_field_name + ", "
                logger.info("adding constructor parameters: %s", constructor_parameters)
                # class_property_information logic:
                
                property_type = None
                
                if "type" in class_field_info:
                    # initializing as default value for arrays
                    if class_field_info["type"] == "array":
                        property_type = "List[" + array_primitive_type + "]"
            
                    
                    # setting property type to int
                    elif class_field_info["type"] == "int" or class_field_info["type"] == "int32" or class_field_info["type"] == "int64" or class_field_info["type"] == "uint32" or class_field_info["type"] == "uint64" or class_field_info["type"] == "sint32" or class_field_info["type"] == "sint64" or class_field_info["type"] == "fixed32" or class_field_info["type"] == "fixed64" or class_field_info["type"] == "sfixed32" or class_field_info["type"] == "sfixed64":   
                        logger.info("class field type is int.")
                        property_type = "int"
                    
                    # setting property type to double
                    elif class_field_info["type"] == "float" or class_field_info["type"] == "double":   
                        logger.info("class field type is double.")
                        property_type = "double"

                    # setting property type to bool
                    elif class_field_info["type"] == "bool":
                        logger.info("class field type is bool.")
                        property_type = "bool"

                    # setting property type to str
                    elif class_field_info["type"] == "string":
                        logger.info("class field type is str.")
                        property_type = "str"

                elif "$ref" in class_field_info:
                    property_type = class_field_info["$ref"].split('.')[-1]
                    """
                    special case:
                    add this to dependency graph 
                    TODO: may need a better logic?
                    """
                    dependency_graph.add_dependency(message_class_name, property_type)
                    logger.info("class field type is %s", property_type)
                

                generated_class_properties = generated_class_properties + "        " + property_template.format(property_name=class_field_name, property_type=property_type, field_name="_"+class_field_name) + "\n"
                
                class_field_information = "        " + class_field_information + "\n"
                generated_class_fields = generated_class_fields + class_field_information
                logger.info("class field information: %s", class_field_information)

        else:
            logger.warn("properties missing in %s", definitions[definition])   
            generated_class_fields = "        pass" 
        logger.info("generated class fields: %s", generated_class_fields)

        if message_class_description != "":
            message_class_description = "    " + "\"\"\" " + message_class_description + " \"\"\""

        # remove the last comma
            
        constructor_parameters = constructor_parameters[0:len(constructor_parameters) - 2]

        logger.info("adding constructor parameters: %s", constructor_parameters)
        generated_class_map[message_class_name] = message_class_template.format(message_class_name=message_class_name, message_class_description=message_class_description, constructor_parameters=constructor_parameters, class_fields=generated_class_fields, class_properties=generated_class_properties)

        logger.info("generated class: %s", generated_class_map[message_class_name])
 

logger.info("Reading files in folder: %s", folder_name)

for file in os.listdir(folder_name):
    if ".json" in file:
        logger.info("Reading files: %s", file)
        file_name = file # this will be the class name
        file_path = os.path.join(folder_name, file)
        
        with open(file_path, "r") as json_file:
            # Load the JSON data
            json_data = json.load(json_file)
            # read and add to generated_class_map
            logger.info("Reading json data.")
            json_reader(json_data)  
            

template = autogen_message + "\n" + import_template

for key in generated_enum_map:
    template = template + generated_enum_map[key]

reverse_precedence_order = dependency_graph.reverse_topological_sort()
logger.info("reverse precedence order: %s", reverse_precedence_order)

for precedence in reverse_precedence_order:
    
    if precedence is not "":
        if precedence not in generated_class_map:
            logger.error("%s not found in generated class map!", precedence)
        else:
            template = template + generated_class_map[precedence]
            generated_class_map[precedence] = ""

with open(folder_name + ".py", "w") as text_file:
    text_file.write(template)
