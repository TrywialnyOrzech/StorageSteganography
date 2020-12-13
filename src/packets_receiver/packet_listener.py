from scapy.all import *


def change(pkt):
    char = (pkt.load).decode("utf-8")

def steg_icmp():
    try:
        sniff(filter="icmp and src 192.168.8.156", prn=change)
    except KeyboardInterrupt:
        print ("\n[*] User Requested Shutdown")
        print ("[*] Exiting...")
        sys.exit(1)

steg_icmp()