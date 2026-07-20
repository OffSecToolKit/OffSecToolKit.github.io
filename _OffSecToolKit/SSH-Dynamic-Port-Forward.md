---
description: |
  When valid SSH credentials for a dual-homed target are obtained, native OpenSSH dynamic port forwarding (-D) can turn that SSH connection into a SOCKS proxy without needing to drop any additional tooling on disk. All traffic sent to the local SOCKS port is tunneled through the SSH session and egresses from the target, allowing the attacker to reach any internal hosts and services the SSH server can route to.

  Command Reference:

  	Target IP: 10.10.10.1

  	Username: john

  	Password: password123

  	Local SOCKS Port: 9050

command: |
  ssh -D 9050 john@10.10.10.1
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
