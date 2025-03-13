#!/usr/bin/env python
import json
import os
from config import get_pango

HOME = os.path.expanduser("~")
POMODORO = "/tmp/pomo_timer"
POMOPAUSE = "/tmp/pomo_pause"

classes = ["normal", "pomo"]
text = "0:00:00"
if os.path.exists(POMODORO):
    with open(POMODORO, "r") as pomodoro:
        text = pomodoro.read().strip()
        if os.path.exists(POMOPAUSE):
            classes[0] = "warning"

output = f"{get_pango('POMO', text)}"

print(json.dumps({
    "text": output,
    "tooltip": f"Updates: {output}",
    "class": classes
}))
