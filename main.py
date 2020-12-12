import os
from src.send_icmp import icmp
from src.sniff import sniff
from src.packets_generator import gen_udp
import src.test


def main():
    #os.system('python3.8 src/test.py')
    gen_udp("192.168.8.1")

if __name__ == '__main__':
    main()