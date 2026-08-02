---
description: |
  WPScan is a black-box WordPress vulnerability scanner that fingerprints the WordPress core version, installed plugins, and themes, and cross-references them against a vulnerability database. The following command enumerates usernames, vulnerable plugins, and vulnerable themes on a target site without requiring any credentials.

  Command Reference:

  	Target URL: http://10.10.10.1/

command: |
  wpscan --url http://10.10.10.1/ --enumerate u,vp,vt --random-user-agent
items:
  - No_Creds
services:
  - Web
OS:
  - Linux
phases:
  - Enumeration
references:
  - https://github.com/wpscanteam/wpscan
  - https://github.com/wpscanteam/wpscan/wiki/WPScan-User-Documentation
---
