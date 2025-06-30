import subprocess
import time

hosts = ["8.8.8.8", "1.1.1.1"]
interface = "wlp3s0"

def ping_host(host):
    try:
        subprocess.check_output(["ping", "-c", "1", "-W", "1", host], stderr=subprocess.DEVNULL)
        print(f"[+] Host {host} is UP")
    except subprocess.CalledProcessError:
        print(f"[-] Host {host} is DOWN")

def check_interface(interface):
    result = subprocess.getoutput(f"ip link show {interface}")
    if "state UP" in result:
        print(f"[+] Interface {interface} is UP")
    else:
        print(f"[-] Interface {interface} is DOWN")

while True:
    print("\n--- Health Check ---")
    for h in hosts:
        ping_host(h)
    check_interface(interface)
    time.sleep(10)
