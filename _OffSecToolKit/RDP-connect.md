---
description: |
  The Remote Desktop Protocol (RDP) is a protocol, or technical standard, for using a desktop computer remotely. xfreerdp is an X11 Remote Desktop Protocol (RDP) client which is part of the FreeRDP project. The following command connects to the remote RDP service.

  Command Reference:

      User: john

      Password: password123

      Target: 10.10.10.1

command: |
  xfreerdp /u:john /p:"password123" /v:10.10.10.1
items:
  - No_Creds
services:
  - RDP
OS:
  - Linux
  - Windows
phases:
  - Enumeration
references:
  - https://linux.die.net/man/1/xfreerdp
---
