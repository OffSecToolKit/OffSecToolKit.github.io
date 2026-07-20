---
description: |
  cloud_enum is an unauthenticated, keyword-based OSINT tool that enumerates publicly accessible resources across AWS, Azure, and GCP simultaneously, including S3 buckets, Azure Blob Storage/App Services/Container instances, and GCP Storage buckets/Firebase/App Engine apps. It works by generating permutations of a target company name or keyword against each provider's naming conventions, then uses DNS and HTTP fingerprinting to identify which resources exist and whether they are publicly readable.

  Attackers use cloud_enum early in an engagement, before any credentials are obtained, to passively map an organization's cloud footprint and discover misconfigured public storage that may leak sensitive data. The command below enumerates resources across all three cloud providers using the keyword "testcompany".

  Command Reference:

  	Keyword: testcompany

command: |
  python3 cloud_enum.py -k testcompany
items:
  - No_Creds
services:
  - AWS
  - Azure
  - GCP
OS:
  - Linux
phases:
  - Recon
references:
  - https://github.com/initstring/cloud_enum
---
