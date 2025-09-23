#!/usr/bin/env python3
import subprocess
import json

def niri_json(cmd):
    result = subprocess.run(
        ["niri", "msg", "--json", cmd],
        capture_output=True,
        text=True,
        check=True
    )
    return json.loads(result.stdout)

monitor_name = niri_json("focused-output")["name"]
windows = niri_json("windows")
workspaces = niri_json("workspaces")
list_names=""
list_info=[]

for win in windows:
    win_id = win["id"]
    title = win["title"]
    app_id = win["app_id"]
    ws_id = win["workspace_id"]

    output = next(
        (ws["output"] for ws in workspaces if ws["id"] == ws_id),
        None
    )

    if output == monitor_name:
        list_names+=f"{win_id} | {title}\n"
        list_info.append({
            "id":win_id,
            "title":title,
            "app_id":app_id,
        })

result = subprocess.run(
    ["wmenu", "-f", "Martian Mono Nerd Font 15",  "-N", "#272E33", "-n", "#D3C6AA", "-S", "#272E33", "-s", "#E69875", "-i", "-l", "5", "-p", "GoTo"],
    input=list_names,
    text=True,
    capture_output=True
)

choice = result.stdout.strip()

if len(choice) > 0:
    selected_id=choice.split("|")[0].strip()
    print(selected_id)
    subprocess.run([
        "niri", "msg","action",  "focus-window", "--id", f"{selected_id}"
    ])

