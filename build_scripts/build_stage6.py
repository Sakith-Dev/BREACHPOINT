#!/usr/bin/env python3
"""
Stage 6 PCAP Generator - NexaCore Exfiltration
Uses STG-03 crypto info: XOR-Stream with key IT24102409:alexvance-dev
"""

from scapy.all import *
import base64
import os

OUTPUT_PCAP = "/home/vboxuser/BREACHPOINT/stage6-networking/html/assets/capture.pcap"
FLAG = "FLAG{N3TW0RK_exf1ltr4t10n_d3cr1pt3d}"
XOR_KEY = "IT24102409:alexvance-dev"  # Same key as STG-03

def xor_encrypt(data, key):
    """XOR encrypt data with key"""
    key_bytes = key.encode()
    data_bytes = data.encode() if isinstance(data, str) else data
    return bytes([data_bytes[i] ^ key_bytes[i % len(key_bytes)] for i in range(len(data_bytes))])

def create_pcap():
    packets = []

    # Normal HTTP noise
    for i in range(5):
        pkt = IP(src="192.168.1.100", dst="192.168.1.1") / \
              TCP(sport=45000+i, dport=80, flags="S") / \
              Raw(load=b"GET /index.html HTTP/1.1\r\nHost: nexacore.local\r\n\r\n")
        packets.append(pkt)

    # Normal DNS traffic
    for i in range(3):
        pkt = IP(src="192.168.1.100", dst="8.8.8.8") / \
              UDP(sport=53000+i, dport=53) / \
              Raw(load=b"\x12\x34\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00")
        packets.append(pkt)

    # Suspicious exfiltration on port 9001
    payload = xor_encrypt(FLAG, XOR_KEY)
    encoded_payload = base64.b64encode(payload).decode()
    exfil_data = f"NEXACORE_LEDGER_EXFIL:{encoded_payload}"

    chunk_size = 50
    for i in range(0, len(exfil_data), chunk_size):
        chunk = exfil_data[i:i+chunk_size]
        pkt = IP(src="192.168.1.100", dst="203.0.113.50") / \
              TCP(sport=55000+i, dport=9001, flags="PA") / \
              Raw(load=chunk.encode())
        packets.append(pkt)

    # Normal HTTPS after
    for i in range(3):
        pkt = IP(src="192.168.1.100", dst="192.168.1.1") / \
              TCP(sport=46000+i, dport=443, flags="S") / \
              Raw(load=b"\x16\x03\x01\x00\x00")
        packets.append(pkt)

    wrpcap(OUTPUT_PCAP, packets)
    print(f"[+] PCAP created: {OUTPUT_PCAP}")
    print(f"[+] Total packets: {len(packets)}")
    print(f"[+] XOR key: {XOR_KEY}")
    print(f"[+] Flag: {FLAG}")
    print(f"[+] Encrypted payload (base64): {encoded_payload[:50]}...")

if __name__ == "__main__":
    os.makedirs(os.path.dirname(OUTPUT_PCAP), exist_ok=True)
    create_pcap()
