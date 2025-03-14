#!/usr/bin/env python
import json
import os
from config import get_pango

classes = ["normal", "gameon"]
text = "OFF"
if os.path.exists("/tmp/gameon"):
    classes[0] = "warning"
    text = "ON"
output = f"{get_pango('PLY', text)}"

print(json.dumps({
    "text": output,
    "tooltip": f"Updates: {text}",
    "class": classes
}))
