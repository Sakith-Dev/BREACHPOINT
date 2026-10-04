# CTFd Setup and Challenge Restore Guide

This guide explains how to start the CTF services and restore all challenges, flags, and configurations on your local machine.

---

## 1. Prerequisites
Make sure you have installed:
- Docker
- Docker Compose
- Git

---

## 2. Start the Docker Services
From the root repository folder (`breachpoint/`), run:

```bash
docker compose up -d
```

Once the containers are running, the services will be available at:
- **CTFd Platform:** http://localhost:8000
- **Stage 1 (OSINT):** http://localhost:8080
- **Stage 2 (Stegano):** http://localhost:8081
- **Stage 3 (Crypto):** http://localhost:8082
- **Stage 4 (Web):** http://localhost:8083
- **Stage 5 (Forensics):** http://localhost:8084
- **Stage 6 (Networking):** http://localhost:8085

---

## 3. Restore Challenges and Flags

1. Open your browser and go to:
   http://localhost:8000

2. If prompted with the setup wizard, create an admin account (or log in).
3. Navigate to the Admin Panel:
   http://localhost:8000/admin

4. Click **Config** in the top navigation bar, then click the **Backup** tab (or go directly to http://localhost:8000/admin/config).
5. Under the **Import** section, click **Choose File**.
6. Select the file:
   `ctfd_backup/ctfd_export.zip`
7. Click **Import**.

All challenges, categories, descriptions, hints, and flags will automatically be loaded.

---

## 4. Verification
- Go to http://localhost:8000/challenges to check that the challenge cards appear.
- Test any challenge URL above to verify the challenge environments respond properly.
