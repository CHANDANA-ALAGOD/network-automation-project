import psutil
import time
import os

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def get_readable(bytes, unit='MB'):
    if unit == 'MB':
        return f"{bytes / (1024 * 1024):.2f} MB"
    elif unit == 'GB':
        return f"{bytes / (1024 * 1024 * 1024):.2f} GB"

while True:
    clear()

    print("--- Linux Telemetry Report ---")
    print(f"CPU Usage      : {psutil.cpu_percent()}%")


    mem = psutil.virtual_memory()
    print(f"Memory Usage   : {mem.percent}% ({get_readable(mem.used)} used / {get_readable(mem.total)} total)")
    disk = psutil.disk_usage('/')
    print(f"Disk Usage     : {disk.percent}% ({get_readable(disk.used)} used / {get_readable(disk.total)} total)")
    net = psutil.net_io_counters()
    print(f"Network I/O    : Sent {get_readable(net.bytes_sent)}, Received {get_readable(net.bytes_recv)}")

    time.sleep(5)
