---
description: |
  After obtaining a PFX certificate impersonating a privileged account (e.g. via an ESC1 template abuse), Certipy's `auth` command uses the certificate to authenticate to the domain via PKINIT/Kerberos. Certipy requests a TGT for the certificate's subject and, because the KDC returns the NTLM hash in the PAC when using UnPAC-the-hash (U-Hash), retrieves the victim's NTLM hash directly without needing to crack anything, enabling immediate pass-the-hash or further ticket abuse.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	PFX file: administrator.pfx

command: |
  certipy auth -pfx administrator.pfx -dc-ip 10.10.10.1 -domain test.local
items:
  - PFX
services:
  - ADCS
OS:
  - Linux
phases:
  - Exploitation
references:
  - https://github.com/ly4k/Certipy
  - https://posts.specterops.io/certified-pre-owned-d95910965cd2
---
