import socket, requests #please, install package "requests": "pip install requests"
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
public_ip = requests.get('https://api.ipify.org').text
print(f"Hostname: \t {hostname}")
print(f"Local IP: \t {local_ip}")
print(f"Public IP: \t {public_ip}")
