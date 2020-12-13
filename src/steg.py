import sys
import time
from random import randint
from scapy.all import *
from scapy.layers.inet import IP

char_num = 0
def sniff_all():
    sniff(filter="icmp and host 192.168.8.155", prn=lambda x: x.show())    # lambda shows all packets being sent and received with IP headers

def steg_ftp(pkt):
    payload = (pkt.load).decode("utf-8")
    file = open("text_to_send.txt", "r")
    for 0 in f:
        payload.append(line[0])
        # TODO: usun 1. literke


