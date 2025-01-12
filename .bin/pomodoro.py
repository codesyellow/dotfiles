#!/usr/bin/env python
from time import sleep
import os
from datetime import timedelta

HOME = os.path.expanduser("~/")


class Pomodoro():
    def __init__(self) -> None:
        self.number_of_breaks = 0
        self.pomodoro = 25 * 60
        self.pomodoro_pause = 5 * 60
        self.pomodoro_long_pause = 20 * 60
        self.breaks_before_long_pause = 5
        self.pomodoro_time_path = "/tmp/pomo_timer"
        self.pomodoro_pause_path = "/tmp/pomo_pause"
        self.created_pomo_pause = False
        self.pause_state = False
        self.cleanup()

    def run(self):
        self.countdown(time=self.pomodoro, state="normal")

    # def run(self):
    #    for times in range(self.breaks_before_long_pause):
    #        if times <= 3 and not self.should_break:
    #            print("yes")
    #            self.play_audio("pomo_start.wav")
    #            self.countdown(time=self.pomodoro, name="pomo")
    #            if self.should_break():
    #                return
    #            self.play_audio("pomo_pause.wav")
    #            self.countdown(time=self.pomodoro_pause, name="pausa")
    #            self.number_of_breaks += 1
    #        else:
    #            if not self.should_break:
    #                self.play_audio("pomo_start.wav")
    #                self.countdown(time=self.pomodoro, name="pomo")
    #                self.play_audio("pomo_pause.wav")
    #                self.number_of_breaks += 1
    #                self.countdown(time=self.pomodoro_long_pause, name="pausa")
    #                self.play_audio("stretch_ended.wav")
    #                self.cleanup()

    def should_break(self):
        """Return true or false wheater it should break the loop or not"""
        return os.path.exists("/tmp/pomo_cancel")

    def cleanup(self):
        if self.file_exist(self.pomodoro_time_path):
            self.remove_file(self.pomodoro_time_path)
        if self.file_exist(self.pomodoro_pause_path):
            self.remove_file(self.pomodoro_pause_path)
        if self.file_exist("/tmp/pomo_cancel"):
            self.remove_file("/tmp/pomo_cancel")

    # def countdown(self, time, name):
    #    while time > 0:
    #        if self.should_break():
    #            break
    #        if name == "pausa" and not self.created_pomo_pause:
    #            self.created_pomo_pause = True
    #            f = open(self.pomodoro_pause_path, mode="w")
    #            f.close()
    #        elif name == "pomo" and self.created_pomo_pause:
    #            self.created_pomo_pause = False
    #            self.remove_file(self.pomodoro_pause_path)
    #        self.save_time(time)
    #        time -= 1
    #        sleep(1)

    def countdown(self, time, state):
        if state != "pause":
            self.play_audio("pomo_start.wav")
            self.remove_file(self.pomodoro_pause_path)
        else:
            f = open(self.pomodoro_pause_path, mode="w")
            f.close()

        while time > 0:
            self.save_time(time)
            if self.should_break():
                break
            time -= 1
            sleep(1)
        if not self.should_break():
            if state == "long_pause":
                return
            if state == "pause":
                self.countdown(self.pomodoro, "normal")
            elif self.number_of_breaks <= 3:
                self.play_audio("pomo_pause.wav")
                self.number_of_breaks += 1
                self.pause_state = True
                self.countdown(self.pomodoro_pause, "pause")
            else:
                self.pause_state = True
                self.countdown(self.pomodoro_long_pause, "long_pause")
                self.play_audio("stretch_ended.wav")
                self.cleanup()

    def is_running(self):
        if os.path.isfile(self.pomodoro_time_path):
            return True
        else:
            return False

    def play_audio(self, audio_name):
        os.system(f'paplay --volume=65536 {HOME}/.audios/{audio_name}')

    def save_time(self, time):
        with open(self.pomodoro_time_path, mode="w") as pomo_file:
            minutes = str(timedelta(seconds=time))[2:]

            pomo_file.write(
                f"{self.number_of_breaks}[{minutes}]")

    def remove_file(self, path):
        if os.path.exists(path):
            os.remove(path)

    def file_exist(self, file_path):
        return os.path.exists(file_path)


if __name__ == "__main__":
    Pomodoro().run()
