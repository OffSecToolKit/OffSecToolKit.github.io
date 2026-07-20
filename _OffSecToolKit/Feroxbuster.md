---
description: |
  feroxbuster is a fast, recursive content-discovery tool written in Rust that brute-forces directories and files on a web server and automatically recurses into any newly discovered directories. The following command fuzzes the target with a wordlist, appends common extensions, and writes discovered results to a file for later review.

  Command Reference:

  	Target URL: http://10.10.10.1/

  	Wordlist: /usr/share/wordlists/seclists/Discovery/Web-Content/raft-medium-directories.txt

  	Output File: output.txt

command: |
  feroxbuster -u http://10.10.10.1/ -w /usr/share/wordlists/seclists/Discovery/Web-Content/raft-medium-directories.txt -x php,html,txt,bak -t 50 -o output.txt
items:
  - No_Creds
services:
  - Web
OS:
  - Linux
phases:
  - Enumeration
references:
  - https://github.com/epi052/feroxbuster
  - https://github.com/danielmiessler/SecLists
---
