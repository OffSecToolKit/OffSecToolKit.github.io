---
description: |
  sudo -l lists the commands the current user is permitted to run via sudo, along with the users/groups they can run them as. Misconfigured sudo rules (e.g. NOPASSWD entries or binaries with known GTFOBins sudo bypasses) can allow an attacker to escalate to root or another privileged account without ever needing that account's password.

  Command Reference:

  	List allowed sudo commands: -l

command: |
  sudo -l
items:
  - Shell
OS:
  - Linux
phases:
  - PrivEsc
references:
  - https://gtfobins.github.io/#+sudo
  - https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid
---
