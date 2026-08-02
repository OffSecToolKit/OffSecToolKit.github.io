---
description: |
  ScoutSuite also audits Google Cloud Platform projects, pulling configuration data via GCP's native APIs to flag issues such as overly permissive IAM bindings, publicly readable Storage buckets, and firewall rules open to the internet, the same way it does for AWS and Azure. Given a service account key with Viewer/Security Reviewer permissions, it can assess a single project, an entire folder, or every project an identity can see.

  The command below runs a full GCP audit of a specific project using a service account key file, a common starting point when an engagement or compromised CI pipeline hands over GCP service account credentials.

  Command Reference:

  	Service Account Key File: key.json

  	Project ID: test-project-id

command: |
  scout gcp --service-account key.json --project-id test-project-id
items:
  - API_Key
services:
  - GCP
OS:
  - Linux
phases:
  - Enumeration
references:
  - https://github.com/nccgroup/ScoutSuite
---
