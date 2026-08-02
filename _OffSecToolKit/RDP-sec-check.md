---
description: |
  The Remote Desktop Protocol (RDP) is a protocol, or technical standard, for using a desktop computer remotely. rdp-sec-check is a Perl script to enumerate security settings of an RDP Service. The following command checks the security settings of the RDP service.

  Command Reference:

      Target: 10.10.10.1

command: |
  rdp-sec-check.pl 10.10.10.1
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
  - https://github.com/CiscoCXSecurity/rdp-sec-check
---
