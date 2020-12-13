import os
from src.steg import steg_icmp
from src.steg import sniff_all
from src.packets_generator import gen_udp
import src.test


def main():
    #os.system('python3.8 src/test.py')
    steg_icmp()

if __name__ == '__main__':
    main()