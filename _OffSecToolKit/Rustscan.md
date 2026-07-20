---
description: |
  RustScan is a fast initial port scanner that leverages asynchronous scanning to identify open ports across a target in seconds, then automatically pipes the results into Nmap to run service/version detection and default scripts against just those open ports. This two-stage approach gives the speed of a raw scanner with the depth of Nmap's service fingerprinting, without wasting time running Nmap's full scripts against all 65535 ports.

  Command Reference:

  	Target IP: 10.10.10.1

  	Nmap Args: -sV -sC

command: |
  rustscan -a 10.10.10.1 -- -sV -sC
items:
  - No_Creds
OS:
  - Linux
phases:
  - Recon
references:
  - https://github.com/RustScan/RustScan
---
