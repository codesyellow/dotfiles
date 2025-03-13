#!/usr/bin/env python
import psutil
import json
from config import get_pango

mem_usage = int(psutil.virtual_memory()[2])

classes = ["normal", "cpu"]
if mem_usage > 80:
    classes[0] = "warning"
output = f"{get_pango('RAM', mem_usage)}%"

print(json.dumps({
    "text": output,
    "tooltip": f"Updates: {mem_usage}",
    "class": classes
}))
