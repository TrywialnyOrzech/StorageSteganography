from scapy.all import *
from steg import steg_ftp

def check_ftp(pkt):
    if pkt.haslayer(TCP) and pkt.haslayer(Raw):
        if pkt[TCP].dport == 21 or pkt[TCP].sport == 21:
            return True
        else:
            return False
    else:
        return False

def prepare(pkt, dst_addr):
    pkt[TCP].dst = dst_addr
    steg_ftp(pkt)
    show2(indent=3, show_summary=True)
    sr1(pkt)  # tutaj czeka na odpowiedz, wiec chyba lepiej zmienic sr1 na send lub sendb
