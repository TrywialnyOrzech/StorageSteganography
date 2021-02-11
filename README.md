# StorageSteganography

This project contains packets sender and receiver for covert channel purposes. It implements storage steganography method, which modifies payload of an ICMP packet. This is meant to be an example of a module of a malware, which possibly could steal information from victim's network.

Packet sender sends ICMP echo request in random time intervals. Packet receiver is constantly sniffing for new packets from sending module. After proper packet recognition, receiver decodes payload to UTF-8 and establishes position of transmitted char cointaining information. Received information appears in decoded_packets.txt file.
