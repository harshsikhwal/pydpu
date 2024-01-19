# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2022 Dell Inc, or its subsidiaries.

from pydpu.dpu import Dpu

import grpc

dpu = Dpu()
dpu.connect_grpc_insecure_channel("10.36.78.168", "50151")

# so IP Sec is present in Security. We call the security class and do the task:

ipsec = dpu.security.ipsec

# the pb2 message format for request and response:

ipsec_message = dpu.security.ipsec.ipsec_message

ipsec.get_ipsec_version(ipsec_message.IPsecVersionReq())

# To get the IPsecStatsReq:

ipsec.get_ipsec_stats(ipsec_message.IPsecStatsReq())

# create tunnel 1

tun1_0_0 = ipsec_message.IPsecLoadConnReq(
    connection=ipsec_message.Connection(
        name='tun1_0_0',
        version='2',
        local_addrs=[ipsec_message.Addrs(addr='200.0.0.1')],
        remote_addrs=[ipsec_message.Addrs(addr='200.0.0.2')],
        local_auth=ipsec_message.LocalAuth(
            auth=ipsec_message.PSK,
            id='200.0.0.1'
        ),
        remote_auth=ipsec_message.RemoteAuth(
            auth=ipsec_message.PSK,
            id='200.0.0.2'
        ),
        children=[ipsec_message.Child(
            name='tun1_0_0',
            esp_proposals=ipsec_message.Proposals(
                crypto_alg=[ipsec_message.AES128],
                integ_alg=[ipsec_message.SHA1]
            ),
            remote_ts=ipsec_message.TrafficSelectors(
                ts=[ipsec_message.TrafficSelectors.TrafficSelector(
                    cidr='40.0.0.0/24'
                )]
            ),
            local_ts=ipsec_message.TrafficSelectors(
                ts=[ipsec_message.TrafficSelectors.TrafficSelector(
                    cidr='201.0.0.0/24'
                )]
            ),
        )],
        proposals=ipsec_message.Proposals(
            crypto_alg=[ipsec_message.AES128],
            integ_alg=[ipsec_message.SHA384],
            dhgroups=[ipsec_message.MODP1536]
        )
    )
)

tun1_0_1 = ipsec_message.IPsecLoadConnReq(
    connection=ipsec_message.Connection(
        name='tun1_0_1',
        version='2',
        local_addrs=[ipsec_message.Addrs(addr='200.0.0.1')],
        remote_addrs=[ipsec_message.Addrs(addr='200.0.0.3')],
        local_auth=ipsec_message.LocalAuth(
            auth=ipsec_message.PSK,
            id='200.0.0.1'
        ),
        remote_auth=ipsec_message.RemoteAuth(
            auth=ipsec_message.PSK,
            id='200.0.0.3'
        ),
        children=[ipsec_message.Child(
            name='tun1_0_1',
            esp_proposals=ipsec_message.Proposals(
                crypto_alg=[ipsec_message.AES128],
                integ_alg=[ipsec_message.SHA1]
            ),
            remote_ts=ipsec_message.TrafficSelectors(
                ts=[ipsec_message.TrafficSelectors.TrafficSelector(
                    cidr='40.0.1.0/24'
                )]
            ),
            local_ts=ipsec_message.TrafficSelectors(
                ts=[ipsec_message.TrafficSelectors.TrafficSelector(
                    cidr='201.0.0.0/24'
                )]
            ),
        )],
        proposals=ipsec_message.Proposals(
            crypto_alg=[ipsec_message.AES128],
            integ_alg=[ipsec_message.SHA384],
            dhgroups=[ipsec_message.MODP1536]
        )
    )
)

connection_1 = ipsec.load_ipsec_connection(tun1_0_0)
connection_2 = ipsec.load_ipsec_connection(tun1_0_1)

list_conn = ipsec_message.IPsecListConnsReq(ike='tun1_0_0')

connections = ipsec.list_ipsec_conns(list_conn)

list_sa = ipsec_message.IPsecListSasReq(ike='tun1_0_0')

sas = ipsec.list_ipsec_sas(list_sa)

list_cert = ipsec_message.IPsecListCertsReq()

certs = ipsec.list_ipsec_certs(list_cert)


# init_conn = stub.IPsecInitiate(
#     ipsec_pb2.IPsecInstallReq(ike='tun1_0_0', child='tun1_0_0')
# )


# init_conn = stub.IPsecInitiate(
#     ipsec_pb2.IPsecInitiateReq(ike='tun1_0_0', child='tun1_0_0')
# )
