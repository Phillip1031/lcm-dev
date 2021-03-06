"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

import LcmGui.Header

class Baro(object):
    __slots__ = ["header", "altitude_m"]

    def __init__(self):
        self.header = LcmGui.Header()
        self.altitude_m = 0.0

    def encode(self):
        buf = BytesIO()
        buf.write(Baro._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        assert self.header._get_packed_fingerprint() == LcmGui.Header._get_packed_fingerprint()
        self.header._encode_one(buf)
        buf.write(struct.pack(">d", self.altitude_m))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != Baro._get_packed_fingerprint():
            raise ValueError("Decode error")
        return Baro._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = Baro()
        self.header = LcmGui.Header._decode_one(buf)
        self.altitude_m = struct.unpack(">d", buf.read(8))[0]
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if Baro in parents: return 0
        newparents = parents + [Baro]
        tmphash = (0x8a6de31dda01ec49+ LcmGui.Header._get_hash_recursive(newparents)) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if Baro._packed_fingerprint is None:
            Baro._packed_fingerprint = struct.pack(">Q", Baro._get_hash_recursive([]))
        return Baro._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

