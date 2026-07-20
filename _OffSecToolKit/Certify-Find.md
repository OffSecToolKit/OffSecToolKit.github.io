---
description: |
  Certify is a .NET offensive tool for enumerating and abusing Active Directory Certificate Services (ADCS) from a Windows host. The `find /vulnerable` module enumerates all Certificate Authorities and certificate templates reachable by the current user's context and highlights those with dangerous configurations (e.g. ESC1-style templates with enrollee-supplied SAN and client authentication EKU, or overly permissive enrollment/write ACLs). This is typically run from a shell on a domain-joined Windows host to find a path to privilege escalation via ADCS.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	Username: john

  	Password: password123

command: |
  Certify.exe find /vulnerable
items:
  - Shell
services:
  - ADCS
OS:
  - Windows
phases:
  - Enumeration
references:
  - https://github.com/GhostPack/Certify
  - https://posts.specterops.io/certified-pre-owned-d95910965cd2
---
