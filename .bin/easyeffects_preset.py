#!/usr/bin/env python
import os

HOME = os.path.expanduser("~")

PRESET_PATH = f"{HOME}/.config/easyeffects_preset"
EASYEFFECTS_APP_NAME = "easyeffects"


class Easyffects():
    def __init__(self) -> None:
        self.check_file()
        self.active_preset = self.read()[0]

    def run(self):
        # self.seto(self.read()[0])
        pass

    def check_file(self):
        """Check if file exist and if it does not, create it"""
        if not os.path.exists(PRESET_PATH):
            with open(PRESET_PATH, mode="w") as data:
                data.write("LoudnessEqualizer")

    def write(self, preset_name):
        """Write the preset name to the PRESET_PATH"""
        with open(PRESET_PATH, mode="w") as data:
            data.write(preset_name)
            self.active_preset = preset_name

    def read(self):
        """Get the current preset and return it as an arrow"""
        with open(PRESET_PATH) as data:
            return data.readlines()

    def seto(self, preset_name):
        """Set the preset for easyeffects. Options: music, equalizer"""
        music = "Bass"
        equalizer = "LoudnessEqualizer"
        if preset_name == "equalizer":
            os.system(f"{EASYEFFECTS_APP_NAME} -l '{equalizer}'")
        else:
            os.system(f"{EASYEFFECTS_APP_NAME} -l '{music}'")


if __name__ == "__main__":
    Easyffects().run()
