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

    def GetNetInterface(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, openconfig_interfaces_pb2.GetNetInterfaceRequest)
            res_obj = self.NetInterfaceServicestub.GetNetInterface(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.openconfig_interfaces_message.NetInterface().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListNetInterfaces(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, openconfig_interfaces_pb2.ListNetInterfacesRequest)
            res_obj = self.NetInterfaceServicestub.ListNetInterfaces(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.openconfig_interfaces_message.ListNetInterfacesResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateNetInterface(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, openconfig_interfaces_pb2.UpdateNetInterfaceRequest)
            res_obj = self.NetInterfaceServicestub.UpdateNetInterface(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.openconfig_interfaces_message.NetInterface().deserialize(response)
        except grpc.RpcError as e:
            print(e)

class NetworktypesAPI(Base):
    def __init__(self, parent):
        super(NetworktypesAPI, self).__init__(parent)

class OpinetcommonAPI(Base):
    def __init__(self, parent):
        super(OpinetcommonAPI, self).__init__(parent)

class RouteAPI(Base):
    def __init__(self, parent):
        super(RouteAPI, self).__init__(parent)

class UnderlayrouteAPI(Base):
    def __init__(self, parent):
        super(UnderlayrouteAPI, self).__init__(parent)

class MappingAPI(Base):
    def __init__(self, parent):
        super(MappingAPI, self).__init__(parent)

class VnicAPI(Base):
    def __init__(self, parent):
        super(VnicAPI, self).__init__(parent)

class TunnelAPI(Base):
    def __init__(self, parent):
        super(TunnelAPI, self).__init__(parent)

class BgpAPI(Base):
    def __init__(self, parent):
        super(BgpAPI, self).__init__(parent)

class VpcAPI(Base):
    def __init__(self, parent):
        super(VpcAPI, self).__init__(parent)

class DeviceAPI(Base):
    def __init__(self, parent):
        super(DeviceAPI, self).__init__(parent)

class CloudrpcAPI(Base):
    def __init__(self, parent):
        super(CloudrpcAPI, self).__init__(parent)
        self.CloudInfraServiceStub = cloudrpc_pb2_grpc.CloudInfraServiceStub(self.channel)

    def GetDeviceCapabilities(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.GetDeviceCapabilitiesRequest)
            res_obj = self.CloudInfraServicestub.GetDeviceCapabilities(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.DeviceCapabilities().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateDevice(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.CreateDeviceRequest)
            res_obj = self.CloudInfraServicestub.CreateDevice(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Device().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteDevice(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.DeleteDeviceRequest)
            res_obj = self.CloudInfraServicestub.DeleteDevice(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateDevice(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.UpdateDeviceRequest)
            res_obj = self.CloudInfraServicestub.UpdateDevice(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Device().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListDevices(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.ListDevicesRequest)
            res_obj = self.CloudInfraServicestub.ListDevices(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.ListDevicesResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetDevice(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.GetDeviceRequest)
            res_obj = self.CloudInfraServicestub.GetDevice(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Device().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdatePort(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.UpdatePortRequest)
            res_obj = self.CloudInfraServicestub.UpdatePort(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Port().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListPorts(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.ListPortsRequest)
            res_obj = self.CloudInfraServicestub.ListPorts(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.ListPortsResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetPort(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.GetPortRequest)
            res_obj = self.CloudInfraServicestub.GetPort(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Port().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateVnic(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.CreateVnicRequest)
            res_obj = self.CloudInfraServicestub.CreateVnic(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Vnic().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteVnic(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.DeleteVnicRequest)
            res_obj = self.CloudInfraServicestub.DeleteVnic(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateVnic(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.UpdateVnicRequest)
            res_obj = self.CloudInfraServicestub.UpdateVnic(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Vnic().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListVnics(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.ListVnicsRequest)
            res_obj = self.CloudInfraServicestub.ListVnics(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.ListVnicsResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetVnic(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.GetVnicRequest)
            res_obj = self.CloudInfraServicestub.GetVnic(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Vnic().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateInterface(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.CreateInterfaceRequest)
            res_obj = self.CloudInfraServicestub.CreateInterface(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Interface().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteInterface(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.DeleteInterfaceRequest)
            res_obj = self.CloudInfraServicestub.DeleteInterface(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateInterface(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.UpdateInterfaceRequest)
            res_obj = self.CloudInfraServicestub.UpdateInterface(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Interface().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListInterfaces(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.ListInterfacesRequest)
            res_obj = self.CloudInfraServicestub.ListInterfaces(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.ListInterfacesResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetInterface(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.GetInterfaceRequest)
            res_obj = self.CloudInfraServicestub.GetInterface(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Interface().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateRouteTable(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.CreateRouteTableRequest)
            res_obj = self.CloudInfraServicestub.CreateRouteTable(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.RouteTable().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteRouteTable(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.DeleteRouteTableRequest)
            res_obj = self.CloudInfraServicestub.DeleteRouteTable(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateRouteTable(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.UpdateRouteTableRequest)
            res_obj = self.CloudInfraServicestub.UpdateRouteTable(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.RouteTable().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListRouteTables(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.ListRouteTablesRequest)
            res_obj = self.CloudInfraServicestub.ListRouteTables(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.ListRouteTablesResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetRouteTable(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.GetRouteTableRequest)
            res_obj = self.CloudInfraServicestub.GetRouteTable(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.RouteTable().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def RouteTableGetStreaming(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.RouteTableGetRequest)
            res_obj = self.CloudInfraServicestub.RouteTableGetStreaming(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.stream().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateRoute(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.CreateRouteRequest)
            res_obj = self.CloudInfraServicestub.CreateRoute(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Route().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteRoute(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.DeleteRouteRequest)
            res_obj = self.CloudInfraServicestub.DeleteRoute(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateRoute(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.UpdateRouteRequest)
            res_obj = self.CloudInfraServicestub.UpdateRoute(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Route().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListRoutes(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.ListRoutesRequest)
            res_obj = self.CloudInfraServicestub.ListRoutes(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.ListRoutesResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetRoute(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.GetRouteRequest)
            res_obj = self.CloudInfraServicestub.GetRoute(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Route().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def RouteLookup(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.RouteLookupRequest)
            res_obj = self.CloudInfraServicestub.RouteLookup(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.RouteLookupResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateUnderlayRoute(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.CreateUnderlayRouteRequest)
            res_obj = self.CloudInfraServicestub.CreateUnderlayRoute(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.UnderlayRoute().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteUnderlayRoute(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.DeleteUnderlayRouteRequest)
            res_obj = self.CloudInfraServicestub.DeleteUnderlayRoute(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateUnderlayRoute(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.UpdateUnderlayRouteRequest)
            res_obj = self.CloudInfraServicestub.UpdateUnderlayRoute(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.UnderlayRoute().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListUnderlayRoutes(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.ListUnderlayRoutesRequest)
            res_obj = self.CloudInfraServicestub.ListUnderlayRoutes(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.ListUnderlayRoutesResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetUnderlayRoute(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.GetUnderlayRouteRequest)
            res_obj = self.CloudInfraServicestub.GetUnderlayRoute(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.UnderlayRoute().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CPRouteLookup(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.CPRouteGetRequest)
            res_obj = self.CloudInfraServicestub.CPRouteLookup(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.CPRouteGetResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CPRouteRedistGet(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.CPRouteRedistGetRequest)
            res_obj = self.CloudInfraServicestub.CPRouteRedistGet(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.CPRouteRedistGetResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateBgp(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.CreateBgpRequest)
            res_obj = self.CloudInfraServicestub.CreateBgp(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Bgp().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteBgp(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.DeleteBgpRequest)
            res_obj = self.CloudInfraServicestub.DeleteBgp(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateBgp(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.UpdateBgpRequest)
            res_obj = self.CloudInfraServicestub.UpdateBgp(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Bgp().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListBgps(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.ListBgpsRequest)
            res_obj = self.CloudInfraServicestub.ListBgps(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.ListBgpsResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetBgp(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.GetBgpRequest)
            res_obj = self.CloudInfraServicestub.GetBgp(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Bgp().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateBGPPeer(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.CreateBGPPeerRequest)
            res_obj = self.CloudInfraServicestub.CreateBGPPeer(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.BGPPeer().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteBGPPeer(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.DeleteBGPPeerRequest)
            res_obj = self.CloudInfraServicestub.DeleteBGPPeer(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateBGPPeer(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.UpdateBGPPeerRequest)
            res_obj = self.CloudInfraServicestub.UpdateBGPPeer(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.BGPPeer().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListBGPPeers(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.ListBGPPeersRequest)
            res_obj = self.CloudInfraServicestub.ListBGPPeers(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.ListBGPPeersResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetBGPPeer(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.GetBGPPeerRequest)
            res_obj = self.CloudInfraServicestub.GetBGPPeer(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.BGPPeer().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateBGPPeerAf(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.CreateBGPPeerAfRequest)
            res_obj = self.CloudInfraServicestub.CreateBGPPeerAf(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.BGPPeerAf().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteBGPPeerAf(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.DeleteBGPPeerAfRequest)
            res_obj = self.CloudInfraServicestub.DeleteBGPPeerAf(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateBGPPeerAf(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.UpdateBGPPeerAfRequest)
            res_obj = self.CloudInfraServicestub.UpdateBGPPeerAf(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.BGPPeerAf().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListBGPPeerAfs(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.ListBGPPeerAfsRequest)
            res_obj = self.CloudInfraServicestub.ListBGPPeerAfs(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.ListBGPPeerAfsResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetBGPPeerAf(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.GetBGPPeerAfRequest)
            res_obj = self.CloudInfraServicestub.GetBGPPeerAf(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.BGPPeerAf().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def BGPClearRoute(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.BGPClearRouteRequest)
            res_obj = self.CloudInfraServicestub.BGPClearRoute(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.BGPClearRouteResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def BGPNLRIPrefixGet(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.BGPNLRIPrefixGetRequest)
            res_obj = self.CloudInfraServicestub.BGPNLRIPrefixGet(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.BGPNLRIPrefixGetResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def BGPPrfxCntrsGet(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.BGPPrfxCntrsGetRequest)
            res_obj = self.CloudInfraServicestub.BGPPrfxCntrsGet(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.BGPPrfxCntrsGetResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def BGPAdjRibOutGet(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.BGPAdjRibOutGetRequest)
            res_obj = self.CloudInfraServicestub.BGPAdjRibOutGet(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.BGPAdjRibOutGetResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateMapping(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.CreateMappingRequest)
            res_obj = self.CloudInfraServicestub.CreateMapping(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Mapping().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteMapping(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.DeleteMappingRequest)
            res_obj = self.CloudInfraServicestub.DeleteMapping(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateMapping(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.UpdateMappingRequest)
            res_obj = self.CloudInfraServicestub.UpdateMapping(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Mapping().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListMappings(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.ListMappingsRequest)
            res_obj = self.CloudInfraServicestub.ListMappings(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.ListMappingsResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetMapping(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.GetMappingRequest)
            res_obj = self.CloudInfraServicestub.GetMapping(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Mapping().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def MappingGetStreaming(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.MappingGetRequest)
            res_obj = self.CloudInfraServicestub.MappingGetStreaming(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.stream().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateNextHop(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.CreateNextHopRequest)
            res_obj = self.CloudInfraServicestub.CreateNextHop(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.NextHop().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteNextHop(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.DeleteNextHopRequest)
            res_obj = self.CloudInfraServicestub.DeleteNextHop(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateNextHop(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.UpdateNextHopRequest)
            res_obj = self.CloudInfraServicestub.UpdateNextHop(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.NextHop().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListNextHop(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.ListNextHopRequest)
            res_obj = self.CloudInfraServicestub.ListNextHop(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.ListNextHopsResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetNextHop(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.GetNextHopRequest)
            res_obj = self.CloudInfraServicestub.GetNextHop(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.NextHop().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateNextHopGroup(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.CreateNextHopGroupRequest)
            res_obj = self.CloudInfraServicestub.CreateNextHopGroup(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.NextHopGroup().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteNextHopGroup(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.DeleteNextHopGroupRequest)
            res_obj = self.CloudInfraServicestub.DeleteNextHopGroup(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateNextHopGroup(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.UpdateNextHopGroupRequest)
            res_obj = self.CloudInfraServicestub.UpdateNextHopGroup(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.NextHopGroup().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListNextHopGroups(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.ListNextHopGroupsRequest)
            res_obj = self.CloudInfraServicestub.ListNextHopGroups(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.ListNextHopGroupsResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetNextHopGroup(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.GetNextHopGroupRequest)
            res_obj = self.CloudInfraServicestub.GetNextHopGroup(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.NextHopGroup().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateSubnet(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.CreateSubnetRequest)
            res_obj = self.CloudInfraServicestub.CreateSubnet(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Subnet().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteSubnet(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.DeleteSubnetRequest)
            res_obj = self.CloudInfraServicestub.DeleteSubnet(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateSubnet(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.UpdateSubnetRequest)
            res_obj = self.CloudInfraServicestub.UpdateSubnet(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Subnet().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListSubnets(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.ListSubnetsRequest)
            res_obj = self.CloudInfraServicestub.ListSubnets(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.ListSubnetsResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetSubnet(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.GetSubnetRequest)
            res_obj = self.CloudInfraServicestub.GetSubnet(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Subnet().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateTunnel(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.CreateTunnelRequest)
            res_obj = self.CloudInfraServicestub.CreateTunnel(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Tunnel().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteTunnel(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.DeleteTunnelRequest)
            res_obj = self.CloudInfraServicestub.DeleteTunnel(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateTunnel(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.UpdateTunnelRequest)
            res_obj = self.CloudInfraServicestub.UpdateTunnel(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Tunnel().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListTunnels(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.ListTunnelsRequest)
            res_obj = self.CloudInfraServicestub.ListTunnels(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.ListTunnelsResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetTunnel(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.GetTunnelRequest)
            res_obj = self.CloudInfraServicestub.GetTunnel(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Tunnel().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateVpc(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.CreateVpcRequest)
            res_obj = self.CloudInfraServicestub.CreateVpc(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Vpc().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteVpc(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.DeleteVpcRequest)
            res_obj = self.CloudInfraServicestub.DeleteVpc(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateVpc(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.UpdateVpcRequest)
            res_obj = self.CloudInfraServicestub.UpdateVpc(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Vpc().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListVpcs(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.ListVpcsRequest)
            res_obj = self.CloudInfraServicestub.ListVpcs(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.ListVpcsResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetVpc(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.GetVpcRequest)
            res_obj = self.CloudInfraServicestub.GetVpc(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.Vpc().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateVPCPeer(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.CreateVPCPeerRequest)
            res_obj = self.CloudInfraServicestub.CreateVPCPeer(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.VPCPeer().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteVPCPeer(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.DeleteVPCPeerRequest)
            res_obj = self.CloudInfraServicestub.DeleteVPCPeer(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateVPCPeer(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.UpdateVPCPeerRequest)
            res_obj = self.CloudInfraServicestub.UpdateVPCPeer(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.VPCPeer().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListVPCPeers(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.ListVPCPeersRequest)
            res_obj = self.CloudInfraServicestub.ListVPCPeers(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.ListVPCPeersResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetVPCPeer(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.GetVPCPeerRequest)
            res_obj = self.CloudInfraServicestub.GetVPCPeer(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.VPCPeer().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateSecurityPolicy(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.CreateSecurityPolicyRequest)
            res_obj = self.CloudInfraServicestub.CreateSecurityPolicy(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.SecurityPolicy().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteSecurityPolicy(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.DeleteSecurityPolicyRequest)
            res_obj = self.CloudInfraServicestub.DeleteSecurityPolicy(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateSecurityPolicy(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.UpdateSecurityPolicyRequest)
            res_obj = self.CloudInfraServicestub.UpdateSecurityPolicy(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.SecurityPolicy().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListSecurityPolicys(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.ListSecurityPolicysRequest)
            res_obj = self.CloudInfraServicestub.ListSecurityPolicys(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.ListSecurityPolicysResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetSecurityPolicy(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.GetSecurityPolicyRequest)
            res_obj = self.CloudInfraServicestub.GetSecurityPolicy(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.SecurityPolicy().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateSecurityRule(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.CreateSecurityRuleRequest)
            res_obj = self.CloudInfraServicestub.CreateSecurityRule(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.SecurityRule().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteSecurityRule(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.DeleteSecurityRuleRequest)
            res_obj = self.CloudInfraServicestub.DeleteSecurityRule(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateSecurityRule(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.UpdateSecurityRuleRequest)
            res_obj = self.CloudInfraServicestub.UpdateSecurityRule(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.SecurityRule().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListSecurityRules(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.ListSecurityRulesRequest)
            res_obj = self.CloudInfraServicestub.ListSecurityRules(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.ListSecurityRulesResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetSecurityRule(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.GetSecurityRuleRequest)
            res_obj = self.CloudInfraServicestub.GetSecurityRule(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.SecurityRule().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateSecurityProfile(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.CreateSecurityProfileRequest)
            res_obj = self.CloudInfraServicestub.CreateSecurityProfile(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.SecurityProfile().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteSecurityProfile(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.DeleteSecurityProfileRequest)
            res_obj = self.CloudInfraServicestub.DeleteSecurityProfile(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateSecurityProfile(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.UpdateSecurityProfileRequest)
            res_obj = self.CloudInfraServicestub.UpdateSecurityProfile(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.SecurityProfile().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListSecurityProfiles(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.ListSecurityProfilesRequest)
            res_obj = self.CloudInfraServicestub.ListSecurityProfiles(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.ListSecurityProfilesResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetSecurityProfile(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.GetSecurityProfileRequest)
            res_obj = self.CloudInfraServicestub.GetSecurityProfile(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.SecurityProfile().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def SecurityPolicyGetStreaming(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.SecurityPolicyGetRequest)
            res_obj = self.CloudInfraServicestub.SecurityPolicyGetStreaming(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.stream().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def SecurityPolicyLookup(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, cloudrpc_pb2.SecurityPolicyLookupRequest)
            res_obj = self.CloudInfraServicestub.SecurityPolicyLookup(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.cloudrpc_message.SecurityPolicyLookupResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

class NexthopAPI(Base):
    def __init__(self, parent):
        super(NexthopAPI, self).__init__(parent)

class InterfaceAPI(Base):
    def __init__(self, parent):
        super(InterfaceAPI, self).__init__(parent)

class SubnetAPI(Base):
    def __init__(self, parent):
        super(SubnetAPI, self).__init__(parent)

class PortAPI(Base):
    def __init__(self, parent):
        super(PortAPI, self).__init__(parent)

class NetworkpolicyAPI(Base):
    def __init__(self, parent):
        super(NetworkpolicyAPI, self).__init__(parent)

class CloudAPI(Base):
    def __init__(self, parent):
        super(CloudAPI, self).__init__(parent)

class L3XpuInfraMgrAPI(Base):
    def __init__(self, parent):
        super(L3XpuInfraMgrAPI, self).__init__(parent)
        self.VrfServiceStub = l3_xpu_infra_mgr_pb2_grpc.VrfServiceStub(self.channel)
        self.SviServiceStub = l3_xpu_infra_mgr_pb2_grpc.SviServiceStub(self.channel)

    def CreateVrf(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, l3_xpu_infra_mgr_pb2.CreateVrfRequest)
            res_obj = self.VrfServicestub.CreateVrf(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l3_xpu_infra_mgr_message.Vrf().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListVrfs(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, l3_xpu_infra_mgr_pb2.ListVrfsRequest)
            res_obj = self.VrfServicestub.ListVrfs(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l3_xpu_infra_mgr_message.ListVrfsResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetVrf(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, l3_xpu_infra_mgr_pb2.GetVrfRequest)
            res_obj = self.VrfServicestub.GetVrf(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l3_xpu_infra_mgr_message.Vrf().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteVrf(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, l3_xpu_infra_mgr_pb2.DeleteVrfRequest)
            res_obj = self.VrfServicestub.DeleteVrf(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l3_xpu_infra_mgr_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateVrf(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, l3_xpu_infra_mgr_pb2.UpdateVrfRequest)
            res_obj = self.VrfServicestub.UpdateVrf(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l3_xpu_infra_mgr_message.Vrf().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateSvi(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, l3_xpu_infra_mgr_pb2.CreateSviRequest)
            res_obj = self.VrfServicestub.CreateSvi(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l3_xpu_infra_mgr_message.Svi().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListSvis(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, l3_xpu_infra_mgr_pb2.ListSvisRequest)
            res_obj = self.VrfServicestub.ListSvis(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l3_xpu_infra_mgr_message.ListSvisResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetSvi(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, l3_xpu_infra_mgr_pb2.GetSviRequest)
            res_obj = self.VrfServicestub.GetSvi(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l3_xpu_infra_mgr_message.Svi().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteSvi(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, l3_xpu_infra_mgr_pb2.DeleteSviRequest)
            res_obj = self.VrfServicestub.DeleteSvi(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l3_xpu_infra_mgr_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateSvi(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, l3_xpu_infra_mgr_pb2.UpdateSviRequest)
            res_obj = self.VrfServicestub.UpdateSvi(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l3_xpu_infra_mgr_message.Svi().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateSvi(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, l3_xpu_infra_mgr_pb2.CreateSviRequest)
            res_obj = self.SviServicestub.CreateSvi(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l3_xpu_infra_mgr_message.Svi().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListSvis(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, l3_xpu_infra_mgr_pb2.ListSvisRequest)
            res_obj = self.SviServicestub.ListSvis(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l3_xpu_infra_mgr_message.ListSvisResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetSvi(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, l3_xpu_infra_mgr_pb2.GetSviRequest)
            res_obj = self.SviServicestub.GetSvi(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l3_xpu_infra_mgr_message.Svi().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteSvi(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, l3_xpu_infra_mgr_pb2.DeleteSviRequest)
            res_obj = self.SviServicestub.DeleteSvi(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l3_xpu_infra_mgr_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateSvi(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, l3_xpu_infra_mgr_pb2.UpdateSviRequest)
            res_obj = self.SviServicestub.UpdateSvi(request=req_obj)
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

    def CreateLogicalBridge(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, l2_xpu_infra_mgr_pb2.CreateLogicalBridgeRequest)
            res_obj = self.LogicalBridgeServicestub.CreateLogicalBridge(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l2_xpu_infra_mgr_message.LogicalBridge().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListLogicalBridges(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, l2_xpu_infra_mgr_pb2.ListLogicalBridgesRequest)
            res_obj = self.LogicalBridgeServicestub.ListLogicalBridges(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l2_xpu_infra_mgr_message.ListLogicalBridgesResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetLogicalBridge(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, l2_xpu_infra_mgr_pb2.GetLogicalBridgeRequest)
            res_obj = self.LogicalBridgeServicestub.GetLogicalBridge(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l2_xpu_infra_mgr_message.LogicalBridge().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteLogicalBridge(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, l2_xpu_infra_mgr_pb2.DeleteLogicalBridgeRequest)
            res_obj = self.LogicalBridgeServicestub.DeleteLogicalBridge(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l2_xpu_infra_mgr_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateLogicalBridge(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, l2_xpu_infra_mgr_pb2.UpdateLogicalBridgeRequest)
            res_obj = self.LogicalBridgeServicestub.UpdateLogicalBridge(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l2_xpu_infra_mgr_message.LogicalBridge().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateBridgePort(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, l2_xpu_infra_mgr_pb2.CreateBridgePortRequest)
            res_obj = self.LogicalBridgeServicestub.CreateBridgePort(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l2_xpu_infra_mgr_message.BridgePort().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListBridgePorts(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, l2_xpu_infra_mgr_pb2.ListBridgePortsRequest)
            res_obj = self.LogicalBridgeServicestub.ListBridgePorts(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l2_xpu_infra_mgr_message.ListBridgePortsResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetBridgePort(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, l2_xpu_infra_mgr_pb2.GetBridgePortRequest)
            res_obj = self.LogicalBridgeServicestub.GetBridgePort(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l2_xpu_infra_mgr_message.BridgePort().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteBridgePort(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, l2_xpu_infra_mgr_pb2.DeleteBridgePortRequest)
            res_obj = self.LogicalBridgeServicestub.DeleteBridgePort(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l2_xpu_infra_mgr_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateBridgePort(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, l2_xpu_infra_mgr_pb2.UpdateBridgePortRequest)
            res_obj = self.LogicalBridgeServicestub.UpdateBridgePort(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l2_xpu_infra_mgr_message.BridgePort().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateBridgePort(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, l2_xpu_infra_mgr_pb2.CreateBridgePortRequest)
            res_obj = self.BridgePortServicestub.CreateBridgePort(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l2_xpu_infra_mgr_message.BridgePort().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListBridgePorts(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, l2_xpu_infra_mgr_pb2.ListBridgePortsRequest)
            res_obj = self.BridgePortServicestub.ListBridgePorts(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l2_xpu_infra_mgr_message.ListBridgePortsResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetBridgePort(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, l2_xpu_infra_mgr_pb2.GetBridgePortRequest)
            res_obj = self.BridgePortServicestub.GetBridgePort(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l2_xpu_infra_mgr_message.BridgePort().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteBridgePort(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, l2_xpu_infra_mgr_pb2.DeleteBridgePortRequest)
            res_obj = self.BridgePortServicestub.DeleteBridgePort(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l2_xpu_infra_mgr_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateBridgePort(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, l2_xpu_infra_mgr_pb2.UpdateBridgePortRequest)
            res_obj = self.BridgePortServicestub.UpdateBridgePort(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.l2_xpu_infra_mgr_message.BridgePort().deserialize(response)
        except grpc.RpcError as e:
            print(e)

class EvpnGwAPI(Base):
    def __init__(self, parent):
        super(EvpnGwAPI, self).__init__(parent)

class TelcoAPI(Base):
    def __init__(self, parent):
        super(TelcoAPI, self).__init__(parent)

class K8sAPI(Base):
    def __init__(self, parent):
        super(K8sAPI, self).__init__(parent)

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

