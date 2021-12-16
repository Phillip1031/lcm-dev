/* LCM type definition class file
 * This file was automatically generated by lcm-gen
 * DO NOT MODIFY BY HAND!!!!
 */

package LcmGui;
 
import java.io.*;
import java.util.*;
import lcm.lcm.*;
 
public final class Baro implements lcm.lcm.LCMEncodable
{
    public LcmGui.Header header;
    public double altitude_m;
 
    public Baro()
    {
    }
 
    public static final long LCM_FINGERPRINT;
    public static final long LCM_FINGERPRINT_BASE = 0x8a6de31dda01ec49L;
 
    static {
        LCM_FINGERPRINT = _hashRecursive(new ArrayList<Class<?>>());
    }
 
    public static long _hashRecursive(ArrayList<Class<?>> classes)
    {
        if (classes.contains(LcmGui.Baro.class))
            return 0L;
 
        classes.add(LcmGui.Baro.class);
        long hash = LCM_FINGERPRINT_BASE
             + LcmGui.Header._hashRecursive(classes)
            ;
        classes.remove(classes.size() - 1);
        return (hash<<1) + ((hash>>63)&1);
    }
 
    public void encode(DataOutput outs) throws IOException
    {
        outs.writeLong(LCM_FINGERPRINT);
        _encodeRecursive(outs);
    }
 
    public void _encodeRecursive(DataOutput outs) throws IOException
    {
        this.header._encodeRecursive(outs); 
 
        outs.writeDouble(this.altitude_m); 
 
    }
 
    public Baro(byte[] data) throws IOException
    {
        this(new LCMDataInputStream(data));
    }
 
    public Baro(DataInput ins) throws IOException
    {
        if (ins.readLong() != LCM_FINGERPRINT)
            throw new IOException("LCM Decode error: bad fingerprint");
 
        _decodeRecursive(ins);
    }
 
    public static LcmGui.Baro _decodeRecursiveFactory(DataInput ins) throws IOException
    {
        LcmGui.Baro o = new LcmGui.Baro();
        o._decodeRecursive(ins);
        return o;
    }
 
    public void _decodeRecursive(DataInput ins) throws IOException
    {
        this.header = LcmGui.Header._decodeRecursiveFactory(ins);
 
        this.altitude_m = ins.readDouble();
 
    }
 
    public LcmGui.Baro copy()
    {
        LcmGui.Baro outobj = new LcmGui.Baro();
        outobj.header = this.header.copy();
 
        outobj.altitude_m = this.altitude_m;
 
        return outobj;
    }
 
}

