import sys
from scapy.all import *

def gen_icmp(dst_addr):
    send(IP(dst=dst_addr)/ICMP())

def gen_fuzz(dst_addr):
    send(IP(dst=dst_addr)/fuzz(UDP()/NTP(version=4)), loop=0)

def gen_udp(dst_addr):
    send(IP(dst=dst_addr)/UDP())