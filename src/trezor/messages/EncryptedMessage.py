# Automatically generated by pb2py
import protobuf as p
from micropython import const

class EncryptedMessage(p.MessageType):
    FIELDS = {
        1: ('nonce', p.BytesType, 0),
        2: ('message', p.BytesType, 0),
        3: ('hmac', p.BytesType, 0),
    }
    MESSAGE_WIRE_TYPE = 50
