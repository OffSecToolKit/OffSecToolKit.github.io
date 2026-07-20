---
description: |
  OWASP Amass performs in-depth attack surface mapping and asset discovery for a target domain. Passive enumeration mode gathers subdomains solely from external sources — certificate transparency logs, DNS aggregators, scraping, and other third-party datasets — without sending any traffic to the target's own name servers. This makes it an ideal first step for stealthy recon since it produces zero footprint on the target's infrastructure.

  Command Reference:

  	Domain: test.local

  	Output file: amass_passive.txt

command: |
  amass enum -passive -d test.local -o amass_passive.txt
items:
  - No_Creds
services:
  - DNS
OS:
  - Linux
phases:
  - Recon
references:
  - https://github.com/owasp-amass/amass
---
