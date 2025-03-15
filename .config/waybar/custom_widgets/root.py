#!/usr/bin/env python
import json
import shutil
from config import get_pango

total, used, free = shutil.disk_usage(f"/")
total_free = free // (2**30)

classes = ["normal", "root"]
if total_free < 20:
    classes[0] = "warning"
output = f"{get_pango('RFS', total_free)}G"

print(json.dumps({
    "text": output,
    "tooltip": f"Updates: {total_free}",
    "class": classes
}))
