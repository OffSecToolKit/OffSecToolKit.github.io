---
description: |
  Transparent Network Substrate (TNS), a proprietary Oracle computer-networking technology, supports homogeneous peer-to-peer connectivity on top of other networking technologies such as TCP/IP, SDP and named pipes. TNS operates mainly for connecting to Oracle databases. Oracle Database Attacking Tool (ODAT) is an open-source penetration testing tool written in Python and designed to enumerate and exploit vulnerabilities in Oracle databases. The following command uploads a file with Oracle RDBMS.

  Command Reference:

      Target: 10.10.10.1

      Database: oracle

      User: john

      Password: password123

      Output file: /tmp/file.txt

      Upload file: test.txt

command: |
  ./odat.py utlfile -s 10.10.10.1 -d oracle -U john -P password123 --sysdba --putFile /tmp/ file.txt ./test.txt
items:
  - No_Creds
services:
  - TNS
OS:
  - Linux
  - Windows
phases:
  - Enumeration
references:
  - https://github.com/quentinhardy/odat
  - https://en.wikipedia.org/wiki/Transparent_Network_Substrate
---
