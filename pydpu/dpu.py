# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2022 Dell Inc, or its subsidiaries.
# Copyright (c) 2024 Keysight Technologies Inc, or its subsidiaries.

import grpc
import importlib
from connection import Connection
from rpc_apis.common import CommonAPI
from rpc_apis.inventory import InventoryAPI
from rpc_apis.network import NetworkAPI
from rpc_apis.security import SecurityAPI
from rpc_apis.storage import StorageAPI
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
    def common(self) -> CommonAPI:
        """
        Create the Common API instance
        :return: common api
        """
        if self._common_api_ is None:
            self._common_api_ = CommonAPI(self)
        return self._common_api_

    @property
    def inventory(self) -> InventoryAPI:
        """
        Create the Inventory API instance
        :return: inventory api
        """
        if self._inventory_api_ is None:
            self._inventory_api_ = InventoryAPI(self)
        return self._inventory_api_

    @property
    def network(self) -> NetworkAPI:
        """
        Create the Security API instance
        :return: security api
        """
        if self._network_api_ is None:
            self._network_api_ = NetworkAPI(self)
        return self._network_api_

    @property
    def security(self) -> SecurityAPI:
        """
        Create the Security API instance
        :return: security api
        """
        if self._security_api_ is None:
            self._security_api_ = SecurityAPI(self)
        return self._security_api_

    @property
    def storage(self) -> StorageAPI:
        """
        Create the Storage API instance
        :return: storage api
        """
        if self._storage_api_ is None:
            self._storage_api_ = StorageAPI(self)
        return self._storage_api_
