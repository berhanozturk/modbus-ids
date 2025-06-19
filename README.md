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
git clone https://github.com/<your-username>/modbus-ids.git
cd modbus-ids
pip install -r requirements.txt
sudo python3 modbus_ids.py
sudo cp systemd/modbus-ids.service /etc/systemd/system/
sudo systemctl daemon-reexec
sudo systemctl enable modbus-ids
sudo systemctl start modbus-ids
