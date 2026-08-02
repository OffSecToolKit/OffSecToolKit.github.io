---
description: |
  Transparent Network Substrate (TNS), a proprietary Oracle computer-networking technology, supports homogeneous peer-to-peer connectivity on top of other networking technologies such as TCP/IP, SDP and named pipes. TNS operates mainly for connecting to Oracle databases. SQLPlus is an interactive and batch query tool that is installed with every Oracle Database installation. The following command logs in to the target Oracle database.

  Command Reference:

      User: john

      Password: password123

      Target: 10.10.10.1

      Datbase: oracle

command: |
  sqlplus john/password123@10.10.10.1/oracle
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
  - https://docs.oracle.com/cd/E11882_01/server.112/e41085/sqlqraa001.htm#SQLQR985
  - https://docs.oracle.com/cd/B19306_01/server.102/b14357/qstart.htm
---
