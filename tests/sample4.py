# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2024 Keysight Technologies

from ..pydpu.dpu import Dpu

dpu = Dpu("10.36.78.168", 50151)
dpu.create_insecure_channel()

# so IP Sec is present in Security. We call the security class and do the task:

ipsec = dpu.security.Ipsec

# the pb2 message format for request and response:

ipsec_message = ipsec.ipsec_messages

res = ipsec.get_ipsec_version(ipsec_message.IPsecVersionRequest())

# To get the IPsecStatsReq:

res = ipsec.get_ipsec_stats(ipsec_message.IPsecStatsRequest())

# create tunnel 1

connection = ipsec_message.Connection()

connection.name = "tun_1_0_0"

connection.version = "2"

address = [ipsec_message.Addrs(addr="200.0.0.1")]

connection.local_addrs = address

connection.local_addrs.append(ipsec_message.Addrs(addr="200.0.0.1"))

local_auth = ipsec_message.LocalAuth()
local_auth.auth = ipsec_message.AuthType.AUTH_TYPE_PSK
local_auth.id = "200.0.0.1"

connection.local_auth = local_auth

connection.remote_addrs = ([ipsec_message.Addrs(addr="200.0.0.2")],)

remote_auth = ipsec_message.RemoteAuth()
remote_auth.auth = ipsec_message.AuthType.AUTH_TYPE_PSK
remote_auth.id = "200.0.0.2"

connection.remote_auth = remote_auth


child = ipsec_message.Child()

child.name = "tun_1_0_0"
child.esp_proposals = ipsec_message.Proposals()
child.esp_proposals.crypto_alg = (
    [ipsec_message.CryptoAlgorithm.CRYPTO_ALGORITHM_AES128],
)
child.esp_proposals.integ_alg = [ipsec_message.PRFunction.PR_FUNCTION_SHA1]


child.remote_ts = ipsec_message.TrafficSelectors()
child.remote_ts.ts = [ipsec_message.TrafficSelector(cidr="40.0.0.0/24")]

child.local_ts = ipsec_message.TrafficSelectors()
child.local_ts.ts = [ipsec_message.TrafficSelector(cidr="201.0.0.0/24")]

connection.children = [child]

proposals = ipsec_message.Proposals()

proposals.crypto_alg = [ipsec_message.CryptoAlgorithm.CRYPTO_ALGORITHM_AES128]
proposals.integ_alg = [ipsec_message.IntegAlgorithm.INTEG_ALGORITHM_SHA384]
proposals.dhgroups = [ipsec_message.DHGroups.DH_GROUPS_MODP1536]

connection.proposals = proposals

tun_1_0_0 = ipsec.load_ipsec_connections(connection)

# TUNNEL 1_0_1

connection = ipsec_message.Connection()

connection.name = "tun_1_0_1"

connection.version = "2"

address = [ipsec_message.Addrs(addr="200.0.0.1")]
connection.local_addrs = address

address = [ipsec_message.Addrs(addr="200.0.0.3")]
connection.remote_addrs = address

local_auth = ipsec_message.LocalAuth()
local_auth.auth = ipsec_message.AuthType.AUTH_TYPE_PSK
local_auth.id = "200.0.0.1"
connection.local_auth = local_auth

remote_auth = ipsec_message.RemoteAuth()
remote_auth.auth = ipsec_message.AuthType.AUTH_TYPE_PSK
remote_auth.id = "200.0.0.3"
connection.remote_auth = remote_auth

child = ipsec_message.Child()

child.name = "tun_1_0_1"
child.esp_proposals = ipsec_message.Proposals()
child.esp_proposals.crypto_alg = [ipsec_message.CryptoAlgorithm.CRYPTO_ALGORITHM_AES128]
child.esp_proposals.integ_alg = [ipsec_message.PRFunction.PR_FUNCTION_SHA1]

child.remote_ts = ipsec_message.TrafficSelectors()
child.remote_ts.ts = [ipsec_message.TrafficSelector(cidr="40.0.1.0/24")]

child.local_ts = ipsec_message.TrafficSelectors()
child.local_ts.ts = [ipsec_message.TrafficSelector(cidr="201.0.0.0/24")]

connection.children = [child]

proposals = ipsec_message.Proposals()

proposals.crypto_alg = [ipsec_message.CryptoAlgorithm.CRYPTO_ALGORITHM_AES128]
proposals.integ_alg = [ipsec_message.IntegAlgorithm.INTEG_ALGORITHM_SHA384]
proposals.dhgroups = [ipsec_message.DHGroups.DH_GROUPS_MODP1536]

connection.proposals = proposals

tun_1_0_1 = ipsec.load_ipsec_connections(connection)

connection_1 = ipsec.load_ipsec_connections(tun_1_0_0)
connection_2 = ipsec.load_ipsec_connections(tun_1_0_1)

list_conn = ipsec_message.IPsecListConnsRequest(ike="tun_1_0_0")

connections = ipsec.list_ipsec_connections(list_conn)

list_sa = ipsec_message.IPsecListSasRequest()
list_sa.ike = "tun_1_0_0"

sas = ipsec.list_ipsec_sas(list_sa)

list_cert = ipsec_message.IPsecListCertsRequest()

certs = ipsec.list_ipsec_certs(list_cert)
