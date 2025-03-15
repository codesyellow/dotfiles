#!/usr/bin/env python
import subprocess
import json
import sys
import os

CURRENT_DESKTOP = os.environ["XDG_CURRENT_DESKTOP"]
ACTIVE_WINDOW = None
ACTIVE_WORKSPACE = None

if CURRENT_DESKTOP == "Hyprland":
    ACTIVE_WINDOW = json.loads(subprocess.check_output([
        "hyprctl",
        "activewindow",
        "-j"
    ]))

    ACTIVE_WORKSPACE = json.loads(subprocess.check_output([
        "hyprctl",
        "activeworkspace",
        "-j"
    ]))
elif CURRENT_DESKTOP.lower() == "sway":
    ACTIVE_WINDOW = json.loads(subprocess.check_output([
        "swaymsg", "-t", "get_tree", "|", "jq", '.. | select(.focused? == true)'
    ]))

    ACTIVE_WORKSPACE = json.loads(subprocess.check_output([
        "swaymsg", "-t", "get_workspaces", "|", "jq", "-r", '.[] | select(.focused) | .name'
    ]))


def hypr(wks):
    subprocess.run([
        "hyprctl", "dispatch", "moveoutofgroup",
    ])
    subprocess.run([
        "hyprctl", "dispatch", "movetoworkspace", f"{wks}"
    ])


print(ACTIVE_WORKSPACE, ACTIVE_WINDOW)


def move_to_wks(wks):
    if CURRENT_DESKTOP == "Hyprland":
        hypr(wks)


def set_to_wks(window, workspace):
    rule = f"windowrulev2 = workspace {
        workspace} silent,class:^({window["class"]})$"
    sway_rule = f"for_window [class='{window}$'] move to workspace 6"
    with open("/home/digo/.config/hypr/configs/rules.conf", mode="a") as data:
        data.write(f"\n{rule}")


try:
    WORKSPACE_NUMBER = sys.argv[1]
except IndexError:
    print("You didn't passed any argument")
else:
    print(ACTIVE_WORKSPACE)

    match WORKSPACE_NUMBER:
        case "g":
            move_to_wks(7)
            set_to_wks(window=ACTIVE_WINDOW, workspace=7)
        case "m":
            move_to_wks(5)
            set_to_wks(window=ACTIVE_WINDOW, workspace=5)
        case "l":
            move_to_wks(4)
            set_to_wks(window=ACTIVE_WINDOW, workspace=4)
        case "v":
            move_to_wks(3)
            set_to_wks(window=ACTIVE_WINDOW, workspace=3)
        case "t":
            move_to_wks(2)
            set_to_wks(window=ACTIVE_WINDOW, workspace=2)
        case "b":
            move_to_wks(1)
            set_to_wks(window=ACTIVE_WINDOW, workspace=1)
        case "s":
            move_to_wks(6)
            set_to_wks(window=ACTIVE_WINDOW, workspace=6)
