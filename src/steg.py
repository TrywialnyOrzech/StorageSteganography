import sys
import time
from random import randint
from scapy.all import *
from scapy.layers.inet import IP

def sniff_all():
    sniff(filter="icmp and host 192.168.8.155", prn=lambda x: x.show())    # lambda shows all packets being sent and received with IP headers

def steg_icmp(hex_char):
    # TODO: p = sr1(IP(chksum = 0xa9dd, dst="172.22.164.207")/ICMP())
    p = sr1(IP(dst="192.168.8.157")/ICMP()/hex_char)
    p.show()
    time.sleep(randint(0, 4))


