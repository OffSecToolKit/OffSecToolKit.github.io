---
description: |
  nuclei is a fast, template-based vulnerability scanner that sends requests crafted from a large community-maintained library of YAML templates covering known CVEs, misconfigurations, exposed panels, and default credentials. The following command runs nuclei against a target URL using only the CVE templates filtered to critical and high severity findings, quickly surfacing known exploitable vulnerabilities.

  Command Reference:

  	Target URL: http://10.10.10.1/

command: |
  nuclei -u http://10.10.10.1/ -t cves/ -severity critical,high -o output.txt
items:
  - No_Creds
services:
  - Web
OS:
  - Linux
phases:
  - Enumeration
references:
  - https://github.com/projectdiscovery/nuclei
  - https://github.com/projectdiscovery/nuclei-templates
---
