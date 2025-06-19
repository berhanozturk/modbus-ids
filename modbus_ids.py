from scapy.all import sniff
from scapy.layers.inet import IP, TCP
import time
import subprocess

MODBUS_PORT = 502

request_times = {}
valid_func_codes = {1,2,3,4,5,6,15,16}
blocked_ips = set()

def log_alarm(msg):
    with open("ids_alerts.log", "a") as f:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp} - {msg}\n")

def block_ip(ip):
    if ip in blocked_ips:
        return
    print(f"[ENGELLE] {ip} IP'si iptables ile engelleniyor!")
    subprocess.run(["sudo", "iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"])
    blocked_ips.add(ip)

def modbus_func_code(payload):
    if len(payload) > 7:
        return payload[7]
    return None

def packet_callback(pkt):
    if IP in pkt and TCP in pkt and pkt[TCP].dport == MODBUS_PORT:
        payload = bytes(pkt[TCP].payload)
        if not payload:
            return
        func_code = modbus_func_code(payload)
        src_ip = pkt[IP].src

        if func_code is None:
            alarm_msg = f"Modbus fonksiyon kodu bulunamadı! Kaynak: {src_ip}"
            print(f"[ALARM] {alarm_msg}")
            log_alarm(alarm_msg)
            return

        if func_code not in valid_func_codes:
            alarm_msg = f"Şüpheli fonksiyon kodu: {func_code} Kaynak: {src_ip}"
            print(f"[ALARM] {alarm_msg}")
            log_alarm(alarm_msg)
            return

        now = time.time()
        request_times.setdefault(src_ip, [])
        request_times[src_ip] = [t for t in request_times[src_ip] if now - t < 1]
        request_times[src_ip].append(now)

        if len(request_times[src_ip]) > 5:
            alarm_msg = f"{src_ip} çok hızlı istek gönderiyor! ({len(request_times[src_ip])} istek/sn)"
            print(f"[ALARM] {alarm_msg}")
            log_alarm(alarm_msg)
            block_ip(src_ip)

        print(f"Modbus Paket: Fonksiyon {func_code} Kaynak {src_ip}")

def main():
    print(f"Modbus IDS başlatıldı, port {MODBUS_PORT} dinleniyor...")
    sniff(filter=f"tcp port {MODBUS_PORT}", prn=packet_callback, store=0, iface="lo")

if __name__ == "__main__":
    main()
