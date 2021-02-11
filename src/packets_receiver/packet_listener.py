from scapy.all import *


def change(pkt):
    payload = (pkt.load).decode("utf-8")
    index = ord(payload[0]) // 4 + 1

    char = payload[index]
    file = open("decoded_packets.txt", "w+")
    file.write(char)
    file.close()


def steg_icmp():
    try:
        sniff(filter="icmp and src 192.168.1.4", prn=change)
    except KeyboardInterrupt:
        print("\n[*] User Requested Shutdown")
        print("[*] Exiting...")
        sys.exit(1)


while True:
    steg_icmp()
