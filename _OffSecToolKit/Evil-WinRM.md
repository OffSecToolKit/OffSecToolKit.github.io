---
description: |
  Evil-WinRM uses Windows Remote Management (WinRM) to give you an interactive shell on the Windows host.

  Command Reference:

  	Target IP: 10.10.10.1

  	Username: john

  	Password: password123

command: |
  evil-winrm -i 10.10.10.1 -u john -p password123
items:
  - Password
  - Username
services:
  - WinRM
OS:
  - Linux
  - Windows
phases:
  - Exploitation
references:
  - https://github.com/Hackplayers/evil-winrm
---
