---
description: |
  socat can be used on a pivot host to relay TCP connections from the attacker into an internal segment that the pivot can reach but the attacker cannot reach directly. Running socat with TCP-LISTEN,fork on the pivot host binds a listener that forks a new relay for each connection and forwards traffic to the internal target, effectively turning the pivot into a transparent port forwarder without any SOCKS or SSH tunneling involved.

  Command Reference:

  	Internal Target IP: 10.10.20.5

  	Relay Listen Port: 4444

  	Internal Target Port: 4444

command: |
  socat TCP-LISTEN:4444,fork TCP:10.10.20.5:4444
items:
  - Shell
OS:
  - Linux
phases:
  - Pivoting
references:
  - http://www.dest-unreach.org/socat/
  - https://book.hacktricks.xyz/generic-methodologies-and-resources/tunneling-and-port-forwarding
---
