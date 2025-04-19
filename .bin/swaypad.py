#!/usr/bin/env python
import subprocess
import json
import argparse
import time

PADDING = (20, 20)
SMALL = (40, 40)
SMALLA = (40, 80)
SMALLF = (90, 40)
MEDIUM = (50, 50)
MEDIUMA = (50, 50)
BIG = (90, 90)

parser = argparse.ArgumentParser(description="Description",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-p", "--position")
parser.add_argument("-s", "--sizes")
parser.add_argument("-c", "--command")
parser.add_argument("-n", "--name", default="")
parser.add_argument("-cn", "--class", default="")


class Swaypad():
    def __init__(self) -> None:
        self.scratch_size = 600
        self.size = self.set_size()
        self.position = self.set_position()
        self.focused_monitor = self.get_focused_monitor()

    def set_position(self):
        """Return the position"""
        monitor_width = self.get_focused_monitor()["rect"]["width"]
        monitor_height = self.get_focused_monitor()["rect"]["height"]
        args = parser.parse_args()
        config = vars(args)
        width = int(monitor_width * (self.size[0] / 100))
        height = int(monitor_height * (self.size[0] / 100))

        match config["position"]:
            case "top":
                return (monitor_width//2 - width // 2, PADDING[1])
            case "bottom":
                return (monitor_width//2 - width // 2, monitor_height - height - 50)
            case "top-left":
                return PADDING
            case "top-right":
                return (monitor_width - width - PADDING[0], PADDING[1])
            case "bottom-left":
                return (PADDING[0], monitor_height - height - 50)
            case "bottom-right":
                return (monitor_width - width - PADDING[0], monitor_height - height - 50)
            case _:
                return ("center", "")

    def set_size(self):
        """Return the chosed size"""
        args = parser.parse_args()
        config = vars(args)
        match config["sizes"]:
            case "sm":
                return SMALL
            case "sma":
                return SMALLA
            case "smf":
                return SMALLF
            case "med":
                return MEDIUM
            case "meda":
                return MEDIUMA
            case "big":
                return BIG

    def get_focused_monitor(self):
        """Return the focused monitor"""
        monitors = json.loads(subprocess.check_output([
            "swaymsg", "-t", "get_outputs", "-r"
        ]).decode("utf-8"))

        for monitor in monitors:
            if monitor["focused"]:
                return monitor

    def get_scratch_position(self):
        """Return the right position based on the scratchpad size"""
        width = self.focused_monitor["rect"]["width"]
        height = self.focused_monitor["rect"]["height"]
        print(width, height)

    def open_app(self):
        """Open the app"""
        args = parser.parse_args()
        config = vars(args)
        command = config["command"]
        subprocess.Popen(command.split(), start_new_session=True)

    def open_scratch(self) -> None:
        """Open the scratchpad"""
        args = parser.parse_args()
        config = vars(args)
        name = config["name"]
        class_name = config["class"]

        if len(class_name) == 0:
            app_name = f"[app_id='{name}']"
        else:
            app_name = f"[class='{class_name}']"
        position = f"move position {self.position[0]} {self.position[1]}"
        width = self.focused_monitor["rect"]["width"]
        height = self.focused_monitor["rect"]["height"]
        scratch_width = int(width * (self.size[0] / 100))
        scratch_height = int(height * (self.size[1] / 100))

        resize = f"resize set {scratch_width} {scratch_height}"
        app = subprocess.run(f'swaymsg {app_name} scratchpad show', shell=True)
        window_id = subprocess.check_output(
            "swaymsg -t get_tree | jq -r '.. | select(.focused?) | .id'", shell=True).strip().decode()
        time.sleep(0.1)
        subprocess.run(f'swaymsg {app_name} {resize}', shell=True)
        time.sleep(0.1)
        subprocess.run(f'swaymsg {app_name} {position}', shell=True)
        time.sleep(0.1)
        if window_id:
            subprocess.run(f'swaymsg [con_id={window_id}] focus', shell=True)

        if app.returncode == 2:
            self.open_app()

    def run(self) -> None:
        """Run the scratchpad"""
        self.open_scratch()


swaypad = Swaypad()
swaypad.run()
