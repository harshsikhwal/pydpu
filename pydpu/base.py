# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2024 Keysight Technologies Inc, or its subsidiaries.

from connection import Connection
class Base(object):
    """
    This is the base class which includes connection info and all the shared operations across different modules
    """
    __slots__ = (
        "_parent",
        "_connection"
    )

    def __init__(self, parent, ip, port):
        self._parent = parent
        self._ip_ = ip
        self._port_ = port
        if self._parent is not None:
            self._connection = parent._connection
        else:
            self._connection = Connection(ip, port)

    @property
    def parent(self):
        """The parent object of the current object
        Returns
        -------
        - obj: The parent object of the current object or None if there is no parent for this object
        """
        return self._parent

    @property
    def channel(self):
        """The grpc insecure channel
        Returns
        -------
        - obj: The grpc insecure channel object
        """
        return self._connection._channel
