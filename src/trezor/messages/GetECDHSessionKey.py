# Automatically generated by pb2py
import protobuf as p
from micropython import const
from .IdentityType import IdentityType

class GetECDHSessionKey(p.MessageType):
    FIELDS = {
        1: ('identity', IdentityType, 0),
        2: ('peer_public_key', p.BytesType, 0),
        3: ('ecdsa_curve_name', p.UnicodeType, 0),
    }
    MESSAGE_WIRE_TYPE = 61
