---
description: |
  WhatWeb identifies websites. The following command identifies the technology powering a web page.

  Command Reference:

      Aggressive level: 3

      Target: https://www.facebook.com

command: |
  whatweb -a 3 https://www.facebook.com -v
items:
  - No_Creds
services:
  - Web
OS:
  - Linux
  - Windows
phases:
  - Enumeration
references:
  - https://github.com/urbanadventurer/WhatWeb/wiki
---
