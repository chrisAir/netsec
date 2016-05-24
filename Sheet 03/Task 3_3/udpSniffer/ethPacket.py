import socket
import struct
from helper import *


# This is a class to simulate a ethernet frame
class Ethernet:
    def __init__(self, raw_data):
        dest, src, prototype = struct.unpack('! 6s 6s H', raw_data[:14])

        self.dest_mac = formatMAC(dest)
        self.src_mac = formatMAC(src)
        self.proto = socket.htons(prototype)
        self.data = raw_data[14:]
