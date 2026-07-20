---
description: |
  ScoutSuite also supports auditing Azure/Entra ID tenants, pulling configuration data via the Azure Resource Manager and Microsoft Graph APIs to flag issues such as overly permissive role assignments, storage accounts open to the internet, and disabled logging/monitoring. When an engagement provides an already-authenticated Azure CLI session (e.g. via `az login` with a compromised or client-provided service principal), ScoutSuite can reuse that session directly instead of requiring separate credentials, making it a fast first step for Azure cloud engagements.

  The command below runs a full Azure audit by authenticating through the local Azure CLI session.

  Command Reference:

  	Azure CLI: authenticated session (az login already completed)

command: |
  scout azure --cli
items:
  - API_Key
services:
  - Azure
OS:
  - Linux
phases:
  - Enumeration
references:
  - https://github.com/nccgroup/ScoutSuite
---
