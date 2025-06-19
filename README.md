# ⚡ Modbus IDS – Industrial Intrusion Detection System

Modbus IDS is a lightweight Python-based intrusion detection system designed for industrial environments. It monitors Modbus TCP traffic, detects suspicious activity such as invalid function codes or high-frequency requests, and can optionally block malicious IP addresses using iptables.

Ideal for energy systems, SCADA networks, industrial IoT, and PLC-based infrastructures.

---

## 🚀 Features

- Real-time monitoring of Modbus TCP traffic
- Detection of:
  - Invalid or unauthorized Modbus function codes
  - Modbus flood/DoS attacks
- Alarm logging to file and console
- Optional **automatic IP blocking** via `iptables`
- Lightweight: works on Raspberry Pi and similar SBCs
- Can be deployed as a Linux service with `systemd`

---

## 🛠 Requirements

- Python 3.8 or newer
- Linux (Kali, Debian, Raspberry Pi OS, etc.)
- Dependencies:

```bash
pip install -r requirements.txt
```
---

## 📁 Project Structure
```bash
modbus-ids/
├── modbus_ids.py              # Main IDS script
├── modbus_client.py           # Modbus client simulator
├── modbus_server.py           # Modbus server simulator
├── configs/
│   └── whitelist.txt          # Whitelisted trusted IPs
├── logs/
│   └── ids_alerts.log         # Example alert log
├── utils/
│   ├── log_handler.py         # (optional) Log formatting
│   └── firewall.py            # IP blocking logic
├── systemd/
│   └── modbus-ids.service     # Linux service file
├── hardware-design/
│   └── (optional PCB files, Altium designs)
└── requirements.txt
```
---

## 🧪 Testing Environment
Run everything locally via loopback (127.0.0.1)
Or simulate on a private LAN (e.g. 192.168.x.x)
Use included Python scripts for client/server communication

---

## ⚙️ Installation
```bash
git clone https://github.com/<your-username>/modbus-ids.git
cd modbus-ids
pip install -r requirements.txt
sudo python3 modbus_ids.py
```
To install as a service:
```bash
sudo cp systemd/modbus-ids.service /etc/systemd/system/
sudo systemctl daemon-reexec
sudo systemctl enable modbus-ids
sudo systemctl start modbus-ids
```

---

🧠 Customization
Add known trusted devices to configs/whitelist.txt

Adjust alerting thresholds in modbus_ids.py

Modify or disable automatic IP blocking if needed

---

🔐 Security Notice
This tool interacts with system-level firewall rules (iptables). Use with caution in production. For critical SCADA systems, start in passive alert-only mode.

---

🙌 Contributions
PRs, issues, forks — all are welcome.
Let’s make OT/ICS environments safer together.

📜 License
MIT – Use freely, but responsibly.

👨‍💻 Developer
Berhan ÖZTÜRK – Electrical & Electronics Engineer
🔗 [https://www.linkedin.com/in/berhanozturk/]
☕ Support or sponsor via BuyMeACoffee (optional)
