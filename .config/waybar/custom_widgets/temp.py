#!/usr/bin/env python
import json
import psutil
from config import get_pango

temperature = int(psutil.sensors_temperatures()["coretemp"][0][1])

classes = ["normal", "temp"]
if temperature > 80:
    classes[0] = "warning"
output = f"{get_pango('TMP', temperature)}°C"

print(json.dumps({
    "text": output,
    "tooltip": f"Updates: {temperature}",
    "class": classes
}))
