#!/usr/bin/env python
import subprocess
import time
from easyeffects_preset import Easyffects


class Music():
    def __init__(self) -> None:
        self.easyeffects = Easyffects()
        self.music_state = False
        self.equalizer_state = False
        self.volume_perc = self.get_volume()
        self.music_preset = "Bass Boosted"
        self.equalizer_preset = "LoudnessEqualizer"

    def get_process(self, process):
        """Check if x process is running"""
        try:
            actual_process = subprocess.check_output(
                ["pgrep",
                 f"{process}"]).strip()
        except subprocess.CalledProcessError:
            pass
        else:
            if len(actual_process) > 0:
                return True
            else:
                return False

    def music_playing(self):
        """Return true or false if music is playing"""
        if (self.get_process("lowfi")
                or self.get_process("youtube-music")
                or self.is_cmus_playing()
                ):
            return True
        else:
            return False

    def is_cmus_playing(self):
        """Check if cmus is playing and if it it's,
        return True or else, False."""
        try:
            cmus_info = subprocess.check_output(
                ["cmus-remote", "-Q"]
            ).decode("utf-8").split("\n")
        except subprocess.CalledProcessError:
            return False
        else:
            cmus_status = cmus_info[0].split(" ")[1].strip()
            if cmus_status == "playing":
                return True
            else:
                return False

    def get_volume(self):
        """Return the volume percentage"""
        return subprocess.check_output(
            [
                "pamixer",
                "--get-volume"
            ]).decode("utf-8").strip()

    def restore_volume(self):
        """Restore the volume to the value that it was before"""
        subprocess.check_output(
            [
                "pamixer",
                "--set-volume",
                f"{self.volume_perc}",
            ]
        )

    def run(self):
        while True:
            if self.music_playing() and not self.music_state:
                print(self.music_state)
                if self.easyeffects.read()[0] != self.music_preset:
                    self.volume_perc = self.get_volume()
                    self.easyeffects.seto("music")
                    self.music_state = True
                    self.equalizer_state = False
                    self.easyeffects.write(self.music_preset)
                    print("Preset was set to Heavy Bass",
                          self.easyeffects.read()[0])

                    subprocess.run(["pkill", "-RTMIN+3", "waybar"])
            elif not self.music_playing() and not self.equalizer_state:
                print("no")
                if self.easyeffects.read()[0] == self.music_preset:
                    self.easyeffects.seto("equalizer")
                    self.restore_volume()
                    self.equalizer_state = True
                    self.music_state = False
                    self.easyeffects.write(self.equalizer_preset)
                    print("Preset was set to Equalizer")
                    subprocess.run(["pkill", "-RTMIN+3", "waybar"])
            time.sleep(1)


if __name__ == "__main__":
    Music().run()
