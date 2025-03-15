#!/usr/bin/env python
import json
import os
from config import get_pango

HOME = os.path.expanduser("~")
EASYEFFECTS_PRESET_PATH = f"{HOME}/.config/easyeffects_preset"

classes = ["normal", "easy"]
text = "EQ"
if os.path.exists(EASYEFFECTS_PRESET_PATH):
    with open(EASYEFFECTS_PRESET_PATH, "r") as easy_preset:
        if easy_preset.read().strip() != "LoudnessEqualizer":
            classes[0] = "warning"
            text = "MUS"
        else:
            text = "EQ"

output = f"{get_pango('DSP', text)}"

print(json.dumps({
    "text": output,
    "tooltip": f"Updates: {output}",
    "class": classes
}))
