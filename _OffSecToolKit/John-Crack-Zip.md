---
description: |
  John the Ripper ships with helper utilities that convert protected files into a crackable hash format. The following command uses zip2john to extract the password hash from a password-protected zip archive, then feeds the resulting hash file into John with a wordlist attack to recover the archive's password.

  Command Reference:

  	Protected Zip: protected.zip

  	Hash File: zip.hash

  	Wordlist: /usr/share/wordlists/rockyou.txt

command: |
  zip2john protected.zip > zip.hash && john --wordlist=/usr/share/wordlists/rockyou.txt zip.hash
items:
  - No_Creds
OS:
  - Linux
  - Windows
phases:
  - CredentialAccess
references:
  - https://github.com/openwall/john
  - https://www.openwall.com/john/
---
