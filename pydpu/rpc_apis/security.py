# AUTO-GENERATED CODE - DO NOT MODIFY
# Modifications may be overwritten during future updates
# Copyright (c) 2024 Keysight Technologies Inc, or its subsidiaries.
import grpc
from ..base import Base
from ..proto_imports.security import *
from google.protobuf import json_format
import json

class IpsecAPI(Base):
    def __init__(self, parent):
        super(IpsecAPI, self).__init__(parent)

    @property
    def ipsec_messages(self):
        return ipsec_messages

    @property
    def ipsec_pb2(self):
        return ipsec_pb2
        self.IPsecServiceStub = ipsec_pb2_grpc.IPsecServiceStub(self.channel)

    def get_ipsec_version(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, ipsec_pb2.IPsecVersionRequest)
            res_obj = self.IPsecServicestub.IPsecVersion(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.ipsec_message.IPsecVersionResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def get_ipsec_stats(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, ipsec_pb2.IPsecStatsRequest)
            res_obj = self.IPsecServicestub.IPsecStats(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.ipsec_message.IPsecStatsResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def initiate_ipsec(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, ipsec_pb2.IPsecInitiateRequest)
            res_obj = self.IPsecServicestub.IPsecInitiate(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.ipsec_message.IPsecInitiateResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def terminate_ipsec(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, ipsec_pb2.IPsecTerminateRequest)
            res_obj = self.IPsecServicestub.IPsecTerminate(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.ipsec_message.IPsecTerminateResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def rekey_ipsec(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, ipsec_pb2.IPsecRekeyRequest)
            res_obj = self.IPsecServicestub.IPsecRekey(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.ipsec_message.IPsecRekeyResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def IPsecListSas(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, ipsec_pb2.IPsecListSasRequest)
            res_obj = self.IPsecServicestub.IPsecListSas(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.ipsec_message.IPsecListSasResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def IPsecListConns(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, ipsec_pb2.IPsecListConnsRequest)
            res_obj = self.IPsecServicestub.IPsecListConns(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.ipsec_message.IPsecListConnsResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def IPsecListCerts(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, ipsec_pb2.IPsecListCertsRequest)
            res_obj = self.IPsecServicestub.IPsecListCerts(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.ipsec_message.IPsecListCertsResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def IPsecLoadConn(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, ipsec_pb2.IPsecLoadConnRequest)
            res_obj = self.IPsecServicestub.IPsecLoadConn(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.ipsec_message.IPsecLoadConnResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def IPsecUnloadConn(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, ipsec_pb2.IPsecUnloadConnRequest)
            res_obj = self.IPsecServicestub.IPsecUnloadConn(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.ipsec_message.IPsecUnloadConnResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

class SecurityAPI(Base):
    def __init__(self, parent):
        super(SecurityAPI, self).__init__(parent)

    @property
    def Ipsec(self) -> IpsecAPI:
        if self._Ipsec_api_ is None:
            self._Ipsec_ = IpsecAPI(self)
        return self._Ipsec_
