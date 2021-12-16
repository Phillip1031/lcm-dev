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

class Imu(object):
    __slots__ = ["header", "accel", "angular_rate"]

    def __init__(self):
        self.header = LcmGui.Header()
        self.accel = [ 0.0 for dim0 in range(3) ]
        self.angular_rate = [ 0.0 for dim0 in range(3) ]

    def encode(self):
        buf = BytesIO()
        buf.write(Imu._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        assert self.header._get_packed_fingerprint() == LcmGui.Header._get_packed_fingerprint()
        self.header._encode_one(buf)
        buf.write(struct.pack('>3d', *self.accel[:3]))
        buf.write(struct.pack('>3d', *self.angular_rate[:3]))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != Imu._get_packed_fingerprint():
            raise ValueError("Decode error")
        return Imu._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = Imu()
        self.header = LcmGui.Header._decode_one(buf)
        self.accel = struct.unpack('>3d', buf.read(24))
        self.angular_rate = struct.unpack('>3d', buf.read(24))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if Imu in parents: return 0
        newparents = parents + [Imu]
        tmphash = (0xccf297d55d257707+ LcmGui.Header._get_hash_recursive(newparents)) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if Imu._packed_fingerprint is None:
            Imu._packed_fingerprint = struct.pack(">Q", Imu._get_hash_recursive([]))
        return Imu._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)
