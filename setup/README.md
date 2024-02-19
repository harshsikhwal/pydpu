# pydpu setup workflow

## Motivation

The opi-api repository contains the generated skeleton and stub. These are generated as per version. The idea is to segregate and create branches which will represent the version. Therefore:

[Insert branch mapping image here]

Since we have a separation of concerns, the auto generator can clone and checkout on specific branch and then build the sdk on that version. This would lead to better versioning control and provide stable APIs

## Design

[Insert Image ]

The pydpu is semi-automated:
* The RPC messages are generated, as python based IDEs are unable to provide code suggestions for generated pb2.py files
* 

## Steps executed
1. Clone the opi-api repository
2. Add the opi-api repository path
3. Run opi_api_setup.py

## opi_api_setup.py

* This code base reads the config.json and gets the repository path
* It scans the opi-api repository and does the following:
    * Search for files with .proto extension
    * Search for _pb2_grpc.py and _pb2.py files with the same name as that of proto file
    * Manage a map with the full source path as the key and values as an object of class having following entires:
        * proto_filename
        * pb2_filename
        * grpc_filename
        * source_proto_dir_path
        * source_stub_dir_path
        * source_relative_path
* The code then starts copying the generated proto stubs to the destination directory: ../pydpu/proto 
* It creates folders if the entries are not present and dumps the protos as a part of the high level APIs
* It also creates folders for JSON dumps: required to generate an intermediate message wrapper
* The code generates proto imports which are imported in a single file, for better abstraction and quicker implementation


## TODO

* Generate the JSON schema for message type and run the class_generator.py
    * Import the same in the first level API code
* Auto-generate the whole RPC code 

### Workflow

* Maintain a dictionary: csv, or some kind of mapper which provide a better name for the RPC call


