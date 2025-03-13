#!/usr/bin/env python
import json
from datetime import datetime
from config import get_pango

now = datetime.now()
formatted_time = now.strftime("%H:%M %d %a")

classes = ["normal", "time"]
output = f"{get_pango('TIME', formatted_time)}"

print(json.dumps({
    "text": output,
    "tooltip": f"Updates: {formatted_time}",
    "class": classes
}))
