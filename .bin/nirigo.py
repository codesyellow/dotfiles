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

rofi_theme = f"""
* {{
    font: "Victor Mono Bold Italic 14";
    bg: #272E33;
    fg: #D3C6AA;
    accent: #E69875;
    background-color: @bg;
    text-color: @fg;
}}
window {{
    width: 35%;
    border: 2px;
    border-color: @accent;
    background-color: @bg;
}}
mainbox {{
    children: [ inputbar, listview ];
}}
inputbar {{
    children: [ prompt, entry ];
    background-color: @bg;
}}
prompt {{
    background-color: @accent;
    text-color: @bg;
    padding: 4px 10px;
}}
entry {{
    padding: 4px;
    text-color: @fg;
    placeholder: "Search...";
}}
listview {{
    lines: 8;
    scrollbar: false;
}}
element {{
    padding: 4px;
}}
element selected {{
    background-color: @accent;
    text-color: @bg;
}}
"""

# --- 3. Execução ---
try:
    proc = subprocess.run(
        [
            "rofi", "-dmenu", 
            "-i", 
            "-p", "GoTo",
            "-theme-str", rofi_theme
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
    print("Erro: Instale o rofi-wayland.")
