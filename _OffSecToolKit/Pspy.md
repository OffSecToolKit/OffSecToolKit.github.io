---
description: |
  pspy is a command-line tool that snoops on process activity without requiring root permissions, allowing an attacker to observe cron jobs, scheduled tasks, and other processes launched by root or other users in real time. This is invaluable for identifying privileged processes that execute attacker-writable scripts or binaries. The following command polls the process table frequently and prints file system events.

  Command Reference:

  	Print file system events: -pf

  	Scan interval (ms): -i 1000

command: |
  ./pspy64 -pf -i 1000
items:
  - Shell
OS:
  - Linux
phases:
  - PrivEsc
references:
  - https://github.com/DominicBreuker/pspy
  - https://book.hacktricks.xyz/linux-hardening/privilege-escalation#processes
---
