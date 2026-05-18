from scapy.all import sniff
from scapy.layers.inet import IP, TCP

# =========================
# DETECT FUNCTION
# =========================

def detect_attack(packet):

    if packet.haslayer(IP):

        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        print("\n========== PACKET ==========")

        print(f"Source IP      : {src_ip}")

        print(f"Destination IP : {dst_ip}")

        # =========================
        # SIMPLE RULE
        # =========================

        if packet.haslayer(TCP):

            dst_port = packet[TCP].dport

            print(f"Destination Port: {dst_port}")

            # Example suspicious ports
            suspicious_ports = [21, 22, 23, 445]

            if dst_port in suspicious_ports:

                print("\n⚠️ ALERT: Suspicious Traffic Detected!")

            else:

                print("Normal Traffic")

# =========================
# START SNIFFING
# =========================

print("Starting Realtime Detection...")

sniff(
    prn=detect_attack,
    store=False,
    count=20
)