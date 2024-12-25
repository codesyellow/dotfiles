#!/usr/bin/env python
from dbus_idle import IdleMonitor
from plyer import notification
import time
import json
import os
import random
from playsound import playsound

config_file = None

try:
    with open("/home/digo/.config/pausa/config.json") as data:
        config_file = json.loads(data.read())
except FileNotFoundError:
    if not os.path.exists("/home/digo/.config/pausa"):
        os.makedirs("/home/digo/.config/pausa")

    with open("/home/digo/.config/pausa/config.json", mode="w") as data:
        config_file = {
            "idle_time": "5",
            "short_break_time": "10",
            "long_break_time": "30",
            "message_list": [],
        }
        json.dump(config_file, data)

IDLE_TIME = int(config_file["idle_time"])
PAUSE_TIME = int(config_file["short_break_time"])
LONG_PAUSE_TIME = int(config_file["long_break_time"])
MESSAGE_LIST = config_file["message_list"]
HOME = os.path.expanduser("~/")


class Pausa():
    def __init__(self) -> None:
        self.idle_seconds = IDLE_TIME * 60
        self.reset_activity = 0
        self.run()

    def play_audio(self, audio_name):
        playsound(f"{HOME}/.audios/{audio_name}", block=False)

    def run(self):
        while True:
            milliseconds = IdleMonitor()

            if not milliseconds.is_idle():
                self.idle_seconds -= 1
                self.reset_activity = 0
                if self.idle_seconds <= 0:
                    random_exercise = random.choice(MESSAGE_LIST)
                    self.play_audio("pausa.mp3")
                    title = random_exercise["title"]
                    message = random_exercise["message"]
                    duration = random_exercise["duration"]
                    self.noti(text=title, message=f"{message} for {
                        duration}", timeout=duration)
                    time.sleep(3)
                    time.sleep(duration)
                    self.idle_seconds = IDLE_TIME * 60
                    self.noti(text="Break ended", message="Back to work")
                    self.play_audio("pomo_start.wav")
            else:
                self.reset_activity += 1
                if self.reset_activity >= 120:
                    self.reset_activity = 0
                    self.idle_seconds = 0

            print(self.reset_activity, self.idle_seconds)
            time.sleep(1)

    def noti(self, text, message, timeout=10):
        notification.notify(
            title=text,
            message=message,
            timeout=timeout,
        )


pausa = Pausa()
