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

    @property
    def frontend_virtio_fs_messages(self):
        return frontend_virtio_fs_messages

    @property
    def frontend_virtio_fs_pb2(self):
        return frontend_virtio_fs_pb2

class MiddleendQosVolumeAPI(Base):
    def __init__(self, parent):
        super(MiddleendQosVolumeAPI, self).__init__(parent)
        self.MiddleendQosVolumeServiceStub = middleend_qos_volume_pb2_grpc.MiddleendQosVolumeServiceStub(self.channel)

    @property
    def middleend_qos_volume_messages(self):
        return middleend_qos_volume_messages

    @property
    def middleend_qos_volume_pb2(self):
        return middleend_qos_volume_pb2

    def CreateQosVolume(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, middleend_qos_volume_pb2.CreateQosVolumeRequest())
            res_obj = self.MiddleendQosVolumeServiceStub.CreateQosVolume(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.middleend_qos_volume_message.QosVolume().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteQosVolume(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, middleend_qos_volume_pb2.DeleteQosVolumeRequest())
            res_obj = self.MiddleendQosVolumeServiceStub.DeleteQosVolume(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.middleend_qos_volume_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateQosVolume(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, middleend_qos_volume_pb2.UpdateQosVolumeRequest())
            res_obj = self.MiddleendQosVolumeServiceStub.UpdateQosVolume(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.middleend_qos_volume_message.QosVolume().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListQosVolumes(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, middleend_qos_volume_pb2.ListQosVolumesRequest())
            res_obj = self.MiddleendQosVolumeServiceStub.ListQosVolumes(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.middleend_qos_volume_message.ListQosVolumesResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetQosVolume(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, middleend_qos_volume_pb2.GetQosVolumeRequest())
            res_obj = self.MiddleendQosVolumeServiceStub.GetQosVolume(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.middleend_qos_volume_message.QosVolume().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def StatsQosVolume(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, middleend_qos_volume_pb2.StatsQosVolumeRequest())
            res_obj = self.MiddleendQosVolumeServiceStub.StatsQosVolume(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.middleend_qos_volume_message.StatsQosVolumeResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

class BackendNvmeAPI(Base):
    def __init__(self, parent):
        super(BackendNvmeAPI, self).__init__(parent)
        self.NvmeRemoteControllerServiceStub = backend_nvme_pb2_grpc.NvmeRemoteControllerServiceStub(self.channel)

    @property
    def backend_nvme_messages(self):
        return backend_nvme_messages

    @property
    def backend_nvme_pb2(self):
        return backend_nvme_pb2

    def CreateNvmeRemoteController(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_nvme_pb2.CreateNvmeRemoteControllerRequest())
            res_obj = self.NvmeRemoteControllerServiceStub.CreateNvmeRemoteController(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_nvme_message.NvmeRemoteController().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteNvmeRemoteController(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_nvme_pb2.DeleteNvmeRemoteControllerRequest())
            res_obj = self.NvmeRemoteControllerServiceStub.DeleteNvmeRemoteController(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_nvme_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateNvmeRemoteController(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_nvme_pb2.UpdateNvmeRemoteControllerRequest())
            res_obj = self.NvmeRemoteControllerServiceStub.UpdateNvmeRemoteController(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_nvme_message.NvmeRemoteController().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListNvmeRemoteControllers(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_nvme_pb2.ListNvmeRemoteControllersRequest())
            res_obj = self.NvmeRemoteControllerServiceStub.ListNvmeRemoteControllers(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_nvme_message.ListNvmeRemoteControllersResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetNvmeRemoteController(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_nvme_pb2.GetNvmeRemoteControllerRequest())
            res_obj = self.NvmeRemoteControllerServiceStub.GetNvmeRemoteController(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_nvme_message.NvmeRemoteController().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ResetNvmeRemoteController(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_nvme_pb2.ResetNvmeRemoteControllerRequest())
            res_obj = self.NvmeRemoteControllerServiceStub.ResetNvmeRemoteController(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_nvme_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def StatsNvmeRemoteController(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_nvme_pb2.StatsNvmeRemoteControllerRequest())
            res_obj = self.NvmeRemoteControllerServiceStub.StatsNvmeRemoteController(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_nvme_message.StatsNvmeRemoteControllerResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListNvmeRemoteNamespaces(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_nvme_pb2.ListNvmeRemoteNamespacesRequest())
            res_obj = self.NvmeRemoteControllerServiceStub.ListNvmeRemoteNamespaces(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_nvme_message.ListNvmeRemoteNamespacesResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetNvmeRemoteNamespace(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_nvme_pb2.GetNvmeRemoteNamespaceRequest())
            res_obj = self.NvmeRemoteControllerServiceStub.GetNvmeRemoteNamespace(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_nvme_message.NvmeRemoteNamespace().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateNvmePath(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_nvme_pb2.CreateNvmePathRequest())
            res_obj = self.NvmeRemoteControllerServiceStub.CreateNvmePath(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_nvme_message.NvmePath().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteNvmePath(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_nvme_pb2.DeleteNvmePathRequest())
            res_obj = self.NvmeRemoteControllerServiceStub.DeleteNvmePath(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_nvme_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateNvmePath(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_nvme_pb2.UpdateNvmePathRequest())
            res_obj = self.NvmeRemoteControllerServiceStub.UpdateNvmePath(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_nvme_message.NvmePath().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListNvmePaths(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_nvme_pb2.ListNvmePathsRequest())
            res_obj = self.NvmeRemoteControllerServiceStub.ListNvmePaths(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_nvme_message.ListNvmePathsResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetNvmePath(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_nvme_pb2.GetNvmePathRequest())
            res_obj = self.NvmeRemoteControllerServiceStub.GetNvmePath(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_nvme_message.NvmePath().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def StatsNvmePath(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_nvme_pb2.StatsNvmePathRequest())
            res_obj = self.NvmeRemoteControllerServiceStub.StatsNvmePath(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_nvme_message.StatsNvmePathResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

class FrontendVirtioScsiAPI(Base):
    def __init__(self, parent):
        super(FrontendVirtioScsiAPI, self).__init__(parent)
        self.FrontendVirtioScsiServiceStub = frontend_virtio_scsi_pb2_grpc.FrontendVirtioScsiServiceStub(self.channel)

    @property
    def frontend_virtio_scsi_messages(self):
        return frontend_virtio_scsi_messages

    @property
    def frontend_virtio_scsi_pb2(self):
        return frontend_virtio_scsi_pb2

    def CreateVirtioScsiTarget(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_scsi_pb2.CreateVirtioScsiTargetRequest())
            res_obj = self.FrontendVirtioScsiServiceStub.CreateVirtioScsiTarget(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_scsi_message.VirtioScsiTarget().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteVirtioScsiTarget(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_scsi_pb2.DeleteVirtioScsiTargetRequest())
            res_obj = self.FrontendVirtioScsiServiceStub.DeleteVirtioScsiTarget(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_scsi_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateVirtioScsiTarget(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_scsi_pb2.UpdateVirtioScsiTargetRequest())
            res_obj = self.FrontendVirtioScsiServiceStub.UpdateVirtioScsiTarget(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_scsi_message.VirtioScsiTarget().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListVirtioScsiTargets(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_scsi_pb2.ListVirtioScsiTargetsRequest())
            res_obj = self.FrontendVirtioScsiServiceStub.ListVirtioScsiTargets(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_scsi_message.ListVirtioScsiTargetsResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetVirtioScsiTarget(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_scsi_pb2.GetVirtioScsiTargetRequest())
            res_obj = self.FrontendVirtioScsiServiceStub.GetVirtioScsiTarget(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_scsi_message.VirtioScsiTarget().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def StatsVirtioScsiTarget(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_scsi_pb2.StatsVirtioScsiTargetRequest())
            res_obj = self.FrontendVirtioScsiServiceStub.StatsVirtioScsiTarget(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_scsi_message.StatsVirtioScsiTargetResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateVirtioScsiController(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_scsi_pb2.CreateVirtioScsiControllerRequest())
            res_obj = self.FrontendVirtioScsiServiceStub.CreateVirtioScsiController(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_scsi_message.VirtioScsiController().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteVirtioScsiController(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_scsi_pb2.DeleteVirtioScsiControllerRequest())
            res_obj = self.FrontendVirtioScsiServiceStub.DeleteVirtioScsiController(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_scsi_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateVirtioScsiController(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_scsi_pb2.UpdateVirtioScsiControllerRequest())
            res_obj = self.FrontendVirtioScsiServiceStub.UpdateVirtioScsiController(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_scsi_message.VirtioScsiController().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListVirtioScsiControllers(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_scsi_pb2.ListVirtioScsiControllersRequest())
            res_obj = self.FrontendVirtioScsiServiceStub.ListVirtioScsiControllers(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_scsi_message.ListVirtioScsiControllersResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetVirtioScsiController(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_scsi_pb2.GetVirtioScsiControllerRequest())
            res_obj = self.FrontendVirtioScsiServiceStub.GetVirtioScsiController(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_scsi_message.VirtioScsiController().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def StatsVirtioScsiController(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_scsi_pb2.StatsVirtioScsiControllerRequest())
            res_obj = self.FrontendVirtioScsiServiceStub.StatsVirtioScsiController(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_scsi_message.StatsVirtioScsiControllerResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateVirtioScsiLun(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_scsi_pb2.CreateVirtioScsiLunRequest())
            res_obj = self.FrontendVirtioScsiServiceStub.CreateVirtioScsiLun(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_scsi_message.VirtioScsiLun().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteVirtioScsiLun(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_scsi_pb2.DeleteVirtioScsiLunRequest())
            res_obj = self.FrontendVirtioScsiServiceStub.DeleteVirtioScsiLun(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_scsi_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateVirtioScsiLun(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_scsi_pb2.UpdateVirtioScsiLunRequest())
            res_obj = self.FrontendVirtioScsiServiceStub.UpdateVirtioScsiLun(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_scsi_message.VirtioScsiLun().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListVirtioScsiLuns(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_scsi_pb2.ListVirtioScsiLunsRequest())
            res_obj = self.FrontendVirtioScsiServiceStub.ListVirtioScsiLuns(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_scsi_message.ListVirtioScsiLunsResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetVirtioScsiLun(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_scsi_pb2.GetVirtioScsiLunRequest())
            res_obj = self.FrontendVirtioScsiServiceStub.GetVirtioScsiLun(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_scsi_message.VirtioScsiLun().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def StatsVirtioScsiLun(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_scsi_pb2.StatsVirtioScsiLunRequest())
            res_obj = self.FrontendVirtioScsiServiceStub.StatsVirtioScsiLun(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_scsi_message.StatsVirtioScsiLunResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

class FrontendNvmeAPI(Base):
    def __init__(self, parent):
        super(FrontendNvmeAPI, self).__init__(parent)
        self.FrontendNvmeServiceStub = frontend_nvme_pb2_grpc.FrontendNvmeServiceStub(self.channel)

    @property
    def frontend_nvme_messages(self):
        return frontend_nvme_messages

    @property
    def frontend_nvme_pb2(self):
        return frontend_nvme_pb2

    def CreateNvmeSubsystem(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_nvme_pb2.CreateNvmeSubsystemRequest())
            res_obj = self.FrontendNvmeServiceStub.CreateNvmeSubsystem(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_nvme_message.NvmeSubsystem().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteNvmeSubsystem(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_nvme_pb2.DeleteNvmeSubsystemRequest())
            res_obj = self.FrontendNvmeServiceStub.DeleteNvmeSubsystem(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_nvme_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateNvmeSubsystem(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_nvme_pb2.UpdateNvmeSubsystemRequest())
            res_obj = self.FrontendNvmeServiceStub.UpdateNvmeSubsystem(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_nvme_message.NvmeSubsystem().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListNvmeSubsystems(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_nvme_pb2.ListNvmeSubsystemsRequest())
            res_obj = self.FrontendNvmeServiceStub.ListNvmeSubsystems(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_nvme_message.ListNvmeSubsystemsResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetNvmeSubsystem(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_nvme_pb2.GetNvmeSubsystemRequest())
            res_obj = self.FrontendNvmeServiceStub.GetNvmeSubsystem(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_nvme_message.NvmeSubsystem().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def StatsNvmeSubsystem(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_nvme_pb2.StatsNvmeSubsystemRequest())
            res_obj = self.FrontendNvmeServiceStub.StatsNvmeSubsystem(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_nvme_message.StatsNvmeSubsystemResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateNvmeController(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_nvme_pb2.CreateNvmeControllerRequest())
            res_obj = self.FrontendNvmeServiceStub.CreateNvmeController(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_nvme_message.NvmeController().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteNvmeController(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_nvme_pb2.DeleteNvmeControllerRequest())
            res_obj = self.FrontendNvmeServiceStub.DeleteNvmeController(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_nvme_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateNvmeController(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_nvme_pb2.UpdateNvmeControllerRequest())
            res_obj = self.FrontendNvmeServiceStub.UpdateNvmeController(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_nvme_message.NvmeController().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListNvmeControllers(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_nvme_pb2.ListNvmeControllersRequest())
            res_obj = self.FrontendNvmeServiceStub.ListNvmeControllers(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_nvme_message.ListNvmeControllersResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetNvmeController(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_nvme_pb2.GetNvmeControllerRequest())
            res_obj = self.FrontendNvmeServiceStub.GetNvmeController(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_nvme_message.NvmeController().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def StatsNvmeController(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_nvme_pb2.StatsNvmeControllerRequest())
            res_obj = self.FrontendNvmeServiceStub.StatsNvmeController(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_nvme_message.StatsNvmeControllerResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def CreateNvmeNamespace(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_nvme_pb2.CreateNvmeNamespaceRequest())
            res_obj = self.FrontendNvmeServiceStub.CreateNvmeNamespace(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_nvme_message.NvmeNamespace().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteNvmeNamespace(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_nvme_pb2.DeleteNvmeNamespaceRequest())
            res_obj = self.FrontendNvmeServiceStub.DeleteNvmeNamespace(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_nvme_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateNvmeNamespace(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_nvme_pb2.UpdateNvmeNamespaceRequest())
            res_obj = self.FrontendNvmeServiceStub.UpdateNvmeNamespace(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_nvme_message.NvmeNamespace().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListNvmeNamespaces(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_nvme_pb2.ListNvmeNamespacesRequest())
            res_obj = self.FrontendNvmeServiceStub.ListNvmeNamespaces(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_nvme_message.ListNvmeNamespacesResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetNvmeNamespace(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_nvme_pb2.GetNvmeNamespaceRequest())
            res_obj = self.FrontendNvmeServiceStub.GetNvmeNamespace(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_nvme_message.NvmeNamespace().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def StatsNvmeNamespace(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_nvme_pb2.StatsNvmeNamespaceRequest())
            res_obj = self.FrontendNvmeServiceStub.StatsNvmeNamespace(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_nvme_message.StatsNvmeNamespaceResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

class FrontendVirtioBlkAPI(Base):
    def __init__(self, parent):
        super(FrontendVirtioBlkAPI, self).__init__(parent)
        self.FrontendVirtioBlkServiceStub = frontend_virtio_blk_pb2_grpc.FrontendVirtioBlkServiceStub(self.channel)

    @property
    def frontend_virtio_blk_messages(self):
        return frontend_virtio_blk_messages

    @property
    def frontend_virtio_blk_pb2(self):
        return frontend_virtio_blk_pb2

    def CreateVirtioBlk(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_blk_pb2.CreateVirtioBlkRequest())
            res_obj = self.FrontendVirtioBlkServiceStub.CreateVirtioBlk(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_blk_message.VirtioBlk().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteVirtioBlk(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_blk_pb2.DeleteVirtioBlkRequest())
            res_obj = self.FrontendVirtioBlkServiceStub.DeleteVirtioBlk(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_blk_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateVirtioBlk(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_blk_pb2.UpdateVirtioBlkRequest())
            res_obj = self.FrontendVirtioBlkServiceStub.UpdateVirtioBlk(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_blk_message.VirtioBlk().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListVirtioBlks(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_blk_pb2.ListVirtioBlksRequest())
            res_obj = self.FrontendVirtioBlkServiceStub.ListVirtioBlks(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_blk_message.ListVirtioBlksResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetVirtioBlk(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_blk_pb2.GetVirtioBlkRequest())
            res_obj = self.FrontendVirtioBlkServiceStub.GetVirtioBlk(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_blk_message.VirtioBlk().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def StatsVirtioBlk(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, frontend_virtio_blk_pb2.StatsVirtioBlkRequest())
            res_obj = self.FrontendVirtioBlkServiceStub.StatsVirtioBlk(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.frontend_virtio_blk_message.StatsVirtioBlkResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

class OpicommonAPI(Base):
    def __init__(self, parent):
        super(OpicommonAPI, self).__init__(parent)

    @property
    def opicommon_messages(self):
        return opicommon_messages

    @property
    def opicommon_pb2(self):
        return opicommon_pb2

class MiddleendEncryptionAPI(Base):
    def __init__(self, parent):
        super(MiddleendEncryptionAPI, self).__init__(parent)
        self.MiddleendEncryptionServiceStub = middleend_encryption_pb2_grpc.MiddleendEncryptionServiceStub(self.channel)

    @property
    def middleend_encryption_messages(self):
        return middleend_encryption_messages

    @property
    def middleend_encryption_pb2(self):
        return middleend_encryption_pb2

    def CreateEncryptedVolume(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, middleend_encryption_pb2.CreateEncryptedVolumeRequest())
            res_obj = self.MiddleendEncryptionServiceStub.CreateEncryptedVolume(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.middleend_encryption_message.EncryptedVolume().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteEncryptedVolume(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, middleend_encryption_pb2.DeleteEncryptedVolumeRequest())
            res_obj = self.MiddleendEncryptionServiceStub.DeleteEncryptedVolume(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.middleend_encryption_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateEncryptedVolume(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, middleend_encryption_pb2.UpdateEncryptedVolumeRequest())
            res_obj = self.MiddleendEncryptionServiceStub.UpdateEncryptedVolume(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.middleend_encryption_message.EncryptedVolume().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListEncryptedVolumes(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, middleend_encryption_pb2.ListEncryptedVolumesRequest())
            res_obj = self.MiddleendEncryptionServiceStub.ListEncryptedVolumes(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.middleend_encryption_message.ListEncryptedVolumesResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetEncryptedVolume(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, middleend_encryption_pb2.GetEncryptedVolumeRequest())
            res_obj = self.MiddleendEncryptionServiceStub.GetEncryptedVolume(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.middleend_encryption_message.EncryptedVolume().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def StatsEncryptedVolume(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, middleend_encryption_pb2.StatsEncryptedVolumeRequest())
            res_obj = self.MiddleendEncryptionServiceStub.StatsEncryptedVolume(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.middleend_encryption_message.StatsEncryptedVolumeResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

class BackendNullAPI(Base):
    def __init__(self, parent):
        super(BackendNullAPI, self).__init__(parent)
        self.NullVolumeServiceStub = backend_null_pb2_grpc.NullVolumeServiceStub(self.channel)

    @property
    def backend_null_messages(self):
        return backend_null_messages

    @property
    def backend_null_pb2(self):
        return backend_null_pb2

    def CreateNullVolume(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_null_pb2.CreateNullVolumeRequest())
            res_obj = self.NullVolumeServiceStub.CreateNullVolume(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_null_message.NullVolume().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteNullVolume(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_null_pb2.DeleteNullVolumeRequest())
            res_obj = self.NullVolumeServiceStub.DeleteNullVolume(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_null_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateNullVolume(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_null_pb2.UpdateNullVolumeRequest())
            res_obj = self.NullVolumeServiceStub.UpdateNullVolume(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_null_message.NullVolume().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListNullVolumes(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_null_pb2.ListNullVolumesRequest())
            res_obj = self.NullVolumeServiceStub.ListNullVolumes(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_null_message.ListNullVolumesResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetNullVolume(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_null_pb2.GetNullVolumeRequest())
            res_obj = self.NullVolumeServiceStub.GetNullVolume(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_null_message.NullVolume().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def StatsNullVolume(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_null_pb2.StatsNullVolumeRequest())
            res_obj = self.NullVolumeServiceStub.StatsNullVolume(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_null_message.StatsNullVolumeResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

class BackendIscsiAPI(Base):
    def __init__(self, parent):
        super(BackendIscsiAPI, self).__init__(parent)

    @property
    def backend_iscsi_messages(self):
        return backend_iscsi_messages

    @property
    def backend_iscsi_pb2(self):
        return backend_iscsi_pb2

class BackendAioAPI(Base):
    def __init__(self, parent):
        super(BackendAioAPI, self).__init__(parent)
        self.AioVolumeServiceStub = backend_aio_pb2_grpc.AioVolumeServiceStub(self.channel)

    @property
    def backend_aio_messages(self):
        return backend_aio_messages

    @property
    def backend_aio_pb2(self):
        return backend_aio_pb2

    def CreateAioVolume(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_aio_pb2.CreateAioVolumeRequest())
            res_obj = self.AioVolumeServiceStub.CreateAioVolume(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_aio_message.AioVolume().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def DeleteAioVolume(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_aio_pb2.DeleteAioVolumeRequest())
            res_obj = self.AioVolumeServiceStub.DeleteAioVolume(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_aio_message.google.protobuf.Empty().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def UpdateAioVolume(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_aio_pb2.UpdateAioVolumeRequest())
            res_obj = self.AioVolumeServiceStub.UpdateAioVolume(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_aio_message.AioVolume().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def ListAioVolumes(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_aio_pb2.ListAioVolumesRequest())
            res_obj = self.AioVolumeServiceStub.ListAioVolumes(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_aio_message.ListAioVolumesResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def GetAioVolume(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_aio_pb2.GetAioVolumeRequest())
            res_obj = self.AioVolumeServiceStub.GetAioVolume(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_aio_message.AioVolume().deserialize(response)
        except grpc.RpcError as e:
            print(e)

    def StatsAioVolume(self, request):
        try:
            request = json.dumps(request)
            req_obj = json_format.Parse(request, backend_aio_pb2.StatsAioVolumeRequest())
            res_obj = self.AioVolumeServiceStub.StatsAioVolume(request=req_obj)
            response = json_format.MessageToDict(res_obj, preserving_proto_field_name=True)
            if response is not None:
                return self.backend_aio_message.StatsAioVolumeResponse().deserialize(response)
        except grpc.RpcError as e:
            print(e)

class StorageAPI(Base):
    def __init__(self, parent):
        super(StorageAPI, self).__init__(parent)

    @property
    def FrontendVirtioFs(self) -> FrontendVirtioFsAPI:
        if self._FrontendVirtioFs_api_ is None:
            self._FrontendVirtioFs_ = FrontendVirtioFsAPI(self)
        return self._FrontendVirtioFs_

    @property
    def MiddleendQosVolume(self) -> MiddleendQosVolumeAPI:
        if self._MiddleendQosVolume_api_ is None:
            self._MiddleendQosVolume_ = MiddleendQosVolumeAPI(self)
        return self._MiddleendQosVolume_

    @property
    def BackendNvme(self) -> BackendNvmeAPI:
        if self._BackendNvme_api_ is None:
            self._BackendNvme_ = BackendNvmeAPI(self)
        return self._BackendNvme_

    @property
    def FrontendVirtioScsi(self) -> FrontendVirtioScsiAPI:
        if self._FrontendVirtioScsi_api_ is None:
            self._FrontendVirtioScsi_ = FrontendVirtioScsiAPI(self)
        return self._FrontendVirtioScsi_

    @property
    def FrontendNvme(self) -> FrontendNvmeAPI:
        if self._FrontendNvme_api_ is None:
            self._FrontendNvme_ = FrontendNvmeAPI(self)
        return self._FrontendNvme_

    @property
    def FrontendVirtioBlk(self) -> FrontendVirtioBlkAPI:
        if self._FrontendVirtioBlk_api_ is None:
            self._FrontendVirtioBlk_ = FrontendVirtioBlkAPI(self)
        return self._FrontendVirtioBlk_

    @property
    def Opicommon(self) -> OpicommonAPI:
        if self._Opicommon_api_ is None:
            self._Opicommon_ = OpicommonAPI(self)
        return self._Opicommon_

    @property
    def MiddleendEncryption(self) -> MiddleendEncryptionAPI:
        if self._MiddleendEncryption_api_ is None:
            self._MiddleendEncryption_ = MiddleendEncryptionAPI(self)
        return self._MiddleendEncryption_

    @property
    def BackendNull(self) -> BackendNullAPI:
        if self._BackendNull_api_ is None:
            self._BackendNull_ = BackendNullAPI(self)
        return self._BackendNull_

    @property
    def BackendIscsi(self) -> BackendIscsiAPI:
        if self._BackendIscsi_api_ is None:
            self._BackendIscsi_ = BackendIscsiAPI(self)
        return self._BackendIscsi_

    @property
    def BackendAio(self) -> BackendAioAPI:
        if self._BackendAio_api_ is None:
            self._BackendAio_ = BackendAioAPI(self)
        return self._BackendAio_
