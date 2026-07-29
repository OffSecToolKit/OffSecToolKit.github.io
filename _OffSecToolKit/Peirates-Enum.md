---
description: |
  Peirates is a Kubernetes penetration testing tool from InGuardians focused on privilege escalation and lateral movement once you have any form of code execution inside a cluster. Run from a shell inside a compromised pod, it automatically picks up the pod's mounted service account token and presents an interactive menu of attacks: listing and switching between every service account token and secret it can reach, querying the Kubernetes API and cloud metadata API, escaping to the underlying node, and using each newly stolen token to pivot into other namespaces.

  Attackers drop the peirates binary into a shell obtained on a pod (e.g. via a vulnerable web app or RCE) and run it directly, no additional credentials are required since it inherits whatever the pod's service account is already allowed to do.

  Command Reference:

  	(none - run from an existing pod shell)

command: |
  ./peirates
items:
  - Shell
services:
  - Kubernetes
OS:
  - Linux
phases:
  - PrivEsc
references:
  - https://github.com/inguardians/peirates
  - https://www.inguardians.com/peirates/
---
