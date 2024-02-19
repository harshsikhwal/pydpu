# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2022 Dell Inc, or its subsidiaries.
# Copyright (c) 2024 Keysight Technologies Inc, or its subsidiaries.

import grpc
from ..base import Base

from ..proto_imports.network import *

class BgpAPI(Base):
    """
    Unimplemented
    """

    def __init__(self, parent):
        super(BgpAPI, self).__init__(parent)
        # Unimplemented
        pass

    @property
    def bgp_message(self):
        """The bgp protobuf stub
        Returns
        -------
        - bgp_pb2 object: The generated bgp pb2 file
        """
        return bgp_pb2


class CloudRpcAPI(Base):

    def __init__(self, parent):
        super(CloudRpcAPI, self).__init__(parent)
        self.stub = cloudrpc_pb2_grpc.CloudInfraServiceStub(self.channel)
        pass

    @property
    def cloud_rpc_message(self):
        """The cloud rpc protobuf stub
        Returns
        -------
        - cloudrpc_pb2 object: The generated cloud rpc pb2 file
        """
        return cloudrpc_pb2


class DeviceAPI(Base):
    """
    Unimplemented
    """

    def __init__(self, parent):
        super(DeviceAPI, self).__init__(parent)
        # unimplemented
        pass

    @property
    def device_message(self):
        """The device protobuf stub
        Returns
        -------
        - device_pb2 object: The generated device pb2 file
        """
        return device_pb2


class CloudAPI(Base):

    def __init__(self, parent):
        super(CloudAPI, self).__init__(parent)


class L2XpuInfraAPI(Base):
    def __init__(self, parent):
        super(L2XpuInfraAPI, self).__init__(parent)
        self.stub = l2_xpu_infra_mgr_pb2_grpc.LogicalBridgeServiceStub(self.channel)

    @property
    def l2xpu_infra_message(self):
        """The l2 xpu infra protobuf stub
        Returns
        -------
        - l2_xpu_infra_mgr_pb2 object: The generated l2_xpu_infra_mgr_pb2 pb2 file
        """
        return l2_xpu_infra_mgr_pb2

    def create_bridge(self, request):
        try:
            return self.stub.CreateLogicalBridge(request=request)
        except grpc.RpcError as e:
            print(e)

    def create_port(self, request):
        try:
            return self.stub.CreateBridgePort(request=request)
        except grpc.RpcError as e:
            print(e)


class L3XpuInfraAPI(Base):
    def __init__(self, parent):
        super(L3XpuInfraAPI, self).__init__(parent)
        self.stub = l3_xpu_infra_mgr_pb2_grpc.VrfServiceStub(self.channel)

    @property
    def l3xpu_infra_message(self):
        """The l3 xpu infra protobuf stub
        Returns
        -------
        - l3_xpu_infra_mgr_pb2 object: The generated l3_xpu_infra_mgr_pb2 pb2 file
        """
        return l3_xpu_infra_mgr_pb2

    def create_vrf(self, request):
        try:
            return self.stub.CreateVrf(request=request)
        except grpc.RpcError as e:
            print(e)

    def create_svi(self, request):
        try:
            return self.stub.CreateSvi(request=request)
        except grpc.RpcError as e:
            print(e)

class EvpnGWAPI(Base):

    def __init__(self, parent):
        super(EvpnGWAPI, self).__init__(parent)

    @property
    def l2_xpu_infra(self) -> L2XpuInfraAPI:
        """The l2 xpu infra protobuf stub
        Returns
        -------
        - l2_xpu_infra_mgr_pb2 object: The generated l2_xpu_infra_mgr_pb2 pb2 file
        """
        if self._l2_xpu_infra_api_ is None:
            self._l2_xpu_infra_api_ = L2XpuInfraAPI(self)
        return self._l2_xpu_infra_api_

    @property
    def l3_xpu_infra(self) -> L3XpuInfraAPI:
        """The l2 xpu infra protobuf stub
        Returns
        -------
        - l2_xpu_infra_mgr_pb2 object: The generated l2_xpu_infra_mgr_pb2 pb2 file
        """
        if self._l3_xpu_infra_api_ is None:
            self._l3_xpu_infra_api_ = L3XpuInfraAPI(self)
        return self._l3_xpu_infra_api_

class K8sAPI(Base):
    """
    Unimplemented
    """

    def __init__(self, parent):
        super(K8sAPI, self).__init__(parent)
        # Unimplemented


class OPINetCommonAPI(Base):

    def __init__(self, parent):
        super(OPINetCommonAPI, self).__init__(parent)


class TelcoAPI(Base):

    def __init__(self, parent):
        super(TelcoAPI, self).__init__(parent)


class NetworkAPI(Base):
    def __init__(self, parent):
        super(NetworkAPI, self).__init__(parent)

    @property
    def cloud(self) -> CloudAPI:
        """
        Creates the cloud API instance
        :return: cloud instance
        """
        if self._cloud_api_ is None:
            self._cloud_api_ = CloudAPI(self)
        return self._cloud_api_

    @property
    def evpn_gw(self) -> EvpnGWAPI:
        """
        Creates the evpn-gw API instance
        :return: evpn-gw instance
        """
        if self._evpn_gw_api_ is None:
            self._evpn_gw_api_ = EvpnGWAPI(self)
        return self._evpn_gw_api_

    @property
    def k8s(self) -> K8sAPI:
        """
        Creates the k8s API instance
        :return: k8s instance
        """
        if self._k8s_api_ is None:
            self._k8s_api_ = K8sAPI(self)
        return self._k8s_api_

    @property
    def opi_net_common(self) -> OPINetCommonAPI:
        """
        Creates the OPI Net Common API instance
        :return: opi_net_common instance
        """
        if self._opi_net_common_api_ is None:
            self._opi_net_common_api_ = OPINetCommonAPI(self)
        return self._opi_net_common_api_

    @property
    def telco(self) -> TelcoAPI:
        """
        Creates the telco API instance
        :return: telco instance
        """
        if self._telco_api_ is None:
            self._telco_api_ = TelcoAPI(self)
        return self._telco_api_
