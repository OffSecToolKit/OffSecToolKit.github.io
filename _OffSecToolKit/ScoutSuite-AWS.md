---
description: |
  ScoutSuite is an open-source multi-cloud security auditing tool developed by NCC Group that assesses the security posture of AWS, Azure, and GCP environments by collecting configuration data through each provider's native APIs. It aggregates the results into a single browsable HTML report, making it easy to spot misconfigured IAM policies, publicly exposed storage, weak logging, and other common cloud security weaknesses.

  Pentesters run ScoutSuite against a target AWS account once they have valid credentials configured locally, using it as a fast way to triage an environment's overall security posture before diving into manual enumeration or exploitation with tools like Pacu. The command below runs a full AWS audit using a pre-configured local AWS CLI profile.

  Command Reference:

  	AWS CLI Profile: pentest

command: |
  scout aws --profile pentest
items:
  - API_Key
services:
  - AWS
OS:
  - Linux
phases:
  - Enumeration
references:
  - https://github.com/nccgroup/ScoutSuite
---
