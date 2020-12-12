import sys
from scapy.all import sr1,IP,ICMP

def icmp():
    p=sr1(IP(dst="192.168.8.1")/ICMP()/"ICMP has been sent.")
    if p:
        p.show()