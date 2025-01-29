#!/usr/bin/env python
from libqtile.command.client import InteractiveCommandClient

# Connect to the running Qtile instance
c = InteractiveCommandClient()

print(dir(c))
