# Network Automation & Security Scripting (Python + Linux)

## Overview
This project demonstrates practical network automation and security scripting using Python and Linux tools. It includes four essential modules that simulate real-world network monitoring, security alerting, firewall behavior, and telemetry data collection.

## Features

### 1. ICMP Ping and Interface Monitoring
- Periodically pings external IPs like 8.8.8.8 and 1.1.1.1
- Monitors the status of a selected network interface (for example, wlp3s0)
- Console output clearly indicates up/down status of hosts and interfaces

### 2. Syslog-Based Alerting
- Monitors /var/log/syslog for suspicious keywords such as "unauthorized" or "failed"
- Prints real-time alerts if anomalies are detected

### 3. Simulated Firewall Behavior with iptables
- Uses Linux iptables to block incoming ICMP traffic
- Effectiveness validated using ping and Wireshark
- Wireshark capture confirms ICMP echo requests with no replies when rule is active

### 4. Basic Linux Telemetry Monitoring
- Displays CPU, RAM, and disk usage using the psutil library
- Tracks network I/O statistics
- Script runs in terminal with a refresh interval of 5 seconds

## Requirements
- Python 3.8 or newer
- psutil (install with pip inside a virtual environment)
- Linux system (Debian/Ubuntu recommended)
- iptables and Wireshark for traffic inspection

## How to Run Each Module

### ICMP and Interface Monitor
```bash
python3 icmp_interface_monitor.py
```

### Syslog Alert
```bash
python3 syslog_alert.py
```

### Firewall Simulation
```bash
sudo iptables -I INPUT -p icmp -j DROP
ping 8.8.8.8
# To remove rule:
sudo iptables -F
```

### Telemetry Monitor
```bash
python3 -m venv venv
source venv/bin/activate
pip install psutil
python telemetry_monitor.py
```

## Screenshots
- icmp_results.pcapng: Wireshark capture file of ICMP echo requests being blocked by iptables

## What I Learned
- Writing practical network automation scripts in Python
- Monitoring Linux system performance and logs
- Understanding and applying iptables for network control
- Using Wireshark for packet-level analysis and debugging

## Project Structure
```
.
├── icmp_interface_monitor.py
├── syslog_alert.py
├── firewall_simulation.md
├── telemetry_monitor.py
├── icmp_results.pcapng
├── README.md
└── venv/  (excluded from version control)
```

## License
This project is licensed under the MIT License.

## Author
Chandana Palagod

If you find this project useful, consider giving the repository a star on GitHub.

