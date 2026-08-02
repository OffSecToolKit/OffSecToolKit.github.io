---
description: |
  Microsoft SQL Server is a proprietary relational database management system developed by Microsoft. mssqlclient.py is a Python script that allows a user to connect to a mssql server. The following command will login to the MSSQL server using Windows authentication.

  Command Reference:

      Username: john

      Target: 10.10.10.1

command: |
  mssqlclient.py john@10.10.10.1 -windows-auth
items:
  - No_Creds
services:
  - MSSQL
OS:
  - Linux
  - Windows
phases:
  - Enumeration
references:
  - https://github.com/fortra/impacket/blob/master/examples/mssqlclient.py
  - https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?view=sql-server-ver16
---
