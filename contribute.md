---
layout: page
title: Contribute
---

## Structure

Each ostk Command is defined in a file in the [`_OffSecToolKit/`] folder named as `<tool name>.md`, such file consists only of a [YAML] front matter which describes the command and its attributes.

The full syntax is the following:

```
---
description: Description of what the command does.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	Username: john

  	Password: password123

command: |
  put command here
items:
  - ITEM
  - ITEM
  ...
services:
  - SERVICE
  ...
OS:
  - OS
  ...
phases:
  - PHASE
references:
  - LINK
  - LINK
  ...
---
```

Where `ITEM` is one of the values described in the [`_data/items.yml`] file, `SERVICE` is one of the values described in the [`_data/services.yml`] file, `OS` is one of the values described in the [`_data/OS.yml`] file, `PHASE` is one of the values described in the [`_data/phases.yml`] file, and `LINK` is a link to download the related tool for that command as well as links to any other relevant information about what the command is doing. 

Feel free to use any file in the [`_OffSecToolKit/`] folder as an example.

## Pull request process

I accept commands that run on either Linux or Windows, just as long as they target Windows machines (this is a Windows/AD cheat sheet after all). 

Before sending a pull request of a new command, ensure the following:

1. Verify the EXACT command works against at least one version of Windows.
2. Any parts of the command that need context should go in the 'Command References', such as username, password, target IP, domain, etc. For consistency, if your command uses a username, password, domain, and/or target IP, use `john`, `password123`, `test.local` and `10.10.10.1` respectively.
3. Include the proper filters related to your command. This currently means including any and all remote services required to be running on the Windows machine in order for the command to work, the Operating System the command can be run from, and the phase of attack. For example, Impacket's smbclient.py requires the SMB service to be running on the remote Windows machine, so SMB would be one of the services included. And since it can be run from any OS, Linux and Windows would be the OS that's included. Finally, the Phase is Exploitation because you are getting a remote shell.
4. Add a minimum, a link to download the related tool MUST be provided and added under `references`.

Pull requests adding new items in [`_data/items.yml`], services in [`_data/services.yml`], OS in [`_data/OS.yml`], or phases in [`_data/phases.yml`] are allowed and subjected to project maintainers vetting.

[YAML]: http://yaml.org/
[`_OffSecToolKit/`]: https://github.com/OffSecToolKit/OffSecToolKit.github.io/tree/main/_OffSecToolKit
[`_data/services.yml`]: https://github.com/OffSecToolKit/OffSecToolKit.github.io/blob/main/_data/services.yml
[`_data/items.yml`]: https://github.com/OffSecToolKit/OffSecToolKit.github.io/blob/main/_data/items.yml
[`_data/OS.yml`]: https://github.com/OffSecToolKit/OffSecToolKit.github.io/blob/main/_data/OS.yml
[`_data/phases.yml`]: https://github.com/OffSecToolKit/OffSecToolKit.github.io/blob/main/_data/phases.yml
