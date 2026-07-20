---
description: |
  Hashcat is a GPU-accelerated password recovery tool supporting a vast number of hash algorithms. The following command cracks a Kerberos TGS-REP hash (hash mode 13100) obtained via a Kerberoasting attack, such as with Impacket's GetUserSPNs.py, in an attempt to recover the plaintext password of a service account whose SPN ticket was requested and encrypted with its NTLM hash.

  Command Reference:

  	TGS Hash File: tgs.hash

  	Wordlist: /usr/share/wordlists/rockyou.txt

command: |
  hashcat -m 13100 tgs.hash /usr/share/wordlists/rockyou.txt
items:
  - TGS
services:
  - Kerberos
OS:
  - Linux
  - Windows
phases:
  - CredentialAccess
references:
  - https://github.com/hashcat/hashcat
  - https://hashcat.net/wiki/doku.php?id=example_hashes
---
