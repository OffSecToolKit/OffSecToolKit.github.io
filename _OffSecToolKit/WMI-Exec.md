---
description: |
  The Remote Desktop Protocol (RDP) is a protocol, or technical standard, for using a desktop computer remotely. Wmiexec.py uses the Windows Management Instrumentation and DCOM to create a windows process to run commands. The following command executes a command using the WMI service.

  Command Reference:

      User: john

      password: password123

      Target: 10.10.10.1

      System command: whoami

command: |
  wmiexec.py john:"password123"@10.10.10.1 "whoami"
items:
  - No_Creds
services:
  - WMI
OS:
  - Linux
  - Windows
phases:
  - Enumeration
references:
  - https://github.com/fortra/impacket/blob/master/examples/wmiexec.py
---
