from scapy.all import sniff
from scapy.layers.inet import IP, TCP

# =========================
# BLOCK FUNCTION
# =========================

blocked_ips = set()

def block_ip(ip):

    if ip not in blocked_ips:

        blocked_ips.add(ip)

        print(f"\n🚫 BLOCKED IP: {ip}")

# =========================
# DETECTION FUNCTION
# =========================

def detect_attack(packet):

    if packet.haslayer(IP):

        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        print("\n========== PACKET ==========")

        print(f"Source IP      : {src_ip}")

        print(f"Destination IP : {dst_ip}")

        # TCP only
        if packet.haslayer(TCP):

            dst_port = packet[TCP].dport

            print(f"Destination Port: {dst_port}")

            suspicious_ports = [443]

            # =========================
            # DETECT
            # =========================

            if dst_port in suspicious_ports:

                print("\n⚠️ ATTACK DETECTED!")

                block_ip(src_ip)

            else:

                print("Normal Traffic")

# =========================
# START IDS/IPS
# =========================

print("Starting IDS/IPS System...")

sniff(
    prn=detect_attack,
    store=False,
    count=30
)