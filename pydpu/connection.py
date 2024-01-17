import requests
import json
import grpc
import grpc_tools


class Connection(object):
    """
    This is the base class which maintains all the gRPC connection info
    """

    def __init__(self, ip, port, ca, ca_key, rca):
        self._ip = ip
        self._port = port
        self._client_certificate = ca
        self._client_certificate_key = ca_key
        self._root_certificate = rca
        self._channel = None

    @property
    def host(self) -> str:
        return self._host

    @property
    def channel(self) -> str:
        if self._channel is None:
            self._channel = self.connect_grpc()
        else:
            return self._channel

    def connect_grpc(self):

        credentials = grpc.ssl_channel_credentials(
            root_certificates=self._root_certificate,
            certificate_chain=self._client_certificate,
            private_key=self._client_certificate_key,
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
