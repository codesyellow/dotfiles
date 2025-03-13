#!/usr/bin/env python
import psutil
import json
from config import get_pango

cpu_usage = int(psutil.cpu_percent(interval=2))

classes = ["normal", "cpu"]
if cpu_usage > 80:
    classes[0] = "warning"
output = f"{get_pango('CPU', cpu_usage)}%"

print(json.dumps({
    "text": output,
    "tooltip": f"Updates: {cpu_usage}",
    "class": classes
}))
