---
description: |
  nikto is a web server scanner that checks for thousands of known-dangerous files, outdated server software, default files, and common misconfigurations across HTTP and HTTPS services. The following command scans a target host and writes a plaintext report of all findings.

  Command Reference:

  	Target URL: http://10.10.10.1/

  	Output File: output.txt

command: |
  nikto -h http://10.10.10.1/ -o output.txt -Format txt
items:
  - No_Creds
services:
  - Web
OS:
  - Linux
phases:
  - Enumeration
references:
  - https://github.com/sullo/nikto
  - https://cirt.net/Nikto2
---
