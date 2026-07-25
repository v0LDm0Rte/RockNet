💀 RockNet - DDOS Engine

Creator: v0LDm0Rte
Version: v1.0.1

---

📌 Description

RockNet is a multi-threaded network stress testing tool built with Python. It uses HTTP Flood, Socket Flood, Requests Flood, and ThreadPool attacks to simulate DDoS traffic. Supports 10,000+ threads, 50MB payloads, and live stats. Created by v0LDm0Rte v1.0.1. For authorized testing only.

---

⚡ Features

· 4 attack vectors combined
· 10,000+ concurrent threads
· 50MB payload per request
· Real-time live statistics
· User-Agent rotation
· Colored CLI interface
· Progress bar monitoring

---

📦 Installation

```bash
git clone https://github.com/v0LDm0Rte/RockNet.git
cd RockNet
pip install -r requirements.txt
python3 RockNet.py
```

---

📋 Requirements

```txt
requests>=2.28.0
pyfiglet>=0.8.post1
urllib3>=1.26.0
```

---

🚀 Usage

```bash
python3 RockNet.py
Enter Target URL: http://target.com
```

---

📊 Live Statistics

```
============================================================
                     LIVE STATS
============================================================
  [v0LDm0Rte] v.1.0.1
------------------------------------------------------------
  Time: 45s
  Total Requests: 1,234,567
  Successful: 1,200,000
  Failed: 34,567
  Speed: 27,434 req/s
  Threads: 3,050
  [████████████████████████░░░░░░░░░░░░░░░░] 75%
  STATUS: ATTACKING
============================================================
```

---

⚠️ Disclaimer

This tool is for educational and authorized testing only. Use only on systems you own or have permission to test. The developer assumes no liability for misuse or damage caused by this software.

---

📞 Contact

· GitHub: v0LDm0Rte
· Email: v0ldm0rte@onionmail.org

---

📜 License

MIT License - Free to use for educational purposes
