---
description: |
  Pacu is an open-source AWS exploitation framework built by Rhino Security Labs, purpose-built for offensive security testing against Amazon Web Services environments. It manages sessions of imported AWS credentials and ships with dozens of modules to enumerate, escalate privileges within, and exploit misconfigured AWS accounts. Attackers use Pacu after obtaining a set of AWS access keys (e.g. from a leaked .env file, EC2 instance metadata, a public Git repo, or phishing) to quickly determine what the compromised credentials are capable of and to discover exposed resources such as S3 buckets.

  The example below imports a stolen key pair into a new Pacu session, runs the iam__enum_permissions module to determine the effective permissions of the compromised identity, then runs s3__bucket_finder to discover accessible S3 buckets.

  Command Reference:

  	AWS Access Key ID: AKIAIOSFODNN7EXAMPLE

  	AWS Secret Key: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY

  	Session Name: pentest

command: |
  $ pacu
  Pacu (new_session)> import_keys --access-key AKIAIOSFODNN7EXAMPLE --secret-key wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY --name pentest
  Pacu (pentest)> run iam__enum_permissions
  Pacu (pentest)> run s3__bucket_finder
items:
  - API_Key
services:
  - AWS
OS:
  - Linux
phases:
  - Enumeration
references:
  - https://github.com/RhinoSecurityLabs/pacu
  - https://rhinosecuritylabs.com/pacu/
---
