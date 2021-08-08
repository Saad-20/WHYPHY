#!/usr/bin/env python3

import subprocess 

commands = subprocess.check_output(['netsh','wlan','show','profiles'])

data = commands.decode('utf-8',errors = "backslashreplace")

data = data.split('\n'))
