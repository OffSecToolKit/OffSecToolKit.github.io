---
description: |
  lse.sh (linux-smart-enumeration) is a privilege escalation enumeration script designed with different verbosity levels so an attacker can control how much information is surfaced, highlighting the most interesting findings (highlighted in color) that are likely to lead to privesc. Level 1 provides a good balance of detail without the full noise of level 2, making it a fast first pass on a new foothold.

  Command Reference:

  	Verbosity level 1: -l1

command: |
  ./lse.sh -l1
items:
  - Shell
OS:
  - Linux
phases:
  - PrivEsc
references:
  - https://github.com/diego-treitos/linux-smart-enumeration
  - https://book.hacktricks.xyz/linux-hardening/privilege-escalation
---
