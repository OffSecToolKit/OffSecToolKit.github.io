---
description: |
  Hydra is a fast, parallelized network login cracker that supports numerous protocols. The following command performs a password spray against SMB, testing a list of harvested/guessed usernames against a password wordlist. This is useful when no valid credentials are known yet but a set of likely usernames has been enumerated, as it avoids repeatedly hammering a single account and reduces the risk of lockout compared to a traditional per-user brute force.

  Command Reference:

  	Target IP: 10.10.10.1

  	User List: users.txt

  	Wordlist: /usr/share/wordlists/rockyou.txt

command: |
  hydra -L users.txt -P /usr/share/wordlists/rockyou.txt smb://10.10.10.1
items:
  - No_Creds
services:
  - SMB
OS:
  - Windows
phases:
  - CredentialAccess
references:
  - https://github.com/vanhauser-thc/thc-hydra
  - https://www.kali.org/tools/hydra/
---
