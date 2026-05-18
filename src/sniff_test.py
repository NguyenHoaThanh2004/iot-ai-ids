from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

# =========================
# PACKET CALLBACK
# =========================

def process_packet(packet):

    # Kiểm tra có IP không
    if packet.haslayer(IP):

        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        protocol = packet[IP].proto

        print("\n========== PACKET ==========")

        print(f"Source IP      : {src_ip}")

        print(f"Destination IP : {dst_ip}")

        print(f"Protocol       : {protocol}")

        # TCP
        if packet.haslayer(TCP):

            print("Type           : TCP")

            print(f"Source Port    : {packet[TCP].sport}")

            print(f"Destination Port: {packet[TCP].dport}")

        # UDP
        elif packet.haslayer(UDP):

            print("Type           : UDP")

            print(f"Source Port    : {packet[UDP].sport}")

            print(f"Destination Port: {packet[UDP].dport}")

# =========================
# START SNIFFING
# =========================

print("Starting Packet Sniffer...")

sniff(
    prn=process_packet,
    store=False,
    count=10    #chạy 10 dòng 
) 