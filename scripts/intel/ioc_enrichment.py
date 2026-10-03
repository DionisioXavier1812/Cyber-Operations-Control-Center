import requests

ip = "8.8.8.8"
url = f"https://ipapi.co/{ip}/json/"

try:
    data = requests.get(url, timeout=5).json()
    print(f"IP: {ip}")
    print(f"País: {data.get('country_name')}")
    print(f"Org: {data.get('org')}")
except Exception as e:
    print(f"Erro ao consultar IP: {e}")
