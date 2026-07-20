---
description: |
  Hashcat is a GPU-accelerated password recovery tool supporting a vast number of hash algorithms. The following command cracks a file of NTLM hashes (hash mode 1000) using a dictionary attack, which is commonly used after dumping hashes from SAM/NTDS.dit via tools such as secretsdump.py to recover usable plaintext credentials.

  Command Reference:

  	Hash File: hash.txt

  	Wordlist: /usr/share/wordlists/rockyou.txt

command: |
  hashcat -m 1000 hash.txt /usr/share/wordlists/rockyou.txt
items:
  - Hash
OS:
  - Linux
  - Windows
phases:
  - CredentialAccess
references:
  - https://github.com/hashcat/hashcat
  - https://hashcat.net/wiki/doku.php?id=example_hashes
---
