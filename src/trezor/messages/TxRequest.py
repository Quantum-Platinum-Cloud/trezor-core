# Automatically generated by pb2py
import protobuf as p
from micropython import const
from .TxRequestDetailsType import TxRequestDetailsType
from .TxRequestSerializedType import TxRequestSerializedType

class TxRequest(p.MessageType):
    FIELDS = {
        1: ('request_type', p.UVarintType, 0),
        2: ('details', TxRequestDetailsType, 0),
        3: ('serialized', TxRequestSerializedType, 0),
    }
    MESSAGE_WIRE_TYPE = 21
