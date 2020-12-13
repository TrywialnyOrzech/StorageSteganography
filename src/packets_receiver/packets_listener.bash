echo '[*] Creating file for packets...'
touch capture.pcap
echo '[*] Running TShark...'
# sudo tshark -i "eth0" -f "src host 192.168.8.156 && icmp" > tsharkdump.csv
sudo tcpdump -i "eth0" src 192.168.8.156 -w capture.pcap
od -c -b capture.pcap > pure_bytes.pcap
