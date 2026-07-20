---
description: |
  ffuf is a fast, Go-based web fuzzer used to brute-force directories, files, and parameters on a target web server. The following command fuzzes for hidden directories and files by substituting the FUZZ keyword with each line of a wordlist, appending common extensions, and filtering matched HTTP status codes to quickly surface accessible but unlinked content.

  Command Reference:

  	Target URL: http://10.10.10.1/FUZZ

  	Wordlist: /usr/share/wordlists/seclists/Discovery/Web-Content/raft-medium-directories.txt

command: |
  ffuf -u http://10.10.10.1/FUZZ -w /usr/share/wordlists/seclists/Discovery/Web-Content/raft-medium-directories.txt -e .php,.html,.txt,.bak -mc 200,204,301,302,307,401,403 -t 50
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
