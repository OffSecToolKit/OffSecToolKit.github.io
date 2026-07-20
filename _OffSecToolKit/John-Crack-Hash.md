---
description: |
  John the Ripper is an offline password cracking tool that supports a huge range of hash formats. The following command runs a wordlist-based dictionary attack against a file of extracted hashes, attempting to recover the plaintext password for each hash by comparing it against every word (and John's built-in mangling rules) in the supplied wordlist.

  Command Reference:

  	Hash File: hash.txt

  	Wordlist: /usr/share/wordlists/rockyou.txt

command: |
  john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
items:
  - Hash
OS:
  - Linux
  - Windows
phases:
  - CredentialAccess
references:
  - https://github.com/openwall/john
  - https://www.openwall.com/john/
---
