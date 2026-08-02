---
description: |
  MySQL is a simple SQL shell with input line editing capabilities. The following command will login to the MySQL server.

  Command Reference:

      Username: john

      Password: password123

      Target: 10.10.10.1

command: |
  mysql -u john -ppassword123 -h 10.10.10.1
items:
  - No_Creds
services:
  - MySQL
OS:
  - Linux
  - Windows
phases:
  - Enumeration
references:
  - https://linux.die.net/man/1/mysql
---
