---
description: |
  Braa is an Ultra-fast SNMPv1/v2 stack. Get/set/walk tens of thousands of hosts at once. The following command will bruteforce SNMP service object identifiers(OIDs).

  Command Reference:

      Community string: public

      Target: 10.10.10.1

command: |
  braa public@10.10.10.1:.1.*
items:
  - No_Creds
services:
  - SNMP
OS:
  - Linux
  - Windows
phases:
  - Enumeration
references:
  - https://github.com/mteg/braa
---
