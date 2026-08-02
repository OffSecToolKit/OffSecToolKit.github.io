---
description: |
  CeWL is a custom wordlist generator that spiders a target website, collecting unique words from its pages to build a wordlist tailored to that organization or individual. The following command crawls the target site up to a depth of 2 links, keeps words of at least 5 characters, and writes the results to a wordlist file, producing a targeted wordlist that can later be fed into tools such as Hydra, John the Ripper, or Hashcat for higher-yield password cracking than generic lists like rockyou.txt.

  Command Reference:

  	Target IP: 10.10.10.1

  	Crawl Depth: 2

  	Minimum Word Length: 5

  	Output File: wordlist.txt

command: |
  cewl http://10.10.10.1 -d 2 -m 5 -w wordlist.txt
items:
  - No_Creds
  - Wordlist
services:
  - Web
OS:
  - Linux
phases:
  - Recon
references:
  - https://github.com/digininja/CeWL
  - https://www.kali.org/tools/cewl/
---
