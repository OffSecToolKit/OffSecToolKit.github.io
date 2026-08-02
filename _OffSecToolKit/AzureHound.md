---
description: |
  AzureHound is the official BloodHound data collector for Azure/Entra ID, written in Go by the BloodHound/SpecterOps team. It authenticates to Azure Resource Manager and Microsoft Graph/Azure AD APIs to enumerate the full tenant graph, users, groups, service principals, applications, managed identities, devices, and role assignments, then exports the data as JSON for ingestion into the BloodHound analysis engine.

  Attackers use AzureHound after obtaining valid Azure AD credentials to map privilege escalation and lateral movement paths across an Entra tenant, such as identifying which users can reset the password of a Global Administrator or take over an Azure Automation Account. The command below authenticates with a username and password and collects the entire tenant graph in a single pass.

  Command Reference:

  	Username: john@test.onmicrosoft.com

  	Password: password123

  	Tenant: test.onmicrosoft.com

command: |
  azurehound -u john@test.onmicrosoft.com -p password123 -t test.onmicrosoft.com list --output azurehound_output.json
items:
  - Username
  - Password
services:
  - Azure
OS:
  - Linux
  - Windows
phases:
  - Enumeration
references:
  - https://github.com/SpecterOps/AzureHound
  - https://bloodhound.specterops.io/collect-data/ce-collection/azurehound
---
