---
description: |
  GraphRunner is a PowerShell post-exploitation toolset for interacting with the Microsoft Graph API against a compromised Microsoft Entra ID (Azure AD) identity. Unlike AzureHound or ROADrecon, which authenticate with a username/password, GraphRunner is built around working directly from a stolen or phished OAuth access/refresh token, and ships modules to enumerate tenant/user settings, dump app registrations and OAuth consent grants, and pillage Outlook, SharePoint, OneDrive, and Teams data once authenticated.

  Attackers load the module after obtaining any valid Graph token (device-code phishing, a stolen refresh token, an over-permissioned app registration, etc.), authenticate through it, then run its recon module to map out the tenant before deciding where to pillage next.

  Command Reference:

  	(none - authenticates interactively via device code)

command: |
  Import-Module .\GraphRunner.ps1
  Get-GraphTokens
  Invoke-GraphRecon
items:
  - API_Key
services:
  - Azure
OS:
  - Windows
phases:
  - Enumeration
references:
  - https://github.com/dafthack/GraphRunner
---
