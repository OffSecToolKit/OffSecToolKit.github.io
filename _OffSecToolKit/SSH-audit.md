---
description: |
  The Secure Shell (SSH) protocol is a method for securely sending commands to a computer over an unsecured network. ssh-audit is a tool for ssh server & client configuration auditing. The following command performs a remote security audit against the target SSH service.

  Command Reference:

      Target: 10.10.10.1

command: |
  ssh-audit.py 10.10.10.1
items:
  - No_Creds
services:
  - SSH
OS:
  - Linux
  - Windows
phases:
  - Enumeration
references:
  - https://github.com/jtesta/ssh-audit/
  - https://pypi.org/project/ssh-audit/
---
