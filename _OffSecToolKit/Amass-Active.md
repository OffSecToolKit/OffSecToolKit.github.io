---
description: |
  OWASP Amass can also perform active subdomain enumeration, combining brute forcing, DNS zone walking, and reverse DNS sweeps against the target's own name servers alongside its usual passive data sources. This surfaces subdomains that never appear in public datasets, at the cost of directly querying (and being visible to) the target's DNS infrastructure, so it's typically run once passive recon has been exhausted.

  Command Reference:

  	Domain: test.local

  	Output file: amass_active.txt

command: |
  amass enum -active -d test.local -o amass_active.txt
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
