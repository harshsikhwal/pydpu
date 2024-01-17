import grpc
import importlib
from connection import Connection
from inventory import InventoryAPI
from security import SecurityAPI
import storage as StorageAPI
from baseAPI import Base

class Dpu(Base):

    def __init__(self):
        super(Dpu, self).__init__(None)


    def create_grpc_insecure_channel(self, ip: str, port: int):
        """
        Creates a gRPC insecure channel
        :param ip: ip/hostname of the gRPC server
        :param port: port at which the gRPC server is running
        """
        connection = Connection(ip, port, )
        self._insecure_channel = connection._insecure_channel

    @property
    def inventory_api(self) -> InventoryAPI:
        """
        Create the Inventory API instance.
        :return: inventory api
        """
        if self._inventory_api_ is None:
            self._inventory_api_ = InventoryAPI(self)
        return self._inventory_api_

    @property
    def security_api(self) -> SecurityAPI:
        """
        Create the Security API instance.
        :return: security api
        """
        if self._security_api_ is None:
            self._security_api_ = SecurityAPI(self)
        return self._security_api_

    @property
    def storage_api(self) -> StorageAPI:
        """
        Create the Storage API instance.
        :return: storage api
        """
        if self._storage_api is None:
            self._storage_api = StorageAPI(self)
        return self._storage_api
