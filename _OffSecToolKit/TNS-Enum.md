---
description: |
  Transparent Network Substrate (TNS), a proprietary Oracle computer-networking technology, supports homogeneous peer-to-peer connectivity on top of other networking technologies such as TCP/IP, SDP and named pipes. TNS operates mainly for connecting to Oracle databases. Oracle Database Attacking Tool (ODAT) is an open-source penetration testing tool written in Python and designed to enumerate and exploit vulnerabilities in Oracle databases. The following command performs a variey of scans to gather information about the Oracle database services and its components.

  Command Reference:

      Target: 10.10.10.1

command: |
  ./odat.py all -s 10.10.10.1
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
