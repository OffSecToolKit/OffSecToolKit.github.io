---
description: |
  ffuf can also be used to discover virtual hosts that are not resolvable via public DNS but are configured on the target web server, by fuzzing the Host header while requesting the server's IP directly. Filtering out the response size of the default/unknown vhost helps isolate genuine matches from the server's catch-all response.

  Command Reference:

  	Target URL: http://10.10.10.1/

  	Domain: test.local

  	Wordlist: /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt

  	Default response size to filter: 4242

command: |
  ffuf -u http://10.10.10.1/ -H "Host: FUZZ.test.local" -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt -fs 4242
items:
  - No_Creds
services:
  - Web
OS:
  - Linux
phases:
  - Enumeration
references:
  - https://github.com/ffuf/ffuf
  - https://github.com/danielmiessler/SecLists
---
