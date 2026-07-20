---
description: |
  Masscan is an asynchronous, extremely high-speed port scanner capable of scanning the entire IPv4 address space in minutes. Attackers use it during recon to rapidly sweep a large target range across the full 65535-port space to identify every open port before running slower, more detailed scanners like Nmap against the discovered hosts/ports.

  Command Reference:

  	Target IP: 10.10.10.1

  	Port Range: 1-65535

  	Rate (packets/sec): 1000

  	Output file (grepable): masscan_output.txt

command: |
  masscan -p1-65535 10.10.10.1 --rate 1000 -oG masscan_output.txt
items:
  - No_Creds
OS:
  - Linux
phases:
  - Recon
references:
  - https://github.com/robertdavidgraham/masscan
---
