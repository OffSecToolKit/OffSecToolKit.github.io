---
description: |
  Local port forwarding (-L) uses an SSH connection to a foothold host to expose a single internal-only service on the attacker's own loopback interface, without needing a full SOCKS proxy. This is useful when only one specific port on an internal host needs to be reached, such as RDP on a machine that is not directly routable from the attacker's position.

  Command Reference:

  	Target IP: 10.10.10.1

  	Internal Target IP: 10.10.20.5

  	Username: john

  	Password: password123

  	Remote Service Port: 3389

command: |
  ssh -L 3389:10.10.20.5:3389 john@10.10.10.1
items:
  - Username
  - Password
services:
  - SSH
OS:
  - Linux
phases:
  - Pivoting
references:
  - https://man.openbsd.org/ssh
  - https://book.hacktricks.xyz/generic-methodologies-and-resources/tunneling-and-port-forwarding
---
