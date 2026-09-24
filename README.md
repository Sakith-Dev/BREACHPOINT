# BREACHPOINT: Incident Response CTF Play Box
**Module:** IE3132 - Penetration Testing & Vulnerability Assessment  
**Scenario:** NexaCore Technologies Insider Threat Investigation  

---

## 👥 Project Team & Responsibilities
* **Platform & Infrastructure Lead:** Chandrasekara RMS (IT24101383)
* **Challenge Design Lead A (STG-01, 02, 03):** Herath H HADSJ (IT24102409)
* **Challenge Design Lead B (STG-04, 05, 06):** Avishka GPM (IT24103169)
* **Integration, Testing & QA Lead:** Wickramasinghe M S (IT24103344)

---

## 🚀 Quick Start: Running the Platform

### Prerequisites
* Ubuntu 22.04 LTS or Kali Linux
* Docker Engine (`>= 24.0`) and Docker Compose v2 (`docker-compose-plugin`)
* Git CLI

### Deployment Steps
```bash
# 1. Clone the repository
git clone [https://github.com/Sakith-Dev/BREACHPOINT.git](https://github.com/Sakith-Dev/BREACHPOINT.git)
cd BREACHPOINT

# 2. Build and start all isolated microservices
docker compose up -d

# 3. Verify that all 4 containers are up and healthy
docker compose ps
