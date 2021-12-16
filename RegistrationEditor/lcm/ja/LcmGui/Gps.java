/* LCM type definition class file
 * This file was automatically generated by lcm-gen
 * DO NOT MODIFY BY HAND!!!!
 */

package LcmGui;
 
import java.io.*;
import java.util.*;
import lcm.lcm.*;
 
public final class Gps implements lcm.lcm.LCMEncodable
{
    public LcmGui.Header header;
    public double latitude_deg;
    public double longitude_deg;
    public double altitude_m;
 
    public Gps()
    {
    }
 
    public static final long LCM_FINGERPRINT;
    public static final long LCM_FINGERPRINT_BASE = 0x8532dafbe3364312L;
 
    static {
        LCM_FINGERPRINT = _hashRecursive(new ArrayList<Class<?>>());
    }
 
    public static long _hashRecursive(ArrayList<Class<?>> classes)
    {
        if (classes.contains(LcmGui.Gps.class))
            return 0L;
 
        classes.add(LcmGui.Gps.class);
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
 
        outs.writeDouble(this.latitude_deg); 
 
        outs.writeDouble(this.longitude_deg); 
 
        outs.writeDouble(this.altitude_m); 
 
    }
 
    public Gps(byte[] data) throws IOException
    {
        this(new LCMDataInputStream(data));
    }
 
    public Gps(DataInput ins) throws IOException
    {
        if (ins.readLong() != LCM_FINGERPRINT)
            throw new IOException("LCM Decode error: bad fingerprint");
 
        _decodeRecursive(ins);
    }
 
    public static LcmGui.Gps _decodeRecursiveFactory(DataInput ins) throws IOException
    {
        LcmGui.Gps o = new LcmGui.Gps();
        o._decodeRecursive(ins);
        return o;
    }
 
    public void _decodeRecursive(DataInput ins) throws IOException
    {
        this.header = LcmGui.Header._decodeRecursiveFactory(ins);
 
        this.latitude_deg = ins.readDouble();
 
        this.longitude_deg = ins.readDouble();
 
        this.altitude_m = ins.readDouble();
 
    }
 
    public LcmGui.Gps copy()
    {
        LcmGui.Gps outobj = new LcmGui.Gps();
        outobj.header = this.header.copy();
 
        outobj.latitude_deg = this.latitude_deg;
 
        outobj.longitude_deg = this.longitude_deg;
 
        outobj.altitude_m = this.altitude_m;
 
        return outobj;
    }
 
}

