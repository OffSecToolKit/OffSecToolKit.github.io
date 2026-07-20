---
description: |
  Ligolo-ng is a lightweight, fast reverse tunneling tool that creates a TUN interface on the attacker host to route traffic to a compromised network, avoiding the need to run per-port SOCKS proxies. The proxy component runs on the attacker box and listens for incoming agent connections, presenting an interactive console used to add routes and start the tunnel to the connecting agent. The -selfcert flag generates a self-signed certificate on the fly so the agent's TLS connection succeeds without needing a pre-issued certificate.

  Command Reference:

  	Listen Port: 11601

command: |
  proxy -selfcert
items:
  - Shell
OS:
  - Linux
phases:
  - Pivoting
references:
  - https://github.com/nicocha30/ligolo-ng
---
