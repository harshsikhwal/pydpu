# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2022 Dell Inc, or its subsidiaries.
# Copyright (c) 2024 Keysight Technologies Inc, or its subsidiaries.

from connection import Connection
from rpc_apis.v1.common import CommonAPI
from rpc_apis.v1.inventory import InventoryAPI
from rpc_apis.v1.network import NetworkAPI
from rpc_apis.v1.security import SecurityAPI
from rpc_apis.v1.storage import StorageAPI
from baseAPI import Base


class Dpu(Base):

    def __init__(self):
        super(Dpu, self).__init__(None)


    def connect_grpc_insecure_channel(self, ip: str, port: int):
        """
        Creates a gRPC insecure channel
        :param ip: ip/hostname of the gRPC server
        :param port: port at which the gRPC server is running
        """
        connection = Connection(ip, port)
        self._insecure_channel = connection.insecure_channel()

    @property
    def common(self):
        """
        Create the Common API instance
        :return: common obj
        """
        if self._common_api_ is None:
            self._common_api_ = CommonAPI(self)
        return self._common_api_

    @property
    def inventory(self):
        """
        Create the Inventory API instance
        :return: inventory obj
        """
        if self._inventory_api_ is None:
            self._inventory_api_ = InventoryAPI(self)
        return self._inventory_api_

    @property
    def network(self):
        """
        Create the Network API instance
        :return: network obj
        """
        if self._network_api_ is None:
            self._network_api_ = NetworkAPI(self)
        return self._network_api_

    @property
    def security(self):
        """
        Create the Security API instance
        :return: security obj
        """
        if self._security_api_ is None:
            self._security_api_ = SecurityAPI(self)
        return self._security_api_

    @property
    def storage(self):
        """
        Create the Storage API instance
        :return: storage obj
        """
        if self._storage_api_ is None:
            self._storage_api_ = StorageAPI(self)
        return self._storage_api_
