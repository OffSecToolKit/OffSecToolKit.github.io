---
description: |
  TREVORspray is a modular password-spraying toolkit from Black Lantern Security purpose-built for Microsoft 365/Azure, Okta, and OWA. Before spraying a single password, its `--recon` mode queries Microsoft's own tenant-discovery endpoints (autodiscover, OpenID config, MX records) for a target domain to confirm it's actually backed by Azure AD/Entra ID, enumerate any federated identity providers, and — critically — resolve the tenant's OAuth `token_endpoint`, which is required to target the spray correctly in the next step.

  Attackers run this recon pass first and for free: it requires no credentials, generates no failed-login telemetry, and often reveals whether the target's real Azure tenant belongs to a parent company (common after M&A), which changes what domain the actual spray needs to target.

  Command Reference:

  	Target Domain: test.local

command: |
  trevorspray.py --recon test.local
items:
  - No_Creds
services:
  - Azure
OS:
  - Linux
phases:
  - Recon
references:
  - https://github.com/blacklanternsecurity/TREVORspray
---
