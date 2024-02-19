# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: l2_xpu_infra_mgr.proto
# Protobuf Python Version: 4.25.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import networktypes_pb2 as networktypes__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16l2_xpu_infra_mgr.proto\x12 opi_api.network.evpn_gw.v1alpha1\x1a\x12networktypes.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a google/protobuf/field_mask.proto\x1a\x19google/api/resource.proto\"\xc2\x02\n\rLogicalBridge\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x08R\x04name\x12M\n\x04spec\x18\x02 \x01(\x0b\x32\x33.opi_api.network.evpn_gw.v1alpha1.LogicalBridgeSpecB\x04\xe2\x41\x01\x02R\x04spec\x12S\n\x06status\x18\x03 \x01(\x0b\x32\x35.opi_api.network.evpn_gw.v1alpha1.LogicalBridgeStatusB\x04\xe2\x41\x01\x03R\x06status:s\xea\x41p\n.opi_api.network.evpn_gw.v1alpha1/LogicalBridge\x12\x1flogicalBridges/{logical_bridge}*\x0elogicalBridges2\rlogicalBridge\"\xb4\x01\n\x11LogicalBridgeSpec\x12\x1d\n\x07vlan_id\x18\x01 \x01(\rB\x04\xe2\x41\x01\x02R\x06vlanId\x12\x1b\n\x03vni\x18\x02 \x01(\rB\x04\xe2\x41\x01\x01H\x00R\x03vni\x88\x01\x01\x12[\n\x0evtep_ip_prefix\x18\x03 \x01(\x0b\x32/.opi_api.network.opinetcommon.v1alpha1.IPPrefixB\x04\xe2\x41\x01\x01R\x0cvtepIpPrefixB\x06\n\x04_vni\"l\n\x13LogicalBridgeStatus\x12U\n\x0boper_status\x18\x01 \x01(\x0e\x32..opi_api.network.evpn_gw.v1alpha1.LBOperStatusB\x04\xe2\x41\x01\x03R\noperStatus\"\xac\x01\n\x1a\x43reateLogicalBridgeRequest\x12\x30\n\x11logical_bridge_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x01R\x0flogicalBridgeId\x12\\\n\x0elogical_bridge\x18\x02 \x01(\x0b\x32/.opi_api.network.evpn_gw.v1alpha1.LogicalBridgeB\x04\xe2\x41\x01\x02R\rlogicalBridge\"c\n\x19ListLogicalBridgesRequest\x12!\n\tpage_size\x18\x01 \x01(\x05\x42\x04\xe2\x41\x01\x01R\x08pageSize\x12#\n\npage_token\x18\x02 \x01(\tB\x04\xe2\x41\x01\x01R\tpageToken\"\x9e\x01\n\x1aListLogicalBridgesResponse\x12X\n\x0flogical_bridges\x18\x01 \x03(\x0b\x32/.opi_api.network.evpn_gw.v1alpha1.LogicalBridgeR\x0elogicalBridges\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"f\n\x17GetLogicalBridgeRequest\x12K\n\x04name\x18\x01 \x01(\tB7\xe2\x41\x01\x02\xfa\x41\x30\n.opi_api.network.evpn_gw.v1alpha1/LogicalBridgeR\x04name\"\x94\x01\n\x1a\x44\x65leteLogicalBridgeRequest\x12K\n\x04name\x18\x01 \x01(\tB7\xe2\x41\x01\x02\xfa\x41\x30\n.opi_api.network.evpn_gw.v1alpha1/LogicalBridgeR\x04name\x12)\n\rallow_missing\x18\x02 \x01(\x08\x42\x04\xe2\x41\x01\x01R\x0c\x61llowMissing\"\xe8\x01\n\x1aUpdateLogicalBridgeRequest\x12\\\n\x0elogical_bridge\x18\x01 \x01(\x0b\x32/.opi_api.network.evpn_gw.v1alpha1.LogicalBridgeB\x04\xe2\x41\x01\x02R\rlogicalBridge\x12\x41\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x04\xe2\x41\x01\x01R\nupdateMask\x12)\n\rallow_missing\x18\x03 \x01(\x08\x42\x04\xe2\x41\x01\x01R\x0c\x61llowMissing\"\xaa\x02\n\nBridgePort\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x08R\x04name\x12J\n\x04spec\x18\x02 \x01(\x0b\x32\x30.opi_api.network.evpn_gw.v1alpha1.BridgePortSpecB\x04\xe2\x41\x01\x02R\x04spec\x12P\n\x06status\x18\x03 \x01(\x0b\x32\x32.opi_api.network.evpn_gw.v1alpha1.BridgePortStatusB\x04\xe2\x41\x01\x03R\x06status:d\xea\x41\x61\n+opi_api.network.evpn_gw.v1alpha1/BridgePort\x12\x19\x62ridgePorts/{bridge_port}*\x0b\x62ridgePorts2\nbridgePort\"\xb4\x01\n\x0e\x42ridgePortSpec\x12%\n\x0bmac_address\x18\x01 \x01(\x0c\x42\x04\xe2\x41\x01\x02R\nmacAddress\x12L\n\x05ptype\x18\x02 \x01(\x0e\x32\x30.opi_api.network.evpn_gw.v1alpha1.BridgePortTypeB\x04\xe2\x41\x01\x02R\x05ptype\x12-\n\x0flogical_bridges\x18\x03 \x03(\tB\x04\xe2\x41\x01\x01R\x0elogicalBridges\"i\n\x10\x42ridgePortStatus\x12U\n\x0boper_status\x18\x01 \x01(\x0e\x32..opi_api.network.evpn_gw.v1alpha1.BPOperStatusB\x04\xe2\x41\x01\x03R\noperStatus\"\x9a\x01\n\x17\x43reateBridgePortRequest\x12*\n\x0e\x62ridge_port_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x01R\x0c\x62ridgePortId\x12S\n\x0b\x62ridge_port\x18\x02 \x01(\x0b\x32,.opi_api.network.evpn_gw.v1alpha1.BridgePortB\x04\xe2\x41\x01\x02R\nbridgePort\"`\n\x16ListBridgePortsRequest\x12!\n\tpage_size\x18\x01 \x01(\x05\x42\x04\xe2\x41\x01\x01R\x08pageSize\x12#\n\npage_token\x18\x02 \x01(\tB\x04\xe2\x41\x01\x01R\tpageToken\"\x92\x01\n\x17ListBridgePortsResponse\x12O\n\x0c\x62ridge_ports\x18\x01 \x03(\x0b\x32,.opi_api.network.evpn_gw.v1alpha1.BridgePortR\x0b\x62ridgePorts\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"`\n\x14GetBridgePortRequest\x12H\n\x04name\x18\x01 \x01(\tB4\xe2\x41\x01\x02\xfa\x41-\n+opi_api.network.evpn_gw.v1alpha1/BridgePortR\x04name\"\x8e\x01\n\x17\x44\x65leteBridgePortRequest\x12H\n\x04name\x18\x01 \x01(\tB4\xe2\x41\x01\x02\xfa\x41-\n+opi_api.network.evpn_gw.v1alpha1/BridgePortR\x04name\x12)\n\rallow_missing\x18\x02 \x01(\x08\x42\x04\xe2\x41\x01\x01R\x0c\x61llowMissing\"\xdc\x01\n\x17UpdateBridgePortRequest\x12S\n\x0b\x62ridge_port\x18\x01 \x01(\x0b\x32,.opi_api.network.evpn_gw.v1alpha1.BridgePortB\x04\xe2\x41\x01\x02R\nbridgePort\x12\x41\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x04\xe2\x41\x01\x01R\nupdateMask\x12)\n\rallow_missing\x18\x03 \x01(\x08\x42\x04\xe2\x41\x01\x01R\x0c\x61llowMissing*^\n\x0cLBOperStatus\x12\x1e\n\x1aLB_OPER_STATUS_UNSPECIFIED\x10\x00\x12\x15\n\x11LB_OPER_STATUS_UP\x10\x01\x12\x17\n\x13LB_OPER_STATUS_DOWN\x10\x02*^\n\x0c\x42POperStatus\x12\x1e\n\x1a\x42P_OPER_STATUS_UNSPECIFIED\x10\x00\x12\x15\n\x11\x42P_OPER_STATUS_UP\x10\x01\x12\x17\n\x13\x42P_OPER_STATUS_DOWN\x10\x02*k\n\x0e\x42ridgePortType\x12 \n\x1c\x42RIDGE_PORT_TYPE_UNSPECIFIED\x10\x00\x12\x1b\n\x17\x42RIDGE_PORT_TYPE_ACCESS\x10\x01\x12\x1a\n\x16\x42RIDGE_PORT_TYPE_TRUNK\x10\x02\x32\xc9\x07\n\x14LogicalBridgeService\x12\xd3\x01\n\x13\x43reateLogicalBridge\x12<.opi_api.network.evpn_gw.v1alpha1.CreateLogicalBridgeRequest\x1a/.opi_api.network.evpn_gw.v1alpha1.LogicalBridge\"M\xda\x41 logical_bridge,logical_bridge_id\x82\xd3\xe4\x93\x02$\"\x12/v1/logicalBridges:\x0elogical_bridge\x12\xab\x01\n\x12ListLogicalBridges\x12;.opi_api.network.evpn_gw.v1alpha1.ListLogicalBridgesRequest\x1a<.opi_api.network.evpn_gw.v1alpha1.ListLogicalBridgesResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/v1/logicalBridges\x12\xaa\x01\n\x10GetLogicalBridge\x12\x39.opi_api.network.evpn_gw.v1alpha1.GetLogicalBridgeRequest\x1a/.opi_api.network.evpn_gw.v1alpha1.LogicalBridge\"*\xda\x41\x04name\x82\xd3\xe4\x93\x02\x1d\x12\x1b/v1/{name=logicalBridges/*}\x12\x97\x01\n\x13\x44\x65leteLogicalBridge\x12<.opi_api.network.evpn_gw.v1alpha1.DeleteLogicalBridgeRequest\x1a\x16.google.protobuf.Empty\"*\xda\x41\x04name\x82\xd3\xe4\x93\x02\x1d*\x1b/v1/{name=logicalBridges/*}\x12\xe5\x01\n\x13UpdateLogicalBridge\x12<.opi_api.network.evpn_gw.v1alpha1.UpdateLogicalBridgeRequest\x1a/.opi_api.network.evpn_gw.v1alpha1.LogicalBridge\"_\xda\x41\x1alogical_bridge,update_mask\x82\xd3\xe4\x93\x02<2*/v1/{logical_bridge.name=logicalBridges/*}:\x0elogical_bridge2\xfb\x06\n\x11\x42ridgePortService\x12\xbe\x01\n\x10\x43reateBridgePort\x12\x39.opi_api.network.evpn_gw.v1alpha1.CreateBridgePortRequest\x1a,.opi_api.network.evpn_gw.v1alpha1.BridgePort\"A\xda\x41\x1a\x62ridge_port,bridge_port_id\x82\xd3\xe4\x93\x02\x1e\"\x0f/v1/bridgePorts:\x0b\x62ridge_port\x12\x9f\x01\n\x0fListBridgePorts\x12\x38.opi_api.network.evpn_gw.v1alpha1.ListBridgePortsRequest\x1a\x39.opi_api.network.evpn_gw.v1alpha1.ListBridgePortsResponse\"\x17\x82\xd3\xe4\x93\x02\x11\x12\x0f/v1/bridgePorts\x12\x9e\x01\n\rGetBridgePort\x12\x36.opi_api.network.evpn_gw.v1alpha1.GetBridgePortRequest\x1a,.opi_api.network.evpn_gw.v1alpha1.BridgePort\"\'\xda\x41\x04name\x82\xd3\xe4\x93\x02\x1a\x12\x18/v1/{name=bridgePorts/*}\x12\x8e\x01\n\x10\x44\x65leteBridgePort\x12\x39.opi_api.network.evpn_gw.v1alpha1.DeleteBridgePortRequest\x1a\x16.google.protobuf.Empty\"\'\xda\x41\x04name\x82\xd3\xe4\x93\x02\x1a*\x18/v1/{name=bridgePorts/*}\x12\xd0\x01\n\x10UpdateBridgePort\x12\x39.opi_api.network.evpn_gw.v1alpha1.UpdateBridgePortRequest\x1a,.opi_api.network.evpn_gw.v1alpha1.BridgePort\"S\xda\x41\x17\x62ridge_port,update_mask\x82\xd3\xe4\x93\x02\x33\x32$/v1/{bridge_port.name=bridgePorts/*}:\x0b\x62ridge_portBw\n opi_api.network.evpn_gw.v1alpha1B\x12L2XpuInfraMgrProtoP\x01Z=github.com/opiproject/opi-api/network/evpn-gw/v1alpha1/gen/gob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'l2_xpu_infra_mgr_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n opi_api.network.evpn_gw.v1alpha1B\022L2XpuInfraMgrProtoP\001Z=github.com/opiproject/opi-api/network/evpn-gw/v1alpha1/gen/go'
  _globals['_LOGICALBRIDGE'].fields_by_name['name']._options = None
  _globals['_LOGICALBRIDGE'].fields_by_name['name']._serialized_options = b'\342A\001\010'
  _globals['_LOGICALBRIDGE'].fields_by_name['spec']._options = None
  _globals['_LOGICALBRIDGE'].fields_by_name['spec']._serialized_options = b'\342A\001\002'
  _globals['_LOGICALBRIDGE'].fields_by_name['status']._options = None
  _globals['_LOGICALBRIDGE'].fields_by_name['status']._serialized_options = b'\342A\001\003'
  _globals['_LOGICALBRIDGE']._options = None
  _globals['_LOGICALBRIDGE']._serialized_options = b'\352Ap\n.opi_api.network.evpn_gw.v1alpha1/LogicalBridge\022\037logicalBridges/{logical_bridge}*\016logicalBridges2\rlogicalBridge'
  _globals['_LOGICALBRIDGESPEC'].fields_by_name['vlan_id']._options = None
  _globals['_LOGICALBRIDGESPEC'].fields_by_name['vlan_id']._serialized_options = b'\342A\001\002'
  _globals['_LOGICALBRIDGESPEC'].fields_by_name['vni']._options = None
  _globals['_LOGICALBRIDGESPEC'].fields_by_name['vni']._serialized_options = b'\342A\001\001'
  _globals['_LOGICALBRIDGESPEC'].fields_by_name['vtep_ip_prefix']._options = None
  _globals['_LOGICALBRIDGESPEC'].fields_by_name['vtep_ip_prefix']._serialized_options = b'\342A\001\001'
  _globals['_LOGICALBRIDGESTATUS'].fields_by_name['oper_status']._options = None
  _globals['_LOGICALBRIDGESTATUS'].fields_by_name['oper_status']._serialized_options = b'\342A\001\003'
  _globals['_CREATELOGICALBRIDGEREQUEST'].fields_by_name['logical_bridge_id']._options = None
  _globals['_CREATELOGICALBRIDGEREQUEST'].fields_by_name['logical_bridge_id']._serialized_options = b'\342A\001\001'
  _globals['_CREATELOGICALBRIDGEREQUEST'].fields_by_name['logical_bridge']._options = None
  _globals['_CREATELOGICALBRIDGEREQUEST'].fields_by_name['logical_bridge']._serialized_options = b'\342A\001\002'
  _globals['_LISTLOGICALBRIDGESREQUEST'].fields_by_name['page_size']._options = None
  _globals['_LISTLOGICALBRIDGESREQUEST'].fields_by_name['page_size']._serialized_options = b'\342A\001\001'
  _globals['_LISTLOGICALBRIDGESREQUEST'].fields_by_name['page_token']._options = None
  _globals['_LISTLOGICALBRIDGESREQUEST'].fields_by_name['page_token']._serialized_options = b'\342A\001\001'
  _globals['_GETLOGICALBRIDGEREQUEST'].fields_by_name['name']._options = None
  _globals['_GETLOGICALBRIDGEREQUEST'].fields_by_name['name']._serialized_options = b'\342A\001\002\372A0\n.opi_api.network.evpn_gw.v1alpha1/LogicalBridge'
  _globals['_DELETELOGICALBRIDGEREQUEST'].fields_by_name['name']._options = None
  _globals['_DELETELOGICALBRIDGEREQUEST'].fields_by_name['name']._serialized_options = b'\342A\001\002\372A0\n.opi_api.network.evpn_gw.v1alpha1/LogicalBridge'
  _globals['_DELETELOGICALBRIDGEREQUEST'].fields_by_name['allow_missing']._options = None
  _globals['_DELETELOGICALBRIDGEREQUEST'].fields_by_name['allow_missing']._serialized_options = b'\342A\001\001'
  _globals['_UPDATELOGICALBRIDGEREQUEST'].fields_by_name['logical_bridge']._options = None
  _globals['_UPDATELOGICALBRIDGEREQUEST'].fields_by_name['logical_bridge']._serialized_options = b'\342A\001\002'
  _globals['_UPDATELOGICALBRIDGEREQUEST'].fields_by_name['update_mask']._options = None
  _globals['_UPDATELOGICALBRIDGEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\342A\001\001'
  _globals['_UPDATELOGICALBRIDGEREQUEST'].fields_by_name['allow_missing']._options = None
  _globals['_UPDATELOGICALBRIDGEREQUEST'].fields_by_name['allow_missing']._serialized_options = b'\342A\001\001'
  _globals['_BRIDGEPORT'].fields_by_name['name']._options = None
  _globals['_BRIDGEPORT'].fields_by_name['name']._serialized_options = b'\342A\001\010'
  _globals['_BRIDGEPORT'].fields_by_name['spec']._options = None
  _globals['_BRIDGEPORT'].fields_by_name['spec']._serialized_options = b'\342A\001\002'
  _globals['_BRIDGEPORT'].fields_by_name['status']._options = None
  _globals['_BRIDGEPORT'].fields_by_name['status']._serialized_options = b'\342A\001\003'
  _globals['_BRIDGEPORT']._options = None
  _globals['_BRIDGEPORT']._serialized_options = b'\352Aa\n+opi_api.network.evpn_gw.v1alpha1/BridgePort\022\031bridgePorts/{bridge_port}*\013bridgePorts2\nbridgePort'
  _globals['_BRIDGEPORTSPEC'].fields_by_name['mac_address']._options = None
  _globals['_BRIDGEPORTSPEC'].fields_by_name['mac_address']._serialized_options = b'\342A\001\002'
  _globals['_BRIDGEPORTSPEC'].fields_by_name['ptype']._options = None
  _globals['_BRIDGEPORTSPEC'].fields_by_name['ptype']._serialized_options = b'\342A\001\002'
  _globals['_BRIDGEPORTSPEC'].fields_by_name['logical_bridges']._options = None
  _globals['_BRIDGEPORTSPEC'].fields_by_name['logical_bridges']._serialized_options = b'\342A\001\001'
  _globals['_BRIDGEPORTSTATUS'].fields_by_name['oper_status']._options = None
  _globals['_BRIDGEPORTSTATUS'].fields_by_name['oper_status']._serialized_options = b'\342A\001\003'
  _globals['_CREATEBRIDGEPORTREQUEST'].fields_by_name['bridge_port_id']._options = None
  _globals['_CREATEBRIDGEPORTREQUEST'].fields_by_name['bridge_port_id']._serialized_options = b'\342A\001\001'
  _globals['_CREATEBRIDGEPORTREQUEST'].fields_by_name['bridge_port']._options = None
  _globals['_CREATEBRIDGEPORTREQUEST'].fields_by_name['bridge_port']._serialized_options = b'\342A\001\002'
  _globals['_LISTBRIDGEPORTSREQUEST'].fields_by_name['page_size']._options = None
  _globals['_LISTBRIDGEPORTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\342A\001\001'
  _globals['_LISTBRIDGEPORTSREQUEST'].fields_by_name['page_token']._options = None
  _globals['_LISTBRIDGEPORTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\342A\001\001'
  _globals['_GETBRIDGEPORTREQUEST'].fields_by_name['name']._options = None
  _globals['_GETBRIDGEPORTREQUEST'].fields_by_name['name']._serialized_options = b'\342A\001\002\372A-\n+opi_api.network.evpn_gw.v1alpha1/BridgePort'
  _globals['_DELETEBRIDGEPORTREQUEST'].fields_by_name['name']._options = None
  _globals['_DELETEBRIDGEPORTREQUEST'].fields_by_name['name']._serialized_options = b'\342A\001\002\372A-\n+opi_api.network.evpn_gw.v1alpha1/BridgePort'
  _globals['_DELETEBRIDGEPORTREQUEST'].fields_by_name['allow_missing']._options = None
  _globals['_DELETEBRIDGEPORTREQUEST'].fields_by_name['allow_missing']._serialized_options = b'\342A\001\001'
  _globals['_UPDATEBRIDGEPORTREQUEST'].fields_by_name['bridge_port']._options = None
  _globals['_UPDATEBRIDGEPORTREQUEST'].fields_by_name['bridge_port']._serialized_options = b'\342A\001\002'
  _globals['_UPDATEBRIDGEPORTREQUEST'].fields_by_name['update_mask']._options = None
  _globals['_UPDATEBRIDGEPORTREQUEST'].fields_by_name['update_mask']._serialized_options = b'\342A\001\001'
  _globals['_UPDATEBRIDGEPORTREQUEST'].fields_by_name['allow_missing']._options = None
  _globals['_UPDATEBRIDGEPORTREQUEST'].fields_by_name['allow_missing']._serialized_options = b'\342A\001\001'
  _globals['_LOGICALBRIDGESERVICE'].methods_by_name['CreateLogicalBridge']._options = None
  _globals['_LOGICALBRIDGESERVICE'].methods_by_name['CreateLogicalBridge']._serialized_options = b'\332A logical_bridge,logical_bridge_id\202\323\344\223\002$\"\022/v1/logicalBridges:\016logical_bridge'
  _globals['_LOGICALBRIDGESERVICE'].methods_by_name['ListLogicalBridges']._options = None
  _globals['_LOGICALBRIDGESERVICE'].methods_by_name['ListLogicalBridges']._serialized_options = b'\202\323\344\223\002\024\022\022/v1/logicalBridges'
  _globals['_LOGICALBRIDGESERVICE'].methods_by_name['GetLogicalBridge']._options = None
  _globals['_LOGICALBRIDGESERVICE'].methods_by_name['GetLogicalBridge']._serialized_options = b'\332A\004name\202\323\344\223\002\035\022\033/v1/{name=logicalBridges/*}'
  _globals['_LOGICALBRIDGESERVICE'].methods_by_name['DeleteLogicalBridge']._options = None
  _globals['_LOGICALBRIDGESERVICE'].methods_by_name['DeleteLogicalBridge']._serialized_options = b'\332A\004name\202\323\344\223\002\035*\033/v1/{name=logicalBridges/*}'
  _globals['_LOGICALBRIDGESERVICE'].methods_by_name['UpdateLogicalBridge']._options = None
  _globals['_LOGICALBRIDGESERVICE'].methods_by_name['UpdateLogicalBridge']._serialized_options = b'\332A\032logical_bridge,update_mask\202\323\344\223\002<2*/v1/{logical_bridge.name=logicalBridges/*}:\016logical_bridge'
  _globals['_BRIDGEPORTSERVICE'].methods_by_name['CreateBridgePort']._options = None
  _globals['_BRIDGEPORTSERVICE'].methods_by_name['CreateBridgePort']._serialized_options = b'\332A\032bridge_port,bridge_port_id\202\323\344\223\002\036\"\017/v1/bridgePorts:\013bridge_port'
  _globals['_BRIDGEPORTSERVICE'].methods_by_name['ListBridgePorts']._options = None
  _globals['_BRIDGEPORTSERVICE'].methods_by_name['ListBridgePorts']._serialized_options = b'\202\323\344\223\002\021\022\017/v1/bridgePorts'
  _globals['_BRIDGEPORTSERVICE'].methods_by_name['GetBridgePort']._options = None
  _globals['_BRIDGEPORTSERVICE'].methods_by_name['GetBridgePort']._serialized_options = b'\332A\004name\202\323\344\223\002\032\022\030/v1/{name=bridgePorts/*}'
  _globals['_BRIDGEPORTSERVICE'].methods_by_name['DeleteBridgePort']._options = None
  _globals['_BRIDGEPORTSERVICE'].methods_by_name['DeleteBridgePort']._serialized_options = b'\332A\004name\202\323\344\223\002\032*\030/v1/{name=bridgePorts/*}'
  _globals['_BRIDGEPORTSERVICE'].methods_by_name['UpdateBridgePort']._options = None
  _globals['_BRIDGEPORTSERVICE'].methods_by_name['UpdateBridgePort']._serialized_options = b'\332A\027bridge_port,update_mask\202\323\344\223\00232$/v1/{bridge_port.name=bridgePorts/*}:\013bridge_port'
  _globals['_LBOPERSTATUS']._serialized_start=3264
  _globals['_LBOPERSTATUS']._serialized_end=3358
  _globals['_BPOPERSTATUS']._serialized_start=3360
  _globals['_BPOPERSTATUS']._serialized_end=3454
  _globals['_BRIDGEPORTTYPE']._serialized_start=3456
  _globals['_BRIDGEPORTTYPE']._serialized_end=3563
  _globals['_LOGICALBRIDGE']._serialized_start=259
  _globals['_LOGICALBRIDGE']._serialized_end=581
  _globals['_LOGICALBRIDGESPEC']._serialized_start=584
  _globals['_LOGICALBRIDGESPEC']._serialized_end=764
  _globals['_LOGICALBRIDGESTATUS']._serialized_start=766
  _globals['_LOGICALBRIDGESTATUS']._serialized_end=874
  _globals['_CREATELOGICALBRIDGEREQUEST']._serialized_start=877
  _globals['_CREATELOGICALBRIDGEREQUEST']._serialized_end=1049
  _globals['_LISTLOGICALBRIDGESREQUEST']._serialized_start=1051
  _globals['_LISTLOGICALBRIDGESREQUEST']._serialized_end=1150
  _globals['_LISTLOGICALBRIDGESRESPONSE']._serialized_start=1153
  _globals['_LISTLOGICALBRIDGESRESPONSE']._serialized_end=1311
  _globals['_GETLOGICALBRIDGEREQUEST']._serialized_start=1313
  _globals['_GETLOGICALBRIDGEREQUEST']._serialized_end=1415
  _globals['_DELETELOGICALBRIDGEREQUEST']._serialized_start=1418
  _globals['_DELETELOGICALBRIDGEREQUEST']._serialized_end=1566
  _globals['_UPDATELOGICALBRIDGEREQUEST']._serialized_start=1569
  _globals['_UPDATELOGICALBRIDGEREQUEST']._serialized_end=1801
  _globals['_BRIDGEPORT']._serialized_start=1804
  _globals['_BRIDGEPORT']._serialized_end=2102
  _globals['_BRIDGEPORTSPEC']._serialized_start=2105
  _globals['_BRIDGEPORTSPEC']._serialized_end=2285
  _globals['_BRIDGEPORTSTATUS']._serialized_start=2287
  _globals['_BRIDGEPORTSTATUS']._serialized_end=2392
  _globals['_CREATEBRIDGEPORTREQUEST']._serialized_start=2395
  _globals['_CREATEBRIDGEPORTREQUEST']._serialized_end=2549
  _globals['_LISTBRIDGEPORTSREQUEST']._serialized_start=2551
  _globals['_LISTBRIDGEPORTSREQUEST']._serialized_end=2647
  _globals['_LISTBRIDGEPORTSRESPONSE']._serialized_start=2650
  _globals['_LISTBRIDGEPORTSRESPONSE']._serialized_end=2796
  _globals['_GETBRIDGEPORTREQUEST']._serialized_start=2798
  _globals['_GETBRIDGEPORTREQUEST']._serialized_end=2894
  _globals['_DELETEBRIDGEPORTREQUEST']._serialized_start=2897
  _globals['_DELETEBRIDGEPORTREQUEST']._serialized_end=3039
  _globals['_UPDATEBRIDGEPORTREQUEST']._serialized_start=3042
  _globals['_UPDATEBRIDGEPORTREQUEST']._serialized_end=3262
  _globals['_LOGICALBRIDGESERVICE']._serialized_start=3566
  _globals['_LOGICALBRIDGESERVICE']._serialized_end=4535
  _globals['_BRIDGEPORTSERVICE']._serialized_start=4538
  _globals['_BRIDGEPORTSERVICE']._serialized_end=5429
# @@protoc_insertion_point(module_scope)