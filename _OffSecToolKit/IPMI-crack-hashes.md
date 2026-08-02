---
description: |
  IPMI (Intelligent Platform Management Interface) is a set of standardized specifications for hardware-based platform management systems that makes it possible to control and monitor servers centrally. Hashcat is the "World's fastest and most advanced password recovery utility". The following command will attempt to crack IPMI hashes.

  Command Reference:

      IPMI hashes file: ipmi-hash.txt

      Cracking wordlist: /usr/share/wordlists/rockyou.txt

command: |
  hashcat -m 7300 ipmi-hash.txt /usr/share/wordlists/rockyou.txt
items:
  - No_Creds
services:
  - IPMI
OS:
  - Linux
  - Windows
phases:
  - Enumeration
references:
  - https://hashcat.net/hashcat/
  - https://hashcat.net/wiki/doku.php?id=example_hashes
---
