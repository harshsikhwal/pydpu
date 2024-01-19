# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2022 Dell Inc, or its subsidiaries.
# Copyright (c) 2024 Keysight Technologies Inc, or its subsidiaries.

import grpc
from ..baseAPI import Base

from ..proto.v1 import uuid_pb2
from ..proto.v1 import uuid_pb2_grpc


class CommonAPI(Base):
    def __init__(self, parent):
        super(CommonAPI, self).__init__(parent)
        # Unimplemented

    @property
    def uuid_message(self):
        """The uuid_message object of the current object
        Returns
        -------
        - uuid_pb2
        """
        return uuid_pb2
