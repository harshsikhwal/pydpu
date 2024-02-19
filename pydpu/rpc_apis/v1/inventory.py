# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2022 Dell Inc, or its subsidiaries.
# Copyright (c) 2024 Keysight Technologies Inc, or its subsidiaries.

import grpc
from ..baseAPI import Base

from ..proto.v1 import inventory_pb2
from ..proto.v1 import inventory_pb2_grpc


class InventoryAPI(Base):
    def __init__(self, parent):
        super(InventoryAPI, self).__init__(parent)
        self.stub = inventory_pb2_grpc.InventorySvcStub(self.grpc_insecure_channel)

    @property
    def inventory_message(self):
        """The inventory_message object of the current object
        Returns
        -------
        - inventory_pb2
        """
        return inventory_pb2

    def get_inventory(self, inventory_request):
        try:
            res = self.stub.GetInventory(request=inventory_request)
            return res

        except grpc.RpcError as e:
            print(e)


def get_inventory(address):
    try:
        with grpc.insecure_channel(address) as channel:
            stub = inventory_pb2_grpc.InventorySvcStub(channel)
            res = stub.GetInventory(request=inventory_pb2.GetInventoryRequest())
            return res
    except grpc.RpcError as e:
        print(e)