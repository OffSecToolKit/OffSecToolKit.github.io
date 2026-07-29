---
description: |
  kubeletctl is a CyberArk-developed client for the kubelet API (default port 10250/TCP), the same API kube-hunter flags as exposed. Many clusters leave the kubelet's `/run` and `/exec` endpoints reachable with anonymous authentication enabled, which lets anyone who can reach the port execute commands inside any pod scheduled on that node without ever touching the Kubernetes API server or presenting a service account token.

  Attackers first scan a CIDR range for kubelets vulnerable to this unauthenticated RCE, then use the returned pod/container names to run commands directly inside a chosen container. The commands below scan a subnet for the vulnerability, then execute `id` inside a discovered pod's container.

  Command Reference:

  	Target CIDR: 10.10.10.0/24

  	Target IP: 10.10.10.1

  	Pod Name: nginx-pod

  	Container Name: nginx

command: |
  kubeletctl scan rce --cidr 10.10.10.0/24
  kubeletctl exec "id" -s 10.10.10.1 -p nginx-pod -c nginx
items:
  - No_Creds
services:
  - Kubernetes
OS:
  - Linux
phases:
  - Exploitation
references:
  - https://github.com/cyberark/kubeletctl
  - https://www.cyberark.com/resources/threat-research-blog/using-kubelet-client-to-attack-the-kubernetes-cluster
---
