import socket
from helper import *
from ethPacket import Ethernet
from ipv4Packet import IPv4
from udpPacket import UDP
from pcap import Pcap

TAB_1 = '\t - '
TAB_2 = '\t\t - '

DATA_TAB_3 = '\t\t\t   '


def main():
    pcap = Pcap('udpTraffic.pcap')  #creating pcap file to write traffic to
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3)) #creating a raw socket listening to every kind of traffic (ntohs(3))

    while True:
        raw_data, addr = conn.recvfrom(65535)
        ethPack = Ethernet(raw_data)

        # IPv4
        if ethPack.proto == 8:
            ipv4Pack = IPv4(ethPack.data)

            # UDP
            if ipv4Pack.proto == 17:
                udpPack = UDP(ipv4Pack.data)

                # as we are just interested in the DNS related Information i check for the port reserved for DNS traffic
                if (udpPack.src_port == 53) or (udpPack.dest_port == 53):

                    # print well formatted/readable traffic description
                    print('\nEthernet Frame:')
                    print(TAB_1 + 'Destination: {}, Source: {}, Protocol: {}'.format(ethPack.dest_mac, ethPack.src_mac, ethPack.proto))
                    print(TAB_1 + 'IPv4 Packet:')
                    print(TAB_2 + 'Version: {}, Header Length: {}, TTL: {},'.format(ipv4Pack.version, ipv4Pack.header_length, ipv4Pack.ttl))
                    print(TAB_2 + 'Protocol: {}, Source: {}, Target: {}'.format(ipv4Pack.proto, ipv4Pack.src, ipv4Pack.target))

                    print('\n' + TAB_1 + 'UDP Segment:')
                    print(TAB_2 + 'Source Port: {}, Destination Port: {}, Length: {}'.format(udpPack.src_port, udpPack.dest_port, udpPack.size))
                    print(TAB_2 + 'UDP Data:')
                    print(formatLines(DATA_TAB_3, udpPack.data))

                    pcap.write(raw_data)

    pcap.close()


main()