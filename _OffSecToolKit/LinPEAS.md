---
description: |
  linpeas.sh is a shell script that will search for all possible paths to escalate privileges on Linux hosts, checking for misconfigured permissions, SUID/SGID binaries, cron jobs, kernel exploits, credentials in files, and much more. The below command will run all priv esc checks with all checks enabled and store the output in a file for later review.

  Command Reference:

  	Run all checks (verbose): -a

  	Output File: linpeas_output.txt

command: |
  ./linpeas.sh -a | tee linpeas_output.txt
items:
  - Shell
OS:
  - Linux
phases:
  - PrivEsc
references:
  - https://github.com/peass-ng/PEASS-ng/tree/master/linPEAS
  - https://book.hacktricks.xyz/linux-hardening/privilege-escalation
---
