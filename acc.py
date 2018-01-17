#!/usr/bin/python
import socket
import time
acc_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
acc_socket.bind(("",8086))
time0 = time.time()

def convword(data):
    high = ord(data[0])
    low = ord(data[1])
    val = (high << 8) + low
    if (val >= 0x8000):
        val = -((65535 - val) + 1)
    val /= 16384.0
    return val

while(True):
    data = acc_socket.recv(4096)
    acc = map(convword,[data[0:2],data[2:4],data[4:6]])
    print("%10f %10d %+2.10f %+2.10f %+2.10f"%(time.time()-time0,ord(data[6]),acc[0],acc[1],acc[1]))
