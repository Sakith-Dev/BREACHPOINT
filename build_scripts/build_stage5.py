import os
import zipfile

log_content = """--- NEXACORE AUDIT LOG ---
DATE: 2026-08-11
USER: alexvance-dev
ACTION: Sudo access granted
STATUS: SUSPICIOUS
EVIDENCE: FLAG{43N51_n3x4c0r3_10g_r3c0v3r3d}
"""

#creating a temporary log file
with open("audit.log", "w") as f:
    f.write(log_content)

# 3. Compressing to zip
with zipfile.ZipFile("corrupted_audit.log", "w", compression=zipfile.ZIP_DEFLATED) as zipf:
    zipf.write("audit.log")

# 4. Remove the temporary plain log
os.remove("audit.log")

# 5. Corrupt the file by zeroing the first 8 bytes (Magic Bytes)
with open("corrupted_audit.log", "r+b") as f:
    f.seek(0)
    f.write(b'\x00' * 8)

# 6. Move the corrupted file to the Nginx Stage 5 folder
output_path = os.path.join(os.path.dirname(__file__), "../stage5-forensics/html/assets/logs/corrupted_audit.log")
os.makedirs(os.path.dirname(output_path), exist_ok=True)
os.rename("corrupted_audit.log", output_path)

print(f"[+] Stage 5 corrupted audit log generated at: {output_path}")
