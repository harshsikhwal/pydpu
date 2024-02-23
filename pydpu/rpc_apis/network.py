# AUTO-GENERATED CODE - DO NOT MODIFY
# Modifications may be overwritten during future updates
# Copyright (c) 2024 Keysight Technologies Inc, or its subsidiaries.
import grpc
from ..base import Base
from ..proto_imports.network import *
from google.protobuf import json_format
import json

class OpenconfigInterfacesAPI(Base):
    def __init__(self, parent):
        super(OpenconfigInterfacesAPI, self).__init__(parent)
        self.NetInterfaceServiceStub = openconfig_interfaces_pb2_grpc.NetInterfaceServiceStub(self.channel)

    @property
    def openconfig_interfaces_messages(self):
        return openconfig_interfaces_messages

    @property
    def openconfig_interfaces_pb2(self):
        return openconfig_interfaces_pb2

    def get_net_interface(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.openconfig_interfaces_pb2.GetNetInterfaceRequest())
            res_obj = self.NetInterfaceServiceStub.GetNetInterface(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.openconfig_interfaces_message.NetInterface().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def list_net_interface(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.openconfig_interfaces_pb2.ListNetInterfacesRequest())
            res_obj = self.NetInterfaceServiceStub.ListNetInterfaces(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.openconfig_interfaces_message.ListNetInterfacesResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def update_net_interface(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.openconfig_interfaces_pb2.UpdateNetInterfaceRequest())
            res_obj = self.NetInterfaceServiceStub.UpdateNetInterface(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.openconfig_interfaces_message.NetInterface().deserialize(response)
        except grpc.RpcError as e:
            print(e)

class NetworktypesAPI(Base):
    def __init__(self, parent):
        super(NetworktypesAPI, self).__init__(parent)

    @property
    def networktypes_messages(self):
        return networktypes_messages

    @property
    def networktypes_pb2(self):
        return networktypes_pb2

class OpinetcommonAPI(Base):
    def __init__(self, parent):
        super(OpinetcommonAPI, self).__init__(parent)

    @property
    def OpenconfigInterfaces(self) -> OpenconfigInterfacesAPI:
        if self._OpenconfigInterfaces_api_ is None:
            self._OpenconfigInterfaces_ = OpenconfigInterfacesAPI(self)
        return self._OpenconfigInterfaces_

    @property
    def Networktypes(self) -> NetworktypesAPI:
        if self._Networktypes_api_ is None:
            self._Networktypes_ = NetworktypesAPI(self)
        return self._Networktypes_

class RouteAPI(Base):
    def __init__(self, parent):
        super(RouteAPI, self).__init__(parent)

    @property
    def route_messages(self):
        return route_messages

    @property
    def route_pb2(self):
        return route_pb2

class UnderlayrouteAPI(Base):
    def __init__(self, parent):
        super(UnderlayrouteAPI, self).__init__(parent)

    @property
    def underlayroute_messages(self):
        return underlayroute_messages

    @property
    def underlayroute_pb2(self):
        return underlayroute_pb2

class MappingAPI(Base):
    def __init__(self, parent):
        super(MappingAPI, self).__init__(parent)

    @property
    def mapping_messages(self):
        return mapping_messages

    @property
    def mapping_pb2(self):
        return mapping_pb2

class VnicAPI(Base):
    def __init__(self, parent):
        super(VnicAPI, self).__init__(parent)

    @property
    def vnic_messages(self):
        return vnic_messages

    @property
    def vnic_pb2(self):
        return vnic_pb2

class TunnelAPI(Base):
    def __init__(self, parent):
        super(TunnelAPI, self).__init__(parent)

    @property
    def tunnel_messages(self):
        return tunnel_messages

    @property
    def tunnel_pb2(self):
        return tunnel_pb2

class BgpAPI(Base):
    def __init__(self, parent):
        super(BgpAPI, self).__init__(parent)

    @property
    def bgp_messages(self):
        return bgp_messages

    @property
    def bgp_pb2(self):
        return bgp_pb2

class VpcAPI(Base):
    def __init__(self, parent):
        super(VpcAPI, self).__init__(parent)

    @property
    def vpc_messages(self):
        return vpc_messages

    @property
    def vpc_pb2(self):
        return vpc_pb2

class DeviceAPI(Base):
    def __init__(self, parent):
        super(DeviceAPI, self).__init__(parent)

    @property
    def device_messages(self):
        return device_messages

    @property
    def device_pb2(self):
        return device_pb2

class CloudrpcAPI(Base):
    def __init__(self, parent):
        super(CloudrpcAPI, self).__init__(parent)
        self.CloudInfraServiceStub = cloudrpc_pb2_grpc.CloudInfraServiceStub(self.channel)

    @property
    def cloudrpc_messages(self):
        return cloudrpc_messages

    @property
    def cloudrpc_pb2(self):
        return cloudrpc_pb2

    def GetDeviceCapabilities(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.GetDeviceCapabilitiesRequest())
            res_obj = self.CloudInfraServiceStub.GetDeviceCapabilities(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.DeviceCapabilities().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateDevice(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.CreateDeviceRequest())
            res_obj = self.CloudInfraServiceStub.CreateDevice(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Device().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteDevice(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.DeleteDeviceRequest())
            res_obj = self.CloudInfraServiceStub.DeleteDevice(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateDevice(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.UpdateDeviceRequest())
            res_obj = self.CloudInfraServiceStub.UpdateDevice(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Device().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListDevices(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.ListDevicesRequest())
            res_obj = self.CloudInfraServiceStub.ListDevices(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.ListDevicesResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetDevice(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.GetDeviceRequest())
            res_obj = self.CloudInfraServiceStub.GetDevice(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Device().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdatePort(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.UpdatePortRequest())
            res_obj = self.CloudInfraServiceStub.UpdatePort(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Port().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListPorts(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.ListPortsRequest())
            res_obj = self.CloudInfraServiceStub.ListPorts(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.ListPortsResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetPort(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.GetPortRequest())
            res_obj = self.CloudInfraServiceStub.GetPort(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Port().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateVnic(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.CreateVnicRequest())
            res_obj = self.CloudInfraServiceStub.CreateVnic(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Vnic().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteVnic(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.DeleteVnicRequest())
            res_obj = self.CloudInfraServiceStub.DeleteVnic(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateVnic(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.UpdateVnicRequest())
            res_obj = self.CloudInfraServiceStub.UpdateVnic(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Vnic().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListVnics(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.ListVnicsRequest())
            res_obj = self.CloudInfraServiceStub.ListVnics(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.ListVnicsResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetVnic(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.GetVnicRequest())
            res_obj = self.CloudInfraServiceStub.GetVnic(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Vnic().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateInterface(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.CreateInterfaceRequest())
            res_obj = self.CloudInfraServiceStub.CreateInterface(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Interface().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteInterface(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.DeleteInterfaceRequest())
            res_obj = self.CloudInfraServiceStub.DeleteInterface(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateInterface(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.UpdateInterfaceRequest())
            res_obj = self.CloudInfraServiceStub.UpdateInterface(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Interface().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListInterfaces(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.ListInterfacesRequest())
            res_obj = self.CloudInfraServiceStub.ListInterfaces(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.ListInterfacesResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetInterface(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.GetInterfaceRequest())
            res_obj = self.CloudInfraServiceStub.GetInterface(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Interface().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateRouteTable(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.CreateRouteTableRequest())
            res_obj = self.CloudInfraServiceStub.CreateRouteTable(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.RouteTable().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteRouteTable(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.DeleteRouteTableRequest())
            res_obj = self.CloudInfraServiceStub.DeleteRouteTable(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateRouteTable(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.UpdateRouteTableRequest())
            res_obj = self.CloudInfraServiceStub.UpdateRouteTable(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.RouteTable().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListRouteTables(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.ListRouteTablesRequest())
            res_obj = self.CloudInfraServiceStub.ListRouteTables(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.ListRouteTablesResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetRouteTable(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.GetRouteTableRequest())
            res_obj = self.CloudInfraServiceStub.GetRouteTable(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.RouteTable().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def RouteTableGetStreaming(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.RouteTableGetRequest())
            res_obj = self.CloudInfraServiceStub.RouteTableGetStreaming(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.stream().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateRoute(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.CreateRouteRequest())
            res_obj = self.CloudInfraServiceStub.CreateRoute(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Route().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteRoute(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.DeleteRouteRequest())
            res_obj = self.CloudInfraServiceStub.DeleteRoute(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateRoute(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.UpdateRouteRequest())
            res_obj = self.CloudInfraServiceStub.UpdateRoute(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Route().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListRoutes(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.ListRoutesRequest())
            res_obj = self.CloudInfraServiceStub.ListRoutes(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.ListRoutesResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetRoute(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.GetRouteRequest())
            res_obj = self.CloudInfraServiceStub.GetRoute(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Route().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def RouteLookup(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.RouteLookupRequest())
            res_obj = self.CloudInfraServiceStub.RouteLookup(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.RouteLookupResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateUnderlayRoute(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.CreateUnderlayRouteRequest())
            res_obj = self.CloudInfraServiceStub.CreateUnderlayRoute(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.UnderlayRoute().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteUnderlayRoute(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.DeleteUnderlayRouteRequest())
            res_obj = self.CloudInfraServiceStub.DeleteUnderlayRoute(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateUnderlayRoute(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.UpdateUnderlayRouteRequest())
            res_obj = self.CloudInfraServiceStub.UpdateUnderlayRoute(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.UnderlayRoute().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListUnderlayRoutes(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.ListUnderlayRoutesRequest())
            res_obj = self.CloudInfraServiceStub.ListUnderlayRoutes(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.ListUnderlayRoutesResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetUnderlayRoute(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.GetUnderlayRouteRequest())
            res_obj = self.CloudInfraServiceStub.GetUnderlayRoute(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.UnderlayRoute().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CPRouteLookup(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.CPRouteGetRequest())
            res_obj = self.CloudInfraServiceStub.CPRouteLookup(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.CPRouteGetResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CPRouteRedistGet(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.CPRouteRedistGetRequest())
            res_obj = self.CloudInfraServiceStub.CPRouteRedistGet(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.CPRouteRedistGetResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateBgp(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.CreateBgpRequest())
            res_obj = self.CloudInfraServiceStub.CreateBgp(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Bgp().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteBgp(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.DeleteBgpRequest())
            res_obj = self.CloudInfraServiceStub.DeleteBgp(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateBgp(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.UpdateBgpRequest())
            res_obj = self.CloudInfraServiceStub.UpdateBgp(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Bgp().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListBgps(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.ListBgpsRequest())
            res_obj = self.CloudInfraServiceStub.ListBgps(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.ListBgpsResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetBgp(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.GetBgpRequest())
            res_obj = self.CloudInfraServiceStub.GetBgp(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Bgp().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateBGPPeer(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.CreateBGPPeerRequest())
            res_obj = self.CloudInfraServiceStub.CreateBGPPeer(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.BGPPeer().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteBGPPeer(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.DeleteBGPPeerRequest())
            res_obj = self.CloudInfraServiceStub.DeleteBGPPeer(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateBGPPeer(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.UpdateBGPPeerRequest())
            res_obj = self.CloudInfraServiceStub.UpdateBGPPeer(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.BGPPeer().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListBGPPeers(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.ListBGPPeersRequest())
            res_obj = self.CloudInfraServiceStub.ListBGPPeers(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.ListBGPPeersResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetBGPPeer(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.GetBGPPeerRequest())
            res_obj = self.CloudInfraServiceStub.GetBGPPeer(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.BGPPeer().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateBGPPeerAf(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.CreateBGPPeerAfRequest())
            res_obj = self.CloudInfraServiceStub.CreateBGPPeerAf(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.BGPPeerAf().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteBGPPeerAf(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.DeleteBGPPeerAfRequest())
            res_obj = self.CloudInfraServiceStub.DeleteBGPPeerAf(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateBGPPeerAf(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.UpdateBGPPeerAfRequest())
            res_obj = self.CloudInfraServiceStub.UpdateBGPPeerAf(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.BGPPeerAf().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListBGPPeerAfs(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.ListBGPPeerAfsRequest())
            res_obj = self.CloudInfraServiceStub.ListBGPPeerAfs(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.ListBGPPeerAfsResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetBGPPeerAf(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.GetBGPPeerAfRequest())
            res_obj = self.CloudInfraServiceStub.GetBGPPeerAf(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.BGPPeerAf().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def BGPClearRoute(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.BGPClearRouteRequest())
            res_obj = self.CloudInfraServiceStub.BGPClearRoute(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.BGPClearRouteResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def BGPNLRIPrefixGet(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.BGPNLRIPrefixGetRequest())
            res_obj = self.CloudInfraServiceStub.BGPNLRIPrefixGet(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.BGPNLRIPrefixGetResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def BGPPrfxCntrsGet(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.BGPPrfxCntrsGetRequest())
            res_obj = self.CloudInfraServiceStub.BGPPrfxCntrsGet(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.BGPPrfxCntrsGetResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def BGPAdjRibOutGet(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.BGPAdjRibOutGetRequest())
            res_obj = self.CloudInfraServiceStub.BGPAdjRibOutGet(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.BGPAdjRibOutGetResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateMapping(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.CreateMappingRequest())
            res_obj = self.CloudInfraServiceStub.CreateMapping(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Mapping().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteMapping(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.DeleteMappingRequest())
            res_obj = self.CloudInfraServiceStub.DeleteMapping(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateMapping(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.UpdateMappingRequest())
            res_obj = self.CloudInfraServiceStub.UpdateMapping(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Mapping().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListMappings(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.ListMappingsRequest())
            res_obj = self.CloudInfraServiceStub.ListMappings(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.ListMappingsResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetMapping(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.GetMappingRequest())
            res_obj = self.CloudInfraServiceStub.GetMapping(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Mapping().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def MappingGetStreaming(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.MappingGetRequest())
            res_obj = self.CloudInfraServiceStub.MappingGetStreaming(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.stream().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateNextHop(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.CreateNextHopRequest())
            res_obj = self.CloudInfraServiceStub.CreateNextHop(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.NextHop().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteNextHop(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.DeleteNextHopRequest())
            res_obj = self.CloudInfraServiceStub.DeleteNextHop(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateNextHop(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.UpdateNextHopRequest())
            res_obj = self.CloudInfraServiceStub.UpdateNextHop(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.NextHop().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListNextHop(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.ListNextHopRequest())
            res_obj = self.CloudInfraServiceStub.ListNextHop(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.ListNextHopsResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetNextHop(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.GetNextHopRequest())
            res_obj = self.CloudInfraServiceStub.GetNextHop(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.NextHop().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateNextHopGroup(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.CreateNextHopGroupRequest())
            res_obj = self.CloudInfraServiceStub.CreateNextHopGroup(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.NextHopGroup().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteNextHopGroup(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.DeleteNextHopGroupRequest())
            res_obj = self.CloudInfraServiceStub.DeleteNextHopGroup(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateNextHopGroup(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.UpdateNextHopGroupRequest())
            res_obj = self.CloudInfraServiceStub.UpdateNextHopGroup(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.NextHopGroup().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListNextHopGroups(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.ListNextHopGroupsRequest())
            res_obj = self.CloudInfraServiceStub.ListNextHopGroups(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.ListNextHopGroupsResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetNextHopGroup(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.GetNextHopGroupRequest())
            res_obj = self.CloudInfraServiceStub.GetNextHopGroup(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.NextHopGroup().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateSubnet(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.CreateSubnetRequest())
            res_obj = self.CloudInfraServiceStub.CreateSubnet(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Subnet().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteSubnet(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.DeleteSubnetRequest())
            res_obj = self.CloudInfraServiceStub.DeleteSubnet(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateSubnet(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.UpdateSubnetRequest())
            res_obj = self.CloudInfraServiceStub.UpdateSubnet(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Subnet().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListSubnets(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.ListSubnetsRequest())
            res_obj = self.CloudInfraServiceStub.ListSubnets(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.ListSubnetsResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetSubnet(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.GetSubnetRequest())
            res_obj = self.CloudInfraServiceStub.GetSubnet(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Subnet().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateTunnel(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.CreateTunnelRequest())
            res_obj = self.CloudInfraServiceStub.CreateTunnel(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Tunnel().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteTunnel(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.DeleteTunnelRequest())
            res_obj = self.CloudInfraServiceStub.DeleteTunnel(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateTunnel(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.UpdateTunnelRequest())
            res_obj = self.CloudInfraServiceStub.UpdateTunnel(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Tunnel().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListTunnels(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.ListTunnelsRequest())
            res_obj = self.CloudInfraServiceStub.ListTunnels(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.ListTunnelsResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetTunnel(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.GetTunnelRequest())
            res_obj = self.CloudInfraServiceStub.GetTunnel(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Tunnel().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateVpc(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.CreateVpcRequest())
            res_obj = self.CloudInfraServiceStub.CreateVpc(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Vpc().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteVpc(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.DeleteVpcRequest())
            res_obj = self.CloudInfraServiceStub.DeleteVpc(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateVpc(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.UpdateVpcRequest())
            res_obj = self.CloudInfraServiceStub.UpdateVpc(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Vpc().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListVpcs(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.ListVpcsRequest())
            res_obj = self.CloudInfraServiceStub.ListVpcs(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.ListVpcsResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetVpc(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.GetVpcRequest())
            res_obj = self.CloudInfraServiceStub.GetVpc(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Vpc().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateVPCPeer(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.CreateVPCPeerRequest())
            res_obj = self.CloudInfraServiceStub.CreateVPCPeer(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.VPCPeer().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteVPCPeer(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.DeleteVPCPeerRequest())
            res_obj = self.CloudInfraServiceStub.DeleteVPCPeer(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateVPCPeer(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.UpdateVPCPeerRequest())
            res_obj = self.CloudInfraServiceStub.UpdateVPCPeer(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.VPCPeer().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListVPCPeers(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.ListVPCPeersRequest())
            res_obj = self.CloudInfraServiceStub.ListVPCPeers(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.ListVPCPeersResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetVPCPeer(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.GetVPCPeerRequest())
            res_obj = self.CloudInfraServiceStub.GetVPCPeer(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.VPCPeer().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateSecurityPolicy(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.CreateSecurityPolicyRequest())
            res_obj = self.CloudInfraServiceStub.CreateSecurityPolicy(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.SecurityPolicy().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteSecurityPolicy(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.DeleteSecurityPolicyRequest())
            res_obj = self.CloudInfraServiceStub.DeleteSecurityPolicy(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateSecurityPolicy(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.UpdateSecurityPolicyRequest())
            res_obj = self.CloudInfraServiceStub.UpdateSecurityPolicy(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.SecurityPolicy().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListSecurityPolicys(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.ListSecurityPolicysRequest())
            res_obj = self.CloudInfraServiceStub.ListSecurityPolicys(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.ListSecurityPolicysResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetSecurityPolicy(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.GetSecurityPolicyRequest())
            res_obj = self.CloudInfraServiceStub.GetSecurityPolicy(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.SecurityPolicy().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateSecurityRule(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.CreateSecurityRuleRequest())
            res_obj = self.CloudInfraServiceStub.CreateSecurityRule(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.SecurityRule().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteSecurityRule(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.DeleteSecurityRuleRequest())
            res_obj = self.CloudInfraServiceStub.DeleteSecurityRule(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateSecurityRule(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.UpdateSecurityRuleRequest())
            res_obj = self.CloudInfraServiceStub.UpdateSecurityRule(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.SecurityRule().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListSecurityRules(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.ListSecurityRulesRequest())
            res_obj = self.CloudInfraServiceStub.ListSecurityRules(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.ListSecurityRulesResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetSecurityRule(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.GetSecurityRuleRequest())
            res_obj = self.CloudInfraServiceStub.GetSecurityRule(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.SecurityRule().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateSecurityProfile(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.CreateSecurityProfileRequest())
            res_obj = self.CloudInfraServiceStub.CreateSecurityProfile(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.SecurityProfile().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteSecurityProfile(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.DeleteSecurityProfileRequest())
            res_obj = self.CloudInfraServiceStub.DeleteSecurityProfile(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateSecurityProfile(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.UpdateSecurityProfileRequest())
            res_obj = self.CloudInfraServiceStub.UpdateSecurityProfile(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.SecurityProfile().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListSecurityProfiles(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.ListSecurityProfilesRequest())
            res_obj = self.CloudInfraServiceStub.ListSecurityProfiles(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.ListSecurityProfilesResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetSecurityProfile(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.GetSecurityProfileRequest())
            res_obj = self.CloudInfraServiceStub.GetSecurityProfile(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.SecurityProfile().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def SecurityPolicyGetStreaming(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.SecurityPolicyGetRequest())
            res_obj = self.CloudInfraServiceStub.SecurityPolicyGetStreaming(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.stream().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def SecurityPolicyLookup(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.cloudrpc_pb2.SecurityPolicyLookupRequest())
            res_obj = self.CloudInfraServiceStub.SecurityPolicyLookup(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.SecurityPolicyLookupResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

class NexthopAPI(Base):
    def __init__(self, parent):
        super(NexthopAPI, self).__init__(parent)

    @property
    def nexthop_messages(self):
        return nexthop_messages

    @property
    def nexthop_pb2(self):
        return nexthop_pb2

class InterfaceAPI(Base):
    def __init__(self, parent):
        super(InterfaceAPI, self).__init__(parent)

    @property
    def interface_messages(self):
        return interface_messages

    @property
    def interface_pb2(self):
        return interface_pb2

class SubnetAPI(Base):
    def __init__(self, parent):
        super(SubnetAPI, self).__init__(parent)

    @property
    def subnet_messages(self):
        return subnet_messages

    @property
    def subnet_pb2(self):
        return subnet_pb2

class PortAPI(Base):
    def __init__(self, parent):
        super(PortAPI, self).__init__(parent)

    @property
    def port_messages(self):
        return port_messages

    @property
    def port_pb2(self):
        return port_pb2

class NetworkpolicyAPI(Base):
    def __init__(self, parent):
        super(NetworkpolicyAPI, self).__init__(parent)

    @property
    def networkpolicy_messages(self):
        return networkpolicy_messages

    @property
    def networkpolicy_pb2(self):
        return networkpolicy_pb2

class CloudAPI(Base):
    def __init__(self, parent):
        super(CloudAPI, self).__init__(parent)

    @property
    def Route(self) -> RouteAPI:
        if self._Route_api_ is None:
            self._Route_ = RouteAPI(self)
        return self._Route_

    @property
    def Underlayroute(self) -> UnderlayrouteAPI:
        if self._Underlayroute_api_ is None:
            self._Underlayroute_ = UnderlayrouteAPI(self)
        return self._Underlayroute_

    @property
    def Mapping(self) -> MappingAPI:
        if self._Mapping_api_ is None:
            self._Mapping_ = MappingAPI(self)
        return self._Mapping_

    @property
    def Vnic(self) -> VnicAPI:
        if self._Vnic_api_ is None:
            self._Vnic_ = VnicAPI(self)
        return self._Vnic_

    @property
    def Tunnel(self) -> TunnelAPI:
        if self._Tunnel_api_ is None:
            self._Tunnel_ = TunnelAPI(self)
        return self._Tunnel_

    @property
    def Bgp(self) -> BgpAPI:
        if self._Bgp_api_ is None:
            self._Bgp_ = BgpAPI(self)
        return self._Bgp_

    @property
    def Vpc(self) -> VpcAPI:
        if self._Vpc_api_ is None:
            self._Vpc_ = VpcAPI(self)
        return self._Vpc_

    @property
    def Device(self) -> DeviceAPI:
        if self._Device_api_ is None:
            self._Device_ = DeviceAPI(self)
        return self._Device_

    @property
    def Cloudrpc(self) -> CloudrpcAPI:
        if self._Cloudrpc_api_ is None:
            self._Cloudrpc_ = CloudrpcAPI(self)
        return self._Cloudrpc_

    @property
    def Nexthop(self) -> NexthopAPI:
        if self._Nexthop_api_ is None:
            self._Nexthop_ = NexthopAPI(self)
        return self._Nexthop_

    @property
    def Interface(self) -> InterfaceAPI:
        if self._Interface_api_ is None:
            self._Interface_ = InterfaceAPI(self)
        return self._Interface_

    @property
    def Subnet(self) -> SubnetAPI:
        if self._Subnet_api_ is None:
            self._Subnet_ = SubnetAPI(self)
        return self._Subnet_

    @property
    def Port(self) -> PortAPI:
        if self._Port_api_ is None:
            self._Port_ = PortAPI(self)
        return self._Port_

    @property
    def Networkpolicy(self) -> NetworkpolicyAPI:
        if self._Networkpolicy_api_ is None:
            self._Networkpolicy_ = NetworkpolicyAPI(self)
        return self._Networkpolicy_

class L3XpuInfraMgrAPI(Base):
    def __init__(self, parent):
        super(L3XpuInfraMgrAPI, self).__init__(parent)
        self.VrfServiceStub = l3_xpu_infra_mgr_pb2_grpc.VrfServiceStub(self.channel)
        self.SviServiceStub = l3_xpu_infra_mgr_pb2_grpc.SviServiceStub(self.channel)

    @property
    def l3_xpu_infra_mgr_messages(self):
        return l3_xpu_infra_mgr_messages

    @property
    def l3_xpu_infra_mgr_pb2(self):
        return l3_xpu_infra_mgr_pb2

    def CreateVrf(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.l3_xpu_infra_mgr_pb2.CreateVrfRequest())
            res_obj = self.VrfServiceStub.CreateVrf(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l3_xpu_infra_mgr_message.Vrf().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListVrfs(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.l3_xpu_infra_mgr_pb2.ListVrfsRequest())
            res_obj = self.VrfServiceStub.ListVrfs(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l3_xpu_infra_mgr_message.ListVrfsResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetVrf(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.l3_xpu_infra_mgr_pb2.GetVrfRequest())
            res_obj = self.VrfServiceStub.GetVrf(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l3_xpu_infra_mgr_message.Vrf().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteVrf(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.l3_xpu_infra_mgr_pb2.DeleteVrfRequest())
            res_obj = self.VrfServiceStub.DeleteVrf(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l3_xpu_infra_mgr_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateVrf(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.l3_xpu_infra_mgr_pb2.UpdateVrfRequest())
            res_obj = self.VrfServiceStub.UpdateVrf(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l3_xpu_infra_mgr_message.Vrf().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateSvi(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.l3_xpu_infra_mgr_pb2.CreateSviRequest())
            res_obj = self.SviServiceStub.CreateSvi(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l3_xpu_infra_mgr_message.Svi().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListSvis(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.l3_xpu_infra_mgr_pb2.ListSvisRequest())
            res_obj = self.SviServiceStub.ListSvis(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l3_xpu_infra_mgr_message.ListSvisResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetSvi(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.l3_xpu_infra_mgr_pb2.GetSviRequest())
            res_obj = self.SviServiceStub.GetSvi(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l3_xpu_infra_mgr_message.Svi().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteSvi(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.l3_xpu_infra_mgr_pb2.DeleteSviRequest())
            res_obj = self.SviServiceStub.DeleteSvi(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l3_xpu_infra_mgr_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateSvi(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.l3_xpu_infra_mgr_pb2.UpdateSviRequest())
            res_obj = self.SviServiceStub.UpdateSvi(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l3_xpu_infra_mgr_message.Svi().deserialize(response)
        except grpc.RpcError as e:
            print(e)

class L2XpuInfraMgrAPI(Base):
    def __init__(self, parent):
        super(L2XpuInfraMgrAPI, self).__init__(parent)
        self.LogicalBridgeServiceStub = l2_xpu_infra_mgr_pb2_grpc.LogicalBridgeServiceStub(self.channel)
        self.BridgePortServiceStub = l2_xpu_infra_mgr_pb2_grpc.BridgePortServiceStub(self.channel)

    @property
    def l2_xpu_infra_mgr_messages(self):
        return l2_xpu_infra_mgr_messages

    @property
    def l2_xpu_infra_mgr_pb2(self):
        return l2_xpu_infra_mgr_pb2

    def create_logical_bridge(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.l2_xpu_infra_mgr_pb2.CreateLogicalBridgeRequest())
            res_obj = self.LogicalBridgeServiceStub.CreateLogicalBridge(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l2_xpu_infra_mgr_message.LogicalBridge().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def list_logical_bridges(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.l2_xpu_infra_mgr_pb2.ListLogicalBridgesRequest())
            res_obj = self.LogicalBridgeServiceStub.ListLogicalBridges(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l2_xpu_infra_mgr_message.ListLogicalBridgesResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def get_logical_bridge(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.l2_xpu_infra_mgr_pb2.GetLogicalBridgeRequest())
            res_obj = self.LogicalBridgeServiceStub.GetLogicalBridge(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l2_xpu_infra_mgr_message.LogicalBridge().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def delete_logical_bridge(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.l2_xpu_infra_mgr_pb2.DeleteLogicalBridgeRequest())
            res_obj = self.LogicalBridgeServiceStub.DeleteLogicalBridge(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l2_xpu_infra_mgr_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def update_logical_bridge(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.l2_xpu_infra_mgr_pb2.UpdateLogicalBridgeRequest())
            res_obj = self.LogicalBridgeServiceStub.UpdateLogicalBridge(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l2_xpu_infra_mgr_message.LogicalBridge().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def create_bridge_port(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.l2_xpu_infra_mgr_pb2.CreateBridgePortRequest())
            res_obj = self.BridgePortServiceStub.CreateBridgePort(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l2_xpu_infra_mgr_message.BridgePort().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def list_bridge_ports(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.l2_xpu_infra_mgr_pb2.ListBridgePortsRequest())
            res_obj = self.BridgePortServiceStub.ListBridgePorts(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l2_xpu_infra_mgr_message.ListBridgePortsResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def get_bridge_port(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.l2_xpu_infra_mgr_pb2.GetBridgePortRequest())
            res_obj = self.BridgePortServiceStub.GetBridgePort(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l2_xpu_infra_mgr_message.BridgePort().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def delete_bridge_port(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.l2_xpu_infra_mgr_pb2.DeleteBridgePortRequest())
            res_obj = self.BridgePortServiceStub.DeleteBridgePort(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l2_xpu_infra_mgr_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def update_bridge_port(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, self.l2_xpu_infra_mgr_pb2.UpdateBridgePortRequest())
            res_obj = self.BridgePortServiceStub.UpdateBridgePort(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l2_xpu_infra_mgr_message.BridgePort().deserialize(response)
        except grpc.RpcError as e:
            print(e)

class EvpnGwAPI(Base):
    def __init__(self, parent):
        super(EvpnGwAPI, self).__init__(parent)

    @property
    def L3XpuInfraMgr(self) -> L3XpuInfraMgrAPI:
        if self._L3XpuInfraMgr_api_ is None:
            self._L3XpuInfraMgr_ = L3XpuInfraMgrAPI(self)
        return self._L3XpuInfraMgr_

    @property
    def L2XpuInfraMgr(self) -> L2XpuInfraMgrAPI:
        if self._L2XpuInfraMgr_api_ is None:
            self._L2XpuInfraMgr_ = L2XpuInfraMgrAPI(self)
        return self._L2XpuInfraMgr_

class TelcoAPI(Base):
    def __init__(self, parent):
        super(TelcoAPI, self).__init__(parent)

    @property
    def telco_messages(self):
        return telco_messages

    @property
    def telco_pb2(self):
        return telco_pb2

class K8sAPI(Base):
    def __init__(self, parent):
        super(K8sAPI, self).__init__(parent)

    @property
    def k8s_messages(self):
        return k8s_messages

    @property
    def k8s_pb2(self):
        return k8s_pb2

class NetworkAPI(Base):
    def __init__(self, parent):
        super(NetworkAPI, self).__init__(parent)

    @property
    def Opinetcommon(self) -> OpinetcommonAPI:
        if self._Opinetcommon_api_ is None:
            self._Opinetcommon_ = OpinetcommonAPI(self)
        return self._Opinetcommon_


    @property
    def Cloud(self) -> CloudAPI:
        if self._Cloud_api_ is None:
            self._Cloud_ = CloudAPI(self)
        return self._Cloud_


    @property
    def EvpnGw(self) -> EvpnGwAPI:
        if self._EvpnGw_api_ is None:
            self._EvpnGw_ = EvpnGwAPI(self)
        return self._EvpnGw_


    @property
    def Telco(self) -> TelcoAPI:
        if self._Telco_api_ is None:
            self._Telco_ = TelcoAPI(self)
        return self._Telco_


    @property
    def K8s(self) -> K8sAPI:
        if self._K8s_api_ is None:
            self._K8s_ = K8sAPI(self)
        return self._K8s_

