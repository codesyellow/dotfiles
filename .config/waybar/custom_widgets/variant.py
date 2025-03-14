#!/usr/bin/env python
import json
import subprocess
from config import get_pango

keyboard_layout = subprocess.check_output(
    'swaymsg -t get_inputs | jq \'map(select(has("xkb_active_layout_name")))[0].xkb_active_layout_name\'',
    shell=True
).decode("utf-8").strip()

classes = ["normal", "variant"]
text = "US"
if "intl" in keyboard_layout:
    classes[0] = "warning"
    text = "INTL"
output = f"{get_pango('EN', text)}"

print(json.dumps({
    "text": output,
    "tooltip": f"Updates: {output}",
    "class": classes
}))
