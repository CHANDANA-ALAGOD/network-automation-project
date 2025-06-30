import time

def monitor_syslog():
    logfile = "/var/log/auth.log"
    with open(logfile, "r") as log:
        log.seek(0, 2)  # move to end of file
        while True:
            line = log.readline()
            if "Failed password" in line:
                print(f"[!] ALERT: {line.strip()}")
            time.sleep(0.2)

monitor_syslog()
