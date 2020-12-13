import sys
from scapy.all import *
from scapy.layers.inet import IP

def sniff_all():
    sniff(filter="icmp and host 192.168.8.155", prn=lambda x: x.show())    # lambda shows all packets being sent and received with IP headers

def steg_icmp():
    p = sr1(IP(chksum = 0xa9dd, dst="172.22.164.207")/ICMP())
    p.show()


