#!/usr/bin/env python
import os
import subprocess
import json
HOME = os.path.expanduser("~/")

windows_info = json.loads(subprocess.check_output([
    "hyprctl", "clients", "-j"
]).decode("utf-8"))

current_workspace_info = json.loads(subprocess.check_output(
    ["hyprctl", "activeworkspace", "-j"]).decode("utf-8"))

focused_window = json.loads(subprocess.check_output(
    [
        "hyprctl", "activewindow", "-j"
    ]
).decode("utf-8"))

focused_window_name = current_workspace_info["lastwindowtitle"].strip()
total_number_of_windows = current_workspace_info["windows"]
current_workspace_id = current_workspace_info["id"]

window_to_display = []

for window in windows_info:
    if window["workspace"]["id"] == current_workspace_id and window["pid"] != focused_window["pid"]:
        if len(window["class"].split(".")) == 3:
            window_to_display.append(window["class"].split(".")[2].title())
        else:
            window_to_display.append(window["class"].split(".")[0].title())

for window in window_to_display:
    if len(window.split(".")) == 3:
        print(window.split(".")[2])

if total_number_of_windows > 1:
    output = f"<span rise='3000'></span> <span rise='2000'>{total_number_of_windows}: {" - ".join(
        window_to_display)}</span><span size='15000' foreground='#4c566a'> | </span>"
    obj = {
        "text": output,
        "tooltip": "tablayout",
        "class": "normal"
    }
    print(json.dumps(obj))
