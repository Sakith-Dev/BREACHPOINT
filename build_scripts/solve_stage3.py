import base64
import os

# 1. Read Encrypted File from html directory
input_path = os.path.join(os.path.dirname(__file__), "../stage3-crypto/html/assets/memos/memo.enc")

with open(input_path, "r") as f:
    lines = f.readlines()

b64_payload = lines[-1].strip()

# 2. Reconstruct Derived Key
emp_id = "IT24102409"
dev_handle = "alexvance-dev"
key = f"{emp_id}:{dev_handle}".encode('utf-8')

# 3. Base64 Decode & XOR Decrypt
cipher_bytes = base64.b64decode(b64_payload)
decrypted_bytes = bytearray()

for i in range(len(cipher_bytes)):
    decrypted_bytes.append(cipher_bytes[i] ^ key[i % len(key)])

print("\n--- DECRYPTED MEMO OUTPUT ---")
print(decrypted_bytes.decode('utf-8'))
