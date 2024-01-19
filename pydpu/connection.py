import requests
import json
import grpc
import grpc_tools


class Connection(object):
    """
    This is the base class which maintains all the gRPC connection info
    """
    def __init__(self, ip, port, ca=None, ca_key=None, rca=None):
        self._ip_ = ip
        self._port_ = port
        self._client_certificate_ = ca
        self._client_certificate_key_ = ca_key
        self._root_certificate_ = rca

    @property
    def host(self) -> str:
        return self._ip_ + self._port_

    def insecure_channel(self):
        return grpc.insecure_channel(self.host)

    def secure_channel(self):
        raise NotImplementedError("This method is not implemented yet")

        """
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
        """
