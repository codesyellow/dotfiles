#!/usr/bin/env python
import subprocess
import json
import argparse

PADDING = (20, 20)
SMALL = (400, 400)
SMALLA = (400, 700)
SMALLF = (800, 400)
MEDIUM = (600, 600)
MEDIUMA = (600, 700)
BIG = (1000, 700)

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
        match config["position"]:
            case "top":
                return (monitor_width//2 - self.size[0] // 2, PADDING[1])
            case "bottom":
                return (monitor_width//2 - self.size[0] // 2, monitor_height - self.size[1] - 50)
            case "top-left":
                return PADDING
            case "top-right":
                return (monitor_width - self.size[0] - PADDING[0], PADDING[1])
            case "bottom-left":
                return (PADDING[0], monitor_height - self.size[1] - 50)
            case "bottom-right":
                return (monitor_width - self.size[0] - PADDING[0], monitor_height - self.size[1] - 50)
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
        args = parser.parse_args()
        config = vars(args)
        command = config["command"]
        print(command.split())
        subprocess.Popen(command.split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                         stdin=subprocess.DEVNULL, start_new_session=True)

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
        resize = f"resize set {self.size[0]} {self.size[1]}"
        var = subprocess.check_output(
            f'swaymsg {app_name} scratchpad show, {position}, {resize} || echo 1', shell=True).decode("utf-8")
        if "false" in var:
            self.open_app()

    def run(self) -> None:
        """Run the scratchpad"""
        self.open_scratch()


swaypad = Swaypad()
print(swaypad.position)
print(swaypad.run())
