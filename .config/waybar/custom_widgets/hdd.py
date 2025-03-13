#!/usr/bin/env python
import json
import shutil
import os
from config import get_pango
HOME = os.path.expanduser("~")

total, used, free = shutil.disk_usage(f"{HOME}/.HDD")
total_free = free // (2**30)

classes = ["normal", "HDD"]
if total_free < 20:
    classes[0] = "warning"
output = f"{get_pango('HDD', total_free)}G"

print(json.dumps({
    "text": output,
    "tooltip": f"Updates: {total_free}",
    "class": classes
}))
