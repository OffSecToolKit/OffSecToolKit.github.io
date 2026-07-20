---
description: |
  Subfinder is a fast passive subdomain discovery tool from ProjectDiscovery that aggregates results from numerous online sources (certificate transparency logs, DNS databases, search engines, and third-party APIs) to build a list of valid subdomains for a target. It's designed for speed and reliability during recon and is commonly chained with other tools like httpx or nuclei for further enumeration.

  Command Reference:

  	Domain: test.local

  	Output file: subfinder_output.txt

command: |
  subfinder -d test.local -o subfinder_output.txt
items:
  - No_Creds
services:
  - DNS
OS:
  - Linux
phases:
  - Recon
references:
  - https://github.com/projectdiscovery/subfinder
---
