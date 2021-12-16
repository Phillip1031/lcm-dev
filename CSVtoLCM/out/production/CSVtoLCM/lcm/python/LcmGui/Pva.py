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

class Pva(object):
    __slots__ = ["header", "latitude", "longitude", "altitude_m", "velocity", "attitude"]

    def __init__(self):
        self.header = LcmGui.Header()
        self.latitude = 0.0
        self.longitude = 0.0
        self.altitude_m = 0.0
        self.velocity = [ 0.0 for dim0 in range(3) ]
        self.attitude = 0.0

    def encode(self):
        buf = BytesIO()
        buf.write(Pva._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        assert self.header._get_packed_fingerprint() == LcmGui.Header._get_packed_fingerprint()
        self.header._encode_one(buf)
        buf.write(struct.pack(">ddd", self.latitude, self.longitude, self.altitude_m))
        buf.write(struct.pack('>3d', *self.velocity[:3]))
        buf.write(struct.pack(">d", self.attitude))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != Pva._get_packed_fingerprint():
            raise ValueError("Decode error")
        return Pva._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = Pva()
        self.header = LcmGui.Header._decode_one(buf)
        self.latitude, self.longitude, self.altitude_m = struct.unpack(">ddd", buf.read(24))
        self.velocity = struct.unpack('>3d', buf.read(24))
        self.attitude = struct.unpack(">d", buf.read(8))[0]
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if Pva in parents: return 0
        newparents = parents + [Pva]
        tmphash = (0x156388e5d77a88e5+ LcmGui.Header._get_hash_recursive(newparents)) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if Pva._packed_fingerprint is None:
            Pva._packed_fingerprint = struct.pack(">Q", Pva._get_hash_recursive([]))
        return Pva._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

