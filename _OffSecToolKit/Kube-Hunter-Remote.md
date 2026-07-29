---
description: |
  kube-hunter is an open-source Kubernetes penetration testing tool from Aqua Security that hunts for security weaknesses in a cluster, such as an exposed API server, anonymous authentication enabled on the kubelet API, open dashboards, or vulnerable add-ons. It maps discovered services against the Kubernetes ATT&CK matrix and reports specific exploitable vulnerabilities rather than just open ports.

  Attackers run kube-hunter in remote mode against a target IP or hostname before gaining any foothold in the cluster, to get an attacker's-eye view of what's exposed externally. The command below scans a single target node for the Kubernetes API server, kubelet API, and any other cluster services reachable from outside.

  Command Reference:

  	Target IP: 10.10.10.1

command: |
  kube-hunter --remote 10.10.10.1
items:
  - No_Creds
services:
  - Kubernetes
OS:
  - Linux
phases:
  - Recon
references:
  - https://github.com/aquasecurity/kube-hunter
  - https://aquasecurity.github.io/kube-hunter/
---
