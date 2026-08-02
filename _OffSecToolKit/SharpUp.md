---
description: |
  SharpUp.exe is part of the GhostPack suite of tools and is a C# port of PowerUp that will perform numerous privilege escalation checks. The following command will run all priv esc checks and store the output in a file.

  Command Reference:

  	Output File: output.txt

command: |
  SharpUp.exe > output.txt
items:
  - Shell
OS:
  - Windows
phases:
  - PrivEsc
references:
  - https://github.com/GhostPack/SharpUp
  - https://blog.harmj0y.net/redteaming/ghostpack/
---
