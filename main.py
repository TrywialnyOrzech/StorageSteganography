import os
import pandas as pd
from src.steg import steg_icmp
from src.steg import sniff_all
from src.packets_generator import gen_udp
import src.test


def main():
    hex_str = 'a'
    file = open("text_to_send.txt", "r")
    for line in file:
        for character in line:
            hex_char = format(ord(character), "x")
            hex_str += hex_char
            steg_icmp(hex_char)
    #os.system('python3.8 src/test.py')
    #steg_icmp()

if __name__ == '__main__':
    main()