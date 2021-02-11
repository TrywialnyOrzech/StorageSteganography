from random import random

import string
from scapy.all import *
from scapy.layers.inet import IP, ICMP
from string import ascii_lowercase


def randString(n):
    random_source = string.ascii_letters + string.digits + string.punctuation
    password = ''

    for i in range(n):
        password += random.choice(random_source)

    password_list = list(password)
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    return password


def sniff_all():
    sniff(filter="icmp and host 8.8.8.8",
          prn=lambda x: x.show())  # lambda shows all packets being sent and received with IP headers


def randStr(n):
    return ''.join(random.sample(ascii_lowercase, n))


def steg_icmp(hex_char):
    data = randString(1)
    index = ord(data) // 4

    p = sr1(IP(dst="192.168.1.6") / ICMP() / data / randString(index - 2) / hex_char / randString(32 - index))

    time.sleep(0.1)
