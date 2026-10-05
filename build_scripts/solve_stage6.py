#!/usr/bin/env python3
"""
Stage 6 Solver - Extract and decrypt flag from PCAP
"""
import base64
from scapy.all import rdpcap, TCP, Raw

PCAP = "/home/vboxuser/BREACHPOINT/stage6-networking/html/assets/capture.pcap"
XOR_KEY = "IT24102409:alexvance-dev"

def xor_decrypt(data, key):
    key_bytes = key.encode()
    return bytes([data[i] ^ key_bytes[i % len(key_bytes)] for i in range(len(data))])

def solve():
    packets = rdpcap(PCAP)
    exfil_data = ""

    for pkt in packets:
        if TCP in pkt and pkt[TCP].dport == 9001 and Raw in pkt:
            exfil_data += pkt[Raw].load.decode(errors='ignore')

    print(f"[+] Reconstructed stream: {exfil_data[:80]}...")

    if "NEXACORE_LEDGER_EXFIL:" in exfil_data:
        encoded = exfil_data.split("NEXACORE_LEDGER_EXFIL:")[1]
        print(f"[+] Encrypted payload (base64): {encoded[:50]}...")

        decoded = base64.b64decode(encoded)
        decrypted = xor_decrypt(decoded, XOR_KEY)
        flag = decrypted.decode(errors='ignore')
        print(f"[+] Decrypted: {flag}")
        return flag
    else:
        print("[-] Exfil marker not found")
        return None

if __name__ == "__main__":
    solve()
