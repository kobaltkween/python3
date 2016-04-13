"""
wiretimes.py: print the timestamp for each packet in wireshark.bin 
"""
import struct

f = open("./wireshark.bin", "rb")
# Account for the global header
globalHeadSize = int(((16 * 2) + (32 * 5)) / 8)
f.read(globalHeadSize)
packetHeadSize = int(4 * 32 / 8)
packetNum = 1

while True:
    packetHead = f.read(packetHeadSize)
    if not packetHead:
        break
    tsSec, tsUsec, inclLen, orgLen = struct.unpack('=LLLL', packetHead)
    print("Packet {0}: seconds = {1}, microseconds = {2}".format(packetNum, tsSec, tsUsec))
    # Go through the rest of the packet
    packetBody = f.read(inclLen)
    packetNum += 1
    