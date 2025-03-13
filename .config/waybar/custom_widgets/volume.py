#!/usr/bin/env python
import json
import subprocess
from config import get_pango

volume = int(subprocess.check_output([
    "pamixer",
    "--get-volume"
]).decode("utf-8"))

classes = ["normal", "volume"]
if volume > 40:
    classes[0] = "warning"
output = f"{get_pango('VOL', volume)}%"

print(json.dumps({
    "text": output,
    "tooltip": f"Updates: {volume}",
    "class": classes
}))
