---
description: |
  Chisel is a fast TCP/UDP tunnel over HTTP, transported over SSH, that can be used to pivot into networks that are otherwise unreachable from the attacker host. Running chisel in server mode with --reverse allows a client running on a compromised host to dial back out to the attacker, which is useful when inbound firewall rules block direct connections to the target. Once the reverse client connects and requests a SOCKS proxy, the attacker gains a route into the target's internal network via the server's local SOCKS listener.

  Command Reference:

  	Listen Port: 8000

command: |
  chisel server -p 8000 --reverse
items:
  - Shell
OS:
  - Linux
phases:
  - Pivoting
references:
  - https://github.com/jpillora/chisel
  - https://book.hacktricks.xyz/generic-methodologies-and-resources/tunneling-and-port-forwarding
---
