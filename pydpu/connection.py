# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2024 Keysight Technologies Inc, or its subsidiaries.

import grpc

class Connection(object):
    """
    This is the base class which maintains all the gRPC connection info
    """ 
    __slots__ = (
        "_channel",
    )
    
    def __init__(self, ip, port):
        self._ip_ = ip
        self._port_ = port
        self._channel = None

    @property
    def host(self) -> str:
        return self._ip_ + self._port_

    def insecure_channel(self):
        self._channel = grpc.insecure_channel(self.host)

    def secure_channel(self, root_certificates, client_certificate, client_certificate_key):
        credentials = grpc.ssl_channel_credentials(
            root_certificates=root_certificates,
            certificate_chain=client_certificate,
            private_key=client_certificate_key,
        )
        CHANNEL_OPTIONS = [
            ("grpc.enable_retries", 0),
            ("grpc.keepalive_timeout_ms", 10),
        ]
        channel = grpc.secure_channel(
            self._ip + ":" + self._port, credentials, options=CHANNEL_OPTIONS
        )
        try:
            grpc.channel_ready_future(channel).result(timeout=5)
            print(f"Successfully established secure channel to {self._ip}")
        except:
            print(f"Timeout. Failed to establish secure channel to {self._ip}")
        return channel
        
