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

tun1_0_0 = ipsec_message.IPsecLoadConnRequest(
    connection=ipsec_message.Connection(
        name="tun1_0_0",
        version="2",
        local_addrs=[ipsec_message.Addrs(addr="200.0.0.1")],
        remote_addrs=[ipsec_message.Addrs(addr="200.0.0.2")],
        local_auth=ipsec_message.LocalAuth(
            auth=ipsec_message.AuthType.AUTH_TYPE_PSK, id="200.0.0.1"
        ),
        remote_auth=ipsec_message.RemoteAuth(
            auth=ipsec_message.AuthType.AUTH_TYPE_PSK, id="200.0.0.2"
        ),
        children=[
            ipsec_message.Child(
                name="tun1_0_0",
                esp_proposals=ipsec_message.Proposals(
                    crypto_alg=[ipsec_message.CryptoAlgorithm.CRYPTO_ALGORITHM_AES128],
                    integ_alg=[ipsec_message.PRFunction.PR_FUNCTION_SHA1],
                ),
                remote_ts=ipsec_message.TrafficSelectors(
                    ts=[ipsec_message.TrafficSelector(cidr="40.0.0.0/24")]
                ),
                local_ts=ipsec_message.TrafficSelectors(
                    ts=[ipsec_message.TrafficSelector(cidr="201.0.0.0/24")]
                ),
            )
        ],
        proposals=ipsec_message.Proposals(
            crypto_alg=[ipsec_message.CryptoAlgorithm.CRYPTO_ALGORITHM_AES128],
            integ_alg=[ipsec_message.IntegAlgorithm.INTEG_ALGORITHM_SHA384],
            dhgroups=[ipsec_message.DHGroups.DH_GROUPS_MODP1536],
        ),
    )
)

tun_1_0_1 = ipsec_message.IPsecLoadConnRequest(
    connection=ipsec_message.Connection(
        name="tun_1_0_1",
        version="2",
        local_addrs=[ipsec_message.Addrs(addr="200.0.0.1")],
        remote_addrs=[ipsec_message.Addrs(addr="200.0.0.3")],
        local_auth=ipsec_message.LocalAuth(
            auth=ipsec_message.AuthType.AUTH_TYPE_PSK, id="200.0.0.1"
        ),
        remote_auth=ipsec_message.RemoteAuth(
            auth=ipsec_message.AuthType.AUTH_TYPE_PSK, id="200.0.0.3"
        ),
        children=[
            ipsec_message.Child(
                name="tun_1_0_1",
                esp_proposals=ipsec_message.Proposals(
                    crypto_alg=[ipsec_message.CryptoAlgorithm.CRYPTO_ALGORITHM_AES128],
                    integ_alg=[ipsec_message.PRFunction.PR_FUNCTION_SHA1],
                ),
                remote_ts=ipsec_message.TrafficSelectors(
                    ts=[ipsec_message.TrafficSelector(cidr="40.0.1.0/24")]
                ),
                local_ts=ipsec_message.TrafficSelectors(
                    ts=[ipsec_message.TrafficSelector(cidr="201.0.0.0/24")]
                ),
            )
        ],
        proposals=ipsec_message.Proposals(
            crypto_alg=[ipsec_message.CryptoAlgorithm.CRYPTO_ALGORITHM_AES128],
            integ_alg=[ipsec_message.IntegAlgorithm.INTEG_ALGORITHM_SHA384],
            dhgroups=[ipsec_message.DHGroups.DH_GROUPS_MODP1536],
        ),
    )
)


connection_1 = ipsec.load_ipsec_connections(tun1_0_0)
connection_2 = ipsec.load_ipsec_connections(tun_1_0_1)

connections = ipsec.list_ipsec_connections(
    ipsec_message.IPsecListConnsRequest(ike="tun1_0_0")
)

sas = ipsec.list_ipsec_sas(ipsec_message.IPsecListSasRequest(ike="tun1_0_0"))

certs = ipsec.list_ipsec_certs(ipsec_message.IPsecListCertsRequest())
