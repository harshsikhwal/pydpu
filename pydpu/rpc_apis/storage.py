# AUTO-GENERATED CODE - DO NOT MODIFY
# Modifications may be overwritten during future updates
# Copyright (c) 2024 Keysight Technologies Inc, or its subsidiaries.
import grpc
from ..base import Base
from ..proto_imports.storage import *
from google.protobuf import json_format
import json

class FrontendVirtioFsAPI(Base):
    def __init__(self, parent):
        super(FrontendVirtioFsAPI, self).__init__(parent)

class MiddleendQosVolumeAPI(Base):
    def __init__(self, parent):
        super(MiddleendQosVolumeAPI, self).__init__(parent)
        self.MiddleendQosVolumeServiceStub = middleend_qos_volume_pb2_grpc.MiddleendQosVolumeServiceStub(self.channel)

    def CreateQosVolume(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, middleend_qos_volume_pb2.CreateQosVolumeRequest)
            res_obj = self.MiddleendQosVolumeServicestub.CreateQosVolume(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.middleend_qos_volume_message.QosVolume().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteQosVolume(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, middleend_qos_volume_pb2.DeleteQosVolumeRequest)
            res_obj = self.MiddleendQosVolumeServicestub.DeleteQosVolume(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.middleend_qos_volume_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateQosVolume(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, middleend_qos_volume_pb2.UpdateQosVolumeRequest)
            res_obj = self.MiddleendQosVolumeServicestub.UpdateQosVolume(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.middleend_qos_volume_message.QosVolume().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListQosVolumes(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, middleend_qos_volume_pb2.ListQosVolumesRequest)
            res_obj = self.MiddleendQosVolumeServicestub.ListQosVolumes(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.middleend_qos_volume_message.ListQosVolumesResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetQosVolume(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, middleend_qos_volume_pb2.GetQosVolumeRequest)
            res_obj = self.MiddleendQosVolumeServicestub.GetQosVolume(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.middleend_qos_volume_message.QosVolume().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def StatsQosVolume(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, middleend_qos_volume_pb2.StatsQosVolumeRequest)
            res_obj = self.MiddleendQosVolumeServicestub.StatsQosVolume(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.middleend_qos_volume_message.StatsQosVolumeResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

class BackendNvmeAPI(Base):
    def __init__(self, parent):
        super(BackendNvmeAPI, self).__init__(parent)
        self.NvmeRemoteControllerServiceStub = backend_nvme_pb2_grpc.NvmeRemoteControllerServiceStub(self.channel)

    def CreateNvmeRemoteController(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_nvme_pb2.CreateNvmeRemoteControllerRequest)
            res_obj = self.NvmeRemoteControllerServicestub.CreateNvmeRemoteController(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_nvme_message.NvmeRemoteController().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteNvmeRemoteController(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_nvme_pb2.DeleteNvmeRemoteControllerRequest)
            res_obj = self.NvmeRemoteControllerServicestub.DeleteNvmeRemoteController(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_nvme_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateNvmeRemoteController(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_nvme_pb2.UpdateNvmeRemoteControllerRequest)
            res_obj = self.NvmeRemoteControllerServicestub.UpdateNvmeRemoteController(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_nvme_message.NvmeRemoteController().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListNvmeRemoteControllers(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_nvme_pb2.ListNvmeRemoteControllersRequest)
            res_obj = self.NvmeRemoteControllerServicestub.ListNvmeRemoteControllers(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_nvme_message.ListNvmeRemoteControllersResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetNvmeRemoteController(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_nvme_pb2.GetNvmeRemoteControllerRequest)
            res_obj = self.NvmeRemoteControllerServicestub.GetNvmeRemoteController(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_nvme_message.NvmeRemoteController().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ResetNvmeRemoteController(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_nvme_pb2.ResetNvmeRemoteControllerRequest)
            res_obj = self.NvmeRemoteControllerServicestub.ResetNvmeRemoteController(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_nvme_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def StatsNvmeRemoteController(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_nvme_pb2.StatsNvmeRemoteControllerRequest)
            res_obj = self.NvmeRemoteControllerServicestub.StatsNvmeRemoteController(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_nvme_message.StatsNvmeRemoteControllerResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListNvmeRemoteNamespaces(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_nvme_pb2.ListNvmeRemoteNamespacesRequest)
            res_obj = self.NvmeRemoteControllerServicestub.ListNvmeRemoteNamespaces(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_nvme_message.ListNvmeRemoteNamespacesResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetNvmeRemoteNamespace(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_nvme_pb2.GetNvmeRemoteNamespaceRequest)
            res_obj = self.NvmeRemoteControllerServicestub.GetNvmeRemoteNamespace(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_nvme_message.NvmeRemoteNamespace().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateNvmePath(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_nvme_pb2.CreateNvmePathRequest)
            res_obj = self.NvmeRemoteControllerServicestub.CreateNvmePath(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_nvme_message.NvmePath().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteNvmePath(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_nvme_pb2.DeleteNvmePathRequest)
            res_obj = self.NvmeRemoteControllerServicestub.DeleteNvmePath(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_nvme_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateNvmePath(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_nvme_pb2.UpdateNvmePathRequest)
            res_obj = self.NvmeRemoteControllerServicestub.UpdateNvmePath(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_nvme_message.NvmePath().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListNvmePaths(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_nvme_pb2.ListNvmePathsRequest)
            res_obj = self.NvmeRemoteControllerServicestub.ListNvmePaths(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_nvme_message.ListNvmePathsResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetNvmePath(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_nvme_pb2.GetNvmePathRequest)
            res_obj = self.NvmeRemoteControllerServicestub.GetNvmePath(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_nvme_message.NvmePath().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def StatsNvmePath(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_nvme_pb2.StatsNvmePathRequest)
            res_obj = self.NvmeRemoteControllerServicestub.StatsNvmePath(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_nvme_message.StatsNvmePathResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

class FrontendVirtioScsiAPI(Base):
    def __init__(self, parent):
        super(FrontendVirtioScsiAPI, self).__init__(parent)
        self.FrontendVirtioScsiServiceStub = frontend_virtio_scsi_pb2_grpc.FrontendVirtioScsiServiceStub(self.channel)

    def CreateVirtioScsiTarget(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_scsi_pb2.CreateVirtioScsiTargetRequest)
            res_obj = self.FrontendVirtioScsiServicestub.CreateVirtioScsiTarget(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_scsi_message.VirtioScsiTarget().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteVirtioScsiTarget(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_scsi_pb2.DeleteVirtioScsiTargetRequest)
            res_obj = self.FrontendVirtioScsiServicestub.DeleteVirtioScsiTarget(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_scsi_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateVirtioScsiTarget(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_scsi_pb2.UpdateVirtioScsiTargetRequest)
            res_obj = self.FrontendVirtioScsiServicestub.UpdateVirtioScsiTarget(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_scsi_message.VirtioScsiTarget().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListVirtioScsiTargets(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_scsi_pb2.ListVirtioScsiTargetsRequest)
            res_obj = self.FrontendVirtioScsiServicestub.ListVirtioScsiTargets(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_scsi_message.ListVirtioScsiTargetsResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetVirtioScsiTarget(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_scsi_pb2.GetVirtioScsiTargetRequest)
            res_obj = self.FrontendVirtioScsiServicestub.GetVirtioScsiTarget(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_scsi_message.VirtioScsiTarget().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def StatsVirtioScsiTarget(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_scsi_pb2.StatsVirtioScsiTargetRequest)
            res_obj = self.FrontendVirtioScsiServicestub.StatsVirtioScsiTarget(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_scsi_message.StatsVirtioScsiTargetResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateVirtioScsiController(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_scsi_pb2.CreateVirtioScsiControllerRequest)
            res_obj = self.FrontendVirtioScsiServicestub.CreateVirtioScsiController(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_scsi_message.VirtioScsiController().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteVirtioScsiController(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_scsi_pb2.DeleteVirtioScsiControllerRequest)
            res_obj = self.FrontendVirtioScsiServicestub.DeleteVirtioScsiController(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_scsi_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateVirtioScsiController(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_scsi_pb2.UpdateVirtioScsiControllerRequest)
            res_obj = self.FrontendVirtioScsiServicestub.UpdateVirtioScsiController(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_scsi_message.VirtioScsiController().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListVirtioScsiControllers(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_scsi_pb2.ListVirtioScsiControllersRequest)
            res_obj = self.FrontendVirtioScsiServicestub.ListVirtioScsiControllers(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_scsi_message.ListVirtioScsiControllersResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetVirtioScsiController(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_scsi_pb2.GetVirtioScsiControllerRequest)
            res_obj = self.FrontendVirtioScsiServicestub.GetVirtioScsiController(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_scsi_message.VirtioScsiController().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def StatsVirtioScsiController(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_scsi_pb2.StatsVirtioScsiControllerRequest)
            res_obj = self.FrontendVirtioScsiServicestub.StatsVirtioScsiController(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_scsi_message.StatsVirtioScsiControllerResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateVirtioScsiLun(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_scsi_pb2.CreateVirtioScsiLunRequest)
            res_obj = self.FrontendVirtioScsiServicestub.CreateVirtioScsiLun(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_scsi_message.VirtioScsiLun().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteVirtioScsiLun(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_scsi_pb2.DeleteVirtioScsiLunRequest)
            res_obj = self.FrontendVirtioScsiServicestub.DeleteVirtioScsiLun(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_scsi_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateVirtioScsiLun(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_scsi_pb2.UpdateVirtioScsiLunRequest)
            res_obj = self.FrontendVirtioScsiServicestub.UpdateVirtioScsiLun(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_scsi_message.VirtioScsiLun().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListVirtioScsiLuns(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_scsi_pb2.ListVirtioScsiLunsRequest)
            res_obj = self.FrontendVirtioScsiServicestub.ListVirtioScsiLuns(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_scsi_message.ListVirtioScsiLunsResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetVirtioScsiLun(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_scsi_pb2.GetVirtioScsiLunRequest)
            res_obj = self.FrontendVirtioScsiServicestub.GetVirtioScsiLun(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_scsi_message.VirtioScsiLun().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def StatsVirtioScsiLun(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_scsi_pb2.StatsVirtioScsiLunRequest)
            res_obj = self.FrontendVirtioScsiServicestub.StatsVirtioScsiLun(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_scsi_message.StatsVirtioScsiLunResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

class FrontendNvmeAPI(Base):
    def __init__(self, parent):
        super(FrontendNvmeAPI, self).__init__(parent)
        self.FrontendNvmeServiceStub = frontend_nvme_pb2_grpc.FrontendNvmeServiceStub(self.channel)

    def CreateNvmeSubsystem(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_nvme_pb2.CreateNvmeSubsystemRequest)
            res_obj = self.FrontendNvmeServicestub.CreateNvmeSubsystem(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_nvme_message.NvmeSubsystem().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteNvmeSubsystem(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_nvme_pb2.DeleteNvmeSubsystemRequest)
            res_obj = self.FrontendNvmeServicestub.DeleteNvmeSubsystem(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_nvme_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateNvmeSubsystem(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_nvme_pb2.UpdateNvmeSubsystemRequest)
            res_obj = self.FrontendNvmeServicestub.UpdateNvmeSubsystem(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_nvme_message.NvmeSubsystem().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListNvmeSubsystems(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_nvme_pb2.ListNvmeSubsystemsRequest)
            res_obj = self.FrontendNvmeServicestub.ListNvmeSubsystems(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_nvme_message.ListNvmeSubsystemsResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetNvmeSubsystem(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_nvme_pb2.GetNvmeSubsystemRequest)
            res_obj = self.FrontendNvmeServicestub.GetNvmeSubsystem(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_nvme_message.NvmeSubsystem().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def StatsNvmeSubsystem(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_nvme_pb2.StatsNvmeSubsystemRequest)
            res_obj = self.FrontendNvmeServicestub.StatsNvmeSubsystem(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_nvme_message.StatsNvmeSubsystemResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateNvmeController(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_nvme_pb2.CreateNvmeControllerRequest)
            res_obj = self.FrontendNvmeServicestub.CreateNvmeController(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_nvme_message.NvmeController().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteNvmeController(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_nvme_pb2.DeleteNvmeControllerRequest)
            res_obj = self.FrontendNvmeServicestub.DeleteNvmeController(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_nvme_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateNvmeController(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_nvme_pb2.UpdateNvmeControllerRequest)
            res_obj = self.FrontendNvmeServicestub.UpdateNvmeController(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_nvme_message.NvmeController().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListNvmeControllers(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_nvme_pb2.ListNvmeControllersRequest)
            res_obj = self.FrontendNvmeServicestub.ListNvmeControllers(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_nvme_message.ListNvmeControllersResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetNvmeController(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_nvme_pb2.GetNvmeControllerRequest)
            res_obj = self.FrontendNvmeServicestub.GetNvmeController(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_nvme_message.NvmeController().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def StatsNvmeController(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_nvme_pb2.StatsNvmeControllerRequest)
            res_obj = self.FrontendNvmeServicestub.StatsNvmeController(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_nvme_message.StatsNvmeControllerResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateNvmeNamespace(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_nvme_pb2.CreateNvmeNamespaceRequest)
            res_obj = self.FrontendNvmeServicestub.CreateNvmeNamespace(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_nvme_message.NvmeNamespace().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteNvmeNamespace(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_nvme_pb2.DeleteNvmeNamespaceRequest)
            res_obj = self.FrontendNvmeServicestub.DeleteNvmeNamespace(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_nvme_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateNvmeNamespace(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_nvme_pb2.UpdateNvmeNamespaceRequest)
            res_obj = self.FrontendNvmeServicestub.UpdateNvmeNamespace(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_nvme_message.NvmeNamespace().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListNvmeNamespaces(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_nvme_pb2.ListNvmeNamespacesRequest)
            res_obj = self.FrontendNvmeServicestub.ListNvmeNamespaces(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_nvme_message.ListNvmeNamespacesResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetNvmeNamespace(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_nvme_pb2.GetNvmeNamespaceRequest)
            res_obj = self.FrontendNvmeServicestub.GetNvmeNamespace(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_nvme_message.NvmeNamespace().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def StatsNvmeNamespace(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_nvme_pb2.StatsNvmeNamespaceRequest)
            res_obj = self.FrontendNvmeServicestub.StatsNvmeNamespace(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_nvme_message.StatsNvmeNamespaceResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

class FrontendVirtioBlkAPI(Base):
    def __init__(self, parent):
        super(FrontendVirtioBlkAPI, self).__init__(parent)
        self.FrontendVirtioBlkServiceStub = frontend_virtio_blk_pb2_grpc.FrontendVirtioBlkServiceStub(self.channel)

    def CreateVirtioBlk(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_blk_pb2.CreateVirtioBlkRequest)
            res_obj = self.FrontendVirtioBlkServicestub.CreateVirtioBlk(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_blk_message.VirtioBlk().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteVirtioBlk(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_blk_pb2.DeleteVirtioBlkRequest)
            res_obj = self.FrontendVirtioBlkServicestub.DeleteVirtioBlk(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_blk_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateVirtioBlk(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_blk_pb2.UpdateVirtioBlkRequest)
            res_obj = self.FrontendVirtioBlkServicestub.UpdateVirtioBlk(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_blk_message.VirtioBlk().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListVirtioBlks(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_blk_pb2.ListVirtioBlksRequest)
            res_obj = self.FrontendVirtioBlkServicestub.ListVirtioBlks(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_blk_message.ListVirtioBlksResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetVirtioBlk(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_blk_pb2.GetVirtioBlkRequest)
            res_obj = self.FrontendVirtioBlkServicestub.GetVirtioBlk(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_blk_message.VirtioBlk().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def StatsVirtioBlk(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_blk_pb2.StatsVirtioBlkRequest)
            res_obj = self.FrontendVirtioBlkServicestub.StatsVirtioBlk(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_blk_message.StatsVirtioBlkResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

class OpicommonAPI(Base):
    def __init__(self, parent):
        super(OpicommonAPI, self).__init__(parent)

class MiddleendEncryptionAPI(Base):
    def __init__(self, parent):
        super(MiddleendEncryptionAPI, self).__init__(parent)
        self.MiddleendEncryptionServiceStub = middleend_encryption_pb2_grpc.MiddleendEncryptionServiceStub(self.channel)

    def CreateEncryptedVolume(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, middleend_encryption_pb2.CreateEncryptedVolumeRequest)
            res_obj = self.MiddleendEncryptionServicestub.CreateEncryptedVolume(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.middleend_encryption_message.EncryptedVolume().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteEncryptedVolume(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, middleend_encryption_pb2.DeleteEncryptedVolumeRequest)
            res_obj = self.MiddleendEncryptionServicestub.DeleteEncryptedVolume(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.middleend_encryption_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateEncryptedVolume(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, middleend_encryption_pb2.UpdateEncryptedVolumeRequest)
            res_obj = self.MiddleendEncryptionServicestub.UpdateEncryptedVolume(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.middleend_encryption_message.EncryptedVolume().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListEncryptedVolumes(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, middleend_encryption_pb2.ListEncryptedVolumesRequest)
            res_obj = self.MiddleendEncryptionServicestub.ListEncryptedVolumes(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.middleend_encryption_message.ListEncryptedVolumesResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetEncryptedVolume(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, middleend_encryption_pb2.GetEncryptedVolumeRequest)
            res_obj = self.MiddleendEncryptionServicestub.GetEncryptedVolume(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.middleend_encryption_message.EncryptedVolume().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def StatsEncryptedVolume(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, middleend_encryption_pb2.StatsEncryptedVolumeRequest)
            res_obj = self.MiddleendEncryptionServicestub.StatsEncryptedVolume(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.middleend_encryption_message.StatsEncryptedVolumeResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

class BackendNullAPI(Base):
    def __init__(self, parent):
        super(BackendNullAPI, self).__init__(parent)
        self.NullVolumeServiceStub = backend_null_pb2_grpc.NullVolumeServiceStub(self.channel)

    def CreateNullVolume(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_null_pb2.CreateNullVolumeRequest)
            res_obj = self.NullVolumeServicestub.CreateNullVolume(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_null_message.NullVolume().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteNullVolume(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_null_pb2.DeleteNullVolumeRequest)
            res_obj = self.NullVolumeServicestub.DeleteNullVolume(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_null_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateNullVolume(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_null_pb2.UpdateNullVolumeRequest)
            res_obj = self.NullVolumeServicestub.UpdateNullVolume(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_null_message.NullVolume().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListNullVolumes(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_null_pb2.ListNullVolumesRequest)
            res_obj = self.NullVolumeServicestub.ListNullVolumes(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_null_message.ListNullVolumesResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetNullVolume(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_null_pb2.GetNullVolumeRequest)
            res_obj = self.NullVolumeServicestub.GetNullVolume(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_null_message.NullVolume().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def StatsNullVolume(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_null_pb2.StatsNullVolumeRequest)
            res_obj = self.NullVolumeServicestub.StatsNullVolume(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_null_message.StatsNullVolumeResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

class BackendIscsiAPI(Base):
    def __init__(self, parent):
        super(BackendIscsiAPI, self).__init__(parent)

class BackendAioAPI(Base):
    def __init__(self, parent):
        super(BackendAioAPI, self).__init__(parent)
        self.AioVolumeServiceStub = backend_aio_pb2_grpc.AioVolumeServiceStub(self.channel)

    def CreateAioVolume(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_aio_pb2.CreateAioVolumeRequest)
            res_obj = self.AioVolumeServicestub.CreateAioVolume(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_aio_message.AioVolume().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteAioVolume(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_aio_pb2.DeleteAioVolumeRequest)
            res_obj = self.AioVolumeServicestub.DeleteAioVolume(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_aio_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateAioVolume(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_aio_pb2.UpdateAioVolumeRequest)
            res_obj = self.AioVolumeServicestub.UpdateAioVolume(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_aio_message.AioVolume().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListAioVolumes(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_aio_pb2.ListAioVolumesRequest)
            res_obj = self.AioVolumeServicestub.ListAioVolumes(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_aio_message.ListAioVolumesResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetAioVolume(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_aio_pb2.GetAioVolumeRequest)
            res_obj = self.AioVolumeServicestub.GetAioVolume(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_aio_message.AioVolume().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def StatsAioVolume(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_aio_pb2.StatsAioVolumeRequest)
            res_obj = self.AioVolumeServicestub.StatsAioVolume(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_aio_message.StatsAioVolumeResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

class StorageAPI(Base):
    def __init__(self, parent):
        super(StorageAPI, self).__init__(parent)
