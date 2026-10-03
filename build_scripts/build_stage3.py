import base64
import os

# 1. Plaintext Memo Content (Narrative + Flag + Stage 4 Web Endpoint)
plaintext = """
====================================================================
CONFIDENTIAL - NEXACORE TECHNOLOGIES INTERNAL MEMO
FROM: Alex Vance (Lead Systems Engineer)
TO: Internal Operations
--------------------------------------------------------------------
SYSTEM AUDIT FLAG: FLAG{CRYPTO_n3x4c0r3_m3m0_d3cryp73d}

OPERATIONAL DIRECTIVE:
Core repository access has been restricted. Secondary persistence 
pipeline deployed at restricted endpoint:
http://localhost:8080/internal/status

Headers required: X-Forwarded-For: 127.0.0.1
====================================================================
""".strip()

# 2. Key Derivation Logic (Employee ID + Dev Handle)
emp_id = "IT24102409"
dev_handle = "alexvance-dev"
derived_key = f"{emp_id}:{dev_handle}"

# 3. Stream XOR Encryption
key_bytes = derived_key.encode('utf-8')
pt_bytes = plaintext.encode('utf-8')

encrypted_bytes = bytearray()
for i in range(len(pt_bytes)):
    encrypted_bytes.append(pt_bytes[i] ^ key_bytes[i % len(key_bytes)])

# 4. Base64 Encoding
encoded_cipher = base64.b64encode(encrypted_bytes).decode('utf-8')

# 5. Output Payload File directly into Nginx html/assets/memos/ directory
output_path = os.path.join(os.path.dirname(__file__), "../stage3-crypto/html/assets/memos/memo.enc")

with open(output_path, "w") as f:
    f.write("--- NEXACORE ENCRYPTED ASSET ---\n")
    f.write("ALGORITHM: XOR-Stream\n")
    f.write("KEY_FORMAT: <EMP_ID>:<DEV_HANDLE>\n")
    f.write(f"PAYLOAD:\n{encoded_cipher}\n")

print(f"[+] Stage 3 encrypted payload generated at: {output_path}")
