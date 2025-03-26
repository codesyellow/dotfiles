#!/usr/bin/env python
import json
import subprocess
from config import get_pango

try:
    updates_available = subprocess.check_output(
        "checkupdates"
    ).decode("utf-8").count("\n")
except subprocess.CalledProcessError:
    pass
else:
    classes = ["normal", "updates"]
    if updates_available > 20:
        classes[0] = "warning"
    output = f"{get_pango('UPD', updates_available)}"

    print(json.dumps({
        "text": output,
        "tooltip": f"Updates: {updates_available}",
        "class": classes
    }))
