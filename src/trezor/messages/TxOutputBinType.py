# Automatically generated by pb2py
import protobuf as p
from micropython import const

class TxOutputBinType(p.MessageType):
    FIELDS = {
        1: ('amount', p.UVarintType, 0), # required
        2: ('script_pubkey', p.BytesType, 0), # required
    }
