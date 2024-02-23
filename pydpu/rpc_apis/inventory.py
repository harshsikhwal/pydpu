# AUTO-GENERATED CODE - DO NOT MODIFY
# Modifications may be overwritten during future updates
# Copyright (c) 2024 Keysight Technologies Inc, or its subsidiaries.
import grpc
from ..base import Base
from ..proto_imports.inventory import *
from google.protobuf import json_format
import json

class InventoryAPI(Base):
    def __init__(self, parent):
        super(InventoryAPI, self).__init__(parent)
        self.InventoryServiceStub = inventory_pb2_grpc.InventoryServiceStub(self.channel)

    @property
    def inventory_messages(self):
        return inventory_messages

    @property
    def inventory_pb2(self):
        return inventory_pb2

    def get_inventory(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.inventory_pb2.GetInventoryRequest())
            res_obj = self.InventoryServiceStub.GetInventory(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.inventory_message.Inventory().deserialize(response)
        except grpc.RpcError as e:
            print(e)
