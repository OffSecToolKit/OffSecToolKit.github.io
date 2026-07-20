---
description: |
  Certipy is a Python-based offensive tool for Active Directory Certificate Services (ADCS) enumeration and abuse. The `find` command with `-vulnerable` enumerates all Certificate Authorities and certificate templates in the domain and automatically flags misconfigurations matching known ESC1-ESC8 attack paths (e.g. templates allowing SAN specification with client authentication EKU, weak enrollment ACLs, or vulnerable CA settings). This is the first step in any ADCS attack chain, used to identify which template/CA to target.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	Username: john

  	Password: password123

command: |
  certipy find -u john@test.local -p password123 -dc-ip 10.10.10.1 -vulnerable -stdout
items:
  - Username
  - Password
services:
  - ADCS
OS:
  - Linux
phases:
  - Enumeration
references:
  - https://github.com/ly4k/Certipy
  - https://posts.specterops.io/certified-pre-owned-d95910965cd2
---
