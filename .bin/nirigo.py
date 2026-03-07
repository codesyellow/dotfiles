#!/usr/bin/env python3
import subprocess
import json
import sys

def niri_json(cmd):
    try:
        result = subprocess.run(
            ["niri", "msg", "--json", cmd],
            capture_output=True, text=True, check=True
        )
        return json.loads(result.stdout)
    except Exception as e:
        sys.exit(1)

monitor_name = niri_json("focused-output")["name"]
windows = niri_json("windows")
workspaces = {ws["id"]: ws for ws in niri_json("workspaces")}

list_items = []
for win in windows:
    ws = workspaces.get(win["workspace_id"])
    if not ws or ws.get("name") == "scratch" or ws["output"] != monitor_name:
        continue
    
    line = f"{win['id']}  {win['title'][:40]}  {win['app_id']}"
    list_items.append(line)

input_str = "\n".join(list_items)

try:
    proc = subprocess.run(
        [
            "rofi", "-dmenu", 
            "-i", 
            "-p", "GoTo",
        ],
        input=input_str,
        text=True,
        capture_output=True
    )
    
    choice = proc.stdout.strip()

    if choice:
        selected_id = choice.split("")[0].strip()
        subprocess.run(["niri", "msg", "action", "focus-window", "--id", selected_id])

except FileNotFoundError:
    print("Err: install rofi-wayland.")
