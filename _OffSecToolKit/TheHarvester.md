---
description: |
  theHarvester is an OSINT reconnaissance tool that gathers emails, subdomains, hostnames, employee names, open ports, and banners for a target domain by querying public sources such as search engines, PGP key servers, and certificate transparency logs. It's used at the very start of an engagement to build a picture of an organization's external footprint without ever touching the target infrastructure directly. The following command queries all supported passive sources for a domain and saves the results to a file.

  Command Reference:

  	Domain: test.local

  	Data Source(s): all

  	Output file: theharvester_output

command: |
  theHarvester -d test.local -b all -f theharvester_output
items:
  - No_Creds
services:
  - DNS
OS:
  - Linux
phases:
  - Recon
references:
  - https://github.com/laramies/theHarvester
---
