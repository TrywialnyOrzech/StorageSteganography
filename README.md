# StorageSteganography

This project contains packets sender and receiver for covert channel purposes. It implements storage steganography method, which modifies payload of an ICMP packet. This is meant to be an example of a module of a malware, which possibly could steal information from victim's network.

Packet sender sends ICMP echo request in random time intervals. Packet receiver is constantly sniffing for new packets from sending module. After proper packet recognition, receiver decodes payload to UTF-8 and establishes position of transmitted char cointaining information. Received information appears in decoded_packets.txt file.

NOTE: Python 3.4-3.8 is required.

To setup project:
```
# to download project
git clone https://github.com/TrywialnyOrzech/StorageSteganography
cd StorageSteganography

# create file with message to send
touch text_to_send.txt
# optionally: fill it with random letters
< /dev/urandom tr -dc "[:alnum:]" | head -c1000 > text_to_send.txt

# create Python virtual environment and install dependencies
python -m venv venv
source venv/bin/activate
pip install scapy[basic]
```
Add proper IP addresses for destination and source in steg.py and packet_listener.py respectively.

To run packet listener:
```
python src/packet_listener.py
```

To run packet sender:
```
python main.py
```
