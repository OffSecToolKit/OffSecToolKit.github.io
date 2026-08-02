---
description: |
  SafetyKatz.exe is part of the GhostPack suite of tools and is a combination of SharpDump and Mimikatz. The following command will dump the LSASS process and run Mimikatz to extract credentials from the dumped process.

command: |
  SafetyKatz.exe
items:
  - Shell
OS:
  - Windows
phases:
  - PrivEsc
  - Enumeration
references:
  - https://github.com/GhostPack/SafetyKatz
  - https://blog.harmj0y.net/redteaming/ghostpack/
---
