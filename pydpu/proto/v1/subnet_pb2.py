# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: subnet.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import networktypes_pb2 as networktypes__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0csubnet.proto\x12\x1eopi_api.network.cloud.v1alpha1\x1a\x12networktypes.proto\x1a\x19google/api/resource.proto\"\xcc\x01\n\x06Subnet\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x38\n\x04spec\x18\x02 \x01(\x0b\x32*.opi_api.network.cloud.v1alpha1.SubnetSpec\x12<\n\x06status\x18\x03 \x01(\x0b\x32,.opi_api.network.cloud.v1alpha1.SubnetStatus:<\xea\x41\x39\n%opi_api.network.cloud.v1alpha1/subnet\x12\x10subnets/{subnet}\"\xb4\x06\n\nSubnetSpec\x12\x14\n\x0cvpc_name_ref\x18\x01 \x01(\t\x12\x44\n\tv4_prefix\x18\x02 \x01(\x0b\x32\x31.opi_api.network.opinetcommon.v1alpha1.IPv4Prefix\x12\x44\n\tv6_prefix\x18\x03 \x01(\x0b\x32\x31.opi_api.network.opinetcommon.v1alpha1.IPv6Prefix\x12\x1e\n\x16ipv4_virtual_router_ip\x18\x04 \x01(\r\x12\x1e\n\x16ipv6_virtual_router_ip\x18\x05 \x01(\x0c\x12\x1a\n\x12virtual_router_mac\x18\x06 \x01(\x0c\x12\x1f\n\x17v4_route_table_name_ref\x18\x07 \x01(\t\x12\x1f\n\x17v6_route_table_name_ref\x18\x08 \x01(\t\x12*\n\"ingess_v4_security_policy_name_ref\x18\t \x03(\t\x12+\n#ingress_v6_security_policy_name_ref\x18\n \x03(\t\x12*\n\"egress_v4_security_policy_name_ref\x18\x0b \x03(\t\x12*\n\"egress_v6_security_policy_name_ref\x18\x0c \x03(\t\x12\x42\n\x0c\x61\x63\x63\x65ss_encap\x18\r \x01(\x0b\x32,.opi_api.network.opinetcommon.v1alpha1.Encap\x12\x42\n\x0c\x66\x61\x62ric_encap\x18\x0e \x01(\x0b\x32,.opi_api.network.opinetcommon.v1alpha1.Encap\x12\x1f\n\x17host_interface_name_ref\x18\x0f \x03(\t\x12\x0b\n\x03tos\x18\x10 \x01(\x05\x12\x11\n\tconnected\x18\x11 \x01(\x08\x12*\n\"ingress_default_sg_policy_name_ref\x18\x12 \x01(\t\x12)\n!egress_default_sg_policy_name_ref\x18\x13 \x01(\t\x12\x15\n\rremote_subnet\x18\x14 \x01(\x08\"4\n\x0cSubnetStatus\x12\x10\n\x08hw_index\x18\x01 \x01(\x05\x12\x12\n\nvnic_count\x18\x02 \x01(\x05\x42l\n\x1eopi_api.network.cloud.v1alpha1B\x0bSubnetProtoP\x01Z;github.com/opiproject/opi-api/network/cloud/v1alpha1/gen/gob\x06proto3')



_SUBNET = DESCRIPTOR.message_types_by_name['Subnet']
_SUBNETSPEC = DESCRIPTOR.message_types_by_name['SubnetSpec']
_SUBNETSTATUS = DESCRIPTOR.message_types_by_name['SubnetStatus']
Subnet = _reflection.GeneratedProtocolMessageType('Subnet', (_message.Message,), {
  'DESCRIPTOR' : _SUBNET,
  '__module__' : 'subnet_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.network.cloud.v1alpha1.Subnet)
  })
_sym_db.RegisterMessage(Subnet)

SubnetSpec = _reflection.GeneratedProtocolMessageType('SubnetSpec', (_message.Message,), {
  'DESCRIPTOR' : _SUBNETSPEC,
  '__module__' : 'subnet_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.network.cloud.v1alpha1.SubnetSpec)
  })
_sym_db.RegisterMessage(SubnetSpec)

SubnetStatus = _reflection.GeneratedProtocolMessageType('SubnetStatus', (_message.Message,), {
  'DESCRIPTOR' : _SUBNETSTATUS,
  '__module__' : 'subnet_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.network.cloud.v1alpha1.SubnetStatus)
  })
_sym_db.RegisterMessage(SubnetStatus)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\036opi_api.network.cloud.v1alpha1B\013SubnetProtoP\001Z;github.com/opiproject/opi-api/network/cloud/v1alpha1/gen/go'
  _SUBNET._options = None
  _SUBNET._serialized_options = b'\352A9\n%opi_api.network.cloud.v1alpha1/subnet\022\020subnets/{subnet}'
  _SUBNET._serialized_start=96
  _SUBNET._serialized_end=300
  _SUBNETSPEC._serialized_start=303
  _SUBNETSPEC._serialized_end=1123
  _SUBNETSTATUS._serialized_start=1125
  _SUBNETSTATUS._serialized_end=1177
# @@protoc_insertion_point(module_scope)