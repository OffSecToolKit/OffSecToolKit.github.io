---
description: |
  ROADrecon is the reconnaissance component of ROADtools, a framework for exploring and enumerating Azure Active Directory/Entra ID environments. It authenticates as a user (or service principal) and builds a local SQLite dump of the tenant's directory objects, including users, groups, devices, applications, service principals, and Conditional Access policies, which can then be browsed through ROADrecon's built-in web interface or queried directly to find privilege escalation opportunities.

  Attackers use ROADrecon after obtaining Azure AD credentials (e.g. via password spraying or an illicit consent grant) to build a complete offline picture of the tenant without needing repeated live API calls. The commands below authenticate with a username and password, then gather the full directory dump.

  Command Reference:

  	Username: john@test.onmicrosoft.com

  	Password: password123

  	Tenant/Domain: test.onmicrosoft.com

command: |
  roadrecon auth -u john@test.onmicrosoft.com -p password123 --tenant test.onmicrosoft.com
  roadrecon gather
items:
  - Username
  - Password
services:
  - Azure
OS:
  - Linux
phases:
  - Enumeration
references:
  - https://github.com/dirkjanm/ROADtools
  - https://github.com/dirkjanm/ROADtools/wiki/Getting-started-with-ROADrecon
---
