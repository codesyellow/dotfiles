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
        self.cleanup()

    def run(self):
        for times in range(self.breaks_before_long_pause):
            if times <= 3:
                self.play_audio("pomo_start.wav")
                self.countdown(time=self.pomodoro, name="pomo")
                self.play_audio("pomo_pause.wav")
                self.countdown(time=self.pomodoro_pause, name="pausa")
                self.number_of_breaks += 1
            else:
                self.play_audio("pomo_start.wav")
                self.countdown(time=self.pomodoro, name="pomo")
                self.play_audio("pomo_pause.wav")
                self.number_of_breaks += 1
                self.countdown(time=self.pomodoro_long_pause, name="pausa")
                self.play_audio("stretch_ended.wav")
                self.cleanup()

    def cleanup(self):
        if self.file_exist(self.pomodoro_time_path):
            self.remove_file(self.pomodoro_time_path)
        elif self.file_exist(self.pomodoro_pause_path):
            self.remove_file(self.pomodoro_pause_path)

    def countdown(self, time, name):
        while time > 0:
            if name == "pausa" and not self.created_pomo_pause:
                self.created_pomo_pause = True
                f = open(self.pomodoro_pause_path, mode="w")
                f.close()
            elif name == "pomo" and self.created_pomo_pause:
                self.created_pomo_pause = False
                self.remove_file(self.pomodoro_pause_path)
            self.save_time(time)
            time -= 1
            sleep(1)

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
