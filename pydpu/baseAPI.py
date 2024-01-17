
class Base(object):
    """
    This is the base class which includes connection info and all the shared operations across different modules
    """
    __slots__ = (
        "_insecure_channel",
        "_parent",
    )

    def __init__(self, parent):
        self._parent = parent
        if self._parent is not None:
            self._insecure_channel = parent._insecure_channel

    @property
    def parent(self):
        """The parent object of the current object
        Returns
        -------
        - obj: The parent object of the current object or None if there is no parent for this object
        """
        return self._parent

    @property
    def grpc_insecure_channel(self):
        """The grpc insecure channel
        Returns
        -------
        - obj: The grpc insecure channel object
        """
        return self._insecure_channel
