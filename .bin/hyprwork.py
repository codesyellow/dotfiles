#!/usr/bin/env python
import subprocess
import json
import sys

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


WORKSPACE_NUMBER = sys.argv[1]


def move_to_wks(wks):
    subprocess.run([
        "hyprctl", "dispatch", "moveoutofgroup",
    ])
    subprocess.run([
        "hyprctl", "dispatch", "movetoworkspace", f"{wks}"
    ])


def set_to_wks(window, workspace):
    rule = f"windowrulev2 = workspace {
        workspace} silent,class:^({window["class"]})$"
    with open("/home/digo/.config/hypr/configs/rules.conf", mode="a") as data:
        data.write(f"\n{rule}")


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
