---
description: |
  Once TREVORspray's recon mode has resolved a tenant's OAuth token endpoint, the same tool sprays a single password across a list of harvested/guessed email addresses against that endpoint, threading requests and automatically tracking which combinations have already been tried so a spray can be paused and resumed without re-triggering lockouts. Built-in loot modules flag which accounts exist, are locked out, or have MFA enabled, straight from the authentication response.

  Attackers pair this with the recon command above: run `--recon` once to get the `token_endpoint` for the target tenant, then feed it here alongside a list of employee emails (harvested via theHarvester, LinkedIn scraping, etc.) and a single low-lockout-risk seasonal password.

  Command Reference:

  	Email List: emails.txt

  	Password: Summer2026!

  	Token Endpoint: https://login.windows.net/<tenant-id>/oauth2/token

command: |
  trevorspray.py -e emails.txt -p 'Summer2026!' --url https://login.windows.net/<tenant-id>/oauth2/token
items:
  - Username
services:
  - Azure
OS:
  - Linux
phases:
  - CredentialAccess
references:
  - https://github.com/blacklanternsecurity/TREVORspray
---
