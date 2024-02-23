# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2022 Dell Inc, or its subsidiaries.

import sys
import os
from pydpu.pydpu.dpu import Dpu

dpu = Dpu("10.36.78.168", 50151)
dpu.create_insecure_channel()

# so IP Sec is present in Security. We call the security class and do the task:

ipsec = dpu.security.Ipsec

# the pb2 message format for request and response:

ipsec_message = ipsec.ipsec_messages

res = ipsec.get_ipsec_version(ipsec_message.IPsecVersionReq())

# To get the IPsecStatsReq:

res = ipsec.get_ipsec_stats(ipsec_message.IPsecStatsReq())

# create tunnel 1

tun1_0_0 = ipsec.ipsec_messages.IPsecLoadConnReq(
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

connection_1 = ipsec.IPsecLoadConn(tun1_0_0)
connection_2 = ipsec.IPsecLoadConn(tun1_0_1)

list_conn = ipsec_message.IPsecListConnsReq(ike='tun1_0_0')

connections = ipsec.IPsecListConns(list_conn)

list_sa = ipsec_message.IPsecListSasReq(ike='tun1_0_0')

sas = ipsec.IPsecListSas(list_sa)

list_cert = ipsec_message.IPsecListCertsReq()

certs = ipsec.IPsecListCerts(list_cert)


# init_conn = stub.IPsecInitiate(
#     ipsec_pb2.IPsecInstallReq(ike='tun1_0_0', child='tun1_0_0')
# )


# init_conn = stub.IPsecInitiate(
#     ipsec_pb2.IPsecInitiateReq(ike='tun1_0_0', child='tun1_0_0')
# )
