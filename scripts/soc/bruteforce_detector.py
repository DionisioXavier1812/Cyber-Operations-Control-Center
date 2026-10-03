import re

log_file = "logs/auth.log"

failed = {}

with open(log_file, "r") as f:
    for line in f:
        if "Failed password" in line:
            ip = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
            if ip:
                ip = ip.group(1)
                failed[ip] = failed.get(ip, 0) + 1

for ip, count in failed.items():
    if count > 5:
        print(f"[ALERTA] Possível brute force detectado do IP: {ip} ({count} tentativas)")
