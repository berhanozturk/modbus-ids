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
