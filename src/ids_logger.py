from scapy.all import sniff
from scapy.layers.inet import IP, TCP
from datetime import datetime

# =========================
# BLOCKED IP LIST
# =========================

blocked_ips = set()

# =========================
# LOG FILE
# =========================

log_file = "../logs/alerts.log"

# =========================
# SAVE LOG
# =========================

def save_log(message):

    with open(log_file, "a", encoding="utf-8") as f:

        f.write(message + "\n")

# =========================
# BLOCK FUNCTION
# =========================

def block_ip(ip):

    if ip not in blocked_ips:

        blocked_ips.add(ip)

        block_message = f"[BLOCKED IP]: {ip}"

        print(block_message)

        save_log(block_message)

# =========================
# DETECTION FUNCTION
# =========================

def detect_attack(packet):

    if packet.haslayer(IP):

        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        # TCP only
        if packet.haslayer(TCP):

            dst_port = packet[TCP].dport

            print("\n========== PACKET ==========")

            print(f"Source IP      : {src_ip}")

            print(f"Destination IP : {dst_ip}")

            print(f"Destination Port: {dst_port}")

            suspicious_ports = [443]

            # =========================
            # DETECT
            # =========================

            if dst_port in suspicious_ports:

                # Skip if already blocked
                if src_ip in blocked_ips:

                    return

                current_time = datetime.now()

                alert_message = (
                    f"[{current_time}] "
                    f"[ALERT] ATTACK DETECTED | "
                    f"SRC={src_ip} "
                    f"DST={dst_ip} "
                    f"PORT={dst_port}"
                )

                print(alert_message)

                save_log(alert_message)

                block_ip(src_ip)

            else:

                print("Normal Traffic")

# =========================
# START SYSTEM
# =========================

print("Starting AI IDS/IPS System...")

sniff(
    prn=detect_attack,
    store=False,
    count=100
)