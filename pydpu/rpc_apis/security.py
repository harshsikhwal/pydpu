# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2022 Dell Inc, or its subsidiaries.
# Copyright (c) 2024 Keysight Technologies Inc, or its subsidiaries.

import grpc
from ..baseAPI import Base

from ..proto_imports.security import *

class IPSecAPI(Base):
    def __init__(self, parent):
        super(IPSecAPI, self).__init__(parent)
        self.stub = ipsec_pb2_grpc.IPsecStub(self.grpc_insecure_channel)

    @property
    def ipsec_message(self):
        """The ipsec protobuf stub
        Returns
        -------
        - ipsec_pb2 object: The generated ipsec pb2 file
        """
        return ipsec_pb2

    def get_ipsec_version(self, request):
        try:
            return self.stub.IPsecVersion(request=request)
        except grpc.RpcError as e:
            print(e)

    def get_ipsec_stats(self, request):
        try:
            return self.stub.IPsecStats(request=request)
        except grpc.RpcError as e:
            print(e)

    def list_ipsec_conns(self, request):
        try:
            return self.stub.IPsecListConns(request=request)
        except grpc.RpcError as e:
            print(e)

    def list_ipsec_sas(self, request):
        try:
            return self.stub.IPsecListSas(request=request)
        except grpc.RpcError as e:
            print(e)

    def list_ipsec_certs(self, request):
        try:
            return self.stub.IPsecListCerts(request=request)
        except grpc.RpcError as e:
            print(e)

    def load_ipsec_connection(self, request):
        try:
            return self.stub.IPsecLoadConn(request=request)
        except grpc.RpcError as e:
            print(e)


class SecurityAPI(Base):

    def __init__(self, parent):
        super(SecurityAPI, self).__init__(parent)

    @property
    def ipsec(self) -> IPSecAPI:
        """
        Create the Inventory API instance.
        :return: inventory api
        """
        if self._ipsec_api_ is None:
            self._ipsec_api_ = IPSecAPI(self)
        return self._ipsec_api_
