#!/usr/bin/env python
from dbus_idle import IdleMonitor
import time
import json
import os
import random

config_file = None

try:
    with open("/home/digo/.config/pausa/config.json") as data:
        config_file = json.loads(data.read())
except FileNotFoundError:
    if not os.path.exists("/home/digo/.config/pausa"):
        os.makedirs("/home/digo/.config/pausa")

    with open("/home/digo/.config/pausa/config.json", mode="w") as data:
        config_file = {
            "idle_time": "10",
            "short_break_time": "20",
            "long_break_multiplier": "2",
            "long_break_time": "60",
            "EXERCISE_LIST": [],
        }
        json.dump(config_file, data)

IDLE_TIME = int(config_file["idle_time"])
PAUSE_TIME = int(config_file["short_break_time"])
LONG_PAUSE_TIME = int(config_file["long_break_time"])
LONG_BREAK_MULTIPLIER = int(config_file["long_break_multiplier"])
EXERCISE_LIST = config_file["exercise_list"]
HOME = os.path.expanduser("~/")


class Pausa():
    def __init__(self) -> None:
        self.idle_seconds = IDLE_TIME * 60
        self.reset_activity = 0
        self.pausa_state_path = "/tmp/pausa"
        self.short_break_time = PAUSE_TIME
        self.long_break_time = (IDLE_TIME * 60) * LONG_BREAK_MULTIPLIER
        self.run()

    def notify(self, title, body, expire=1000, urgency="normal"):
        os.system(f"notify-send '{title}' '{body}' -t {expire} -u {urgency}")

    def play_audio(self, audio_name):
        os.system(f'paplay --volume=65536 {HOME}/.audios/{audio_name}')

    def pausa_state(self):
        f = open(self.pausa_state_path, mode="w")
        f.close()

    def reset_idle_time(self):
        self.idle_seconds = IDLE_TIME * 60

    def exercise(self, which):
        random_exercise = random.choice(EXERCISE_LIST[which])
        title = random_exercise["title"]
        message = random_exercise["message"]
        duration = PAUSE_TIME * 1000
        if "long" in which:
            duration = LONG_PAUSE_TIME * 1000
        self.notify(title=title, body=message,
                    expire=duration, urgency="critical")

    def do_break(self, pause_time, which):
        self.pausa_state()
        self.exercise(which)
        self.play_audio("pausa.mp3")
        time.sleep(3)
        while pause_time > 0:
            pause_time -= 1
            time.sleep(1)
        self.notify(title="PAUSA", body="DONE")
        self.play_audio("pausa_end.wav")
        self.reset_idle_time()

    def reset_long_break(self):
        self.long_break_time = (IDLE_TIME * 60) * LONG_BREAK_MULTIPLIER

    def is_active(self):
        """return the idle state as true or false"""
        milliseconds = IdleMonitor()
        if not milliseconds.is_idle():
            return True
        else:
            return False

    def run(self):
        while True:
            if self.is_active() and not os.path.exists("/tmp/pausa_stop"):
                for _ in range(0, 9):
                    self.idle_seconds -= 1
                    self.long_break_time -= 1
                    self.reset_activity = 0
                    if self.long_break_time == 0:
                        self.do_break(
                            LONG_PAUSE_TIME, "long_break")
                        self.reset_long_break()
                    elif self.idle_seconds == 0:
                        self.do_break(PAUSE_TIME, "short_break")
                    if os.path.exists(self.pausa_state_path):
                        os.remove(self.pausa_state_path)
                    time.sleep(1)
            else:
                if os.path.exists(self.pausa_state_path):
                    os.remove(self.pausa_state_path)
                self.reset_activity += 1
                if self.reset_activity >= 120 and self.idle_seconds != IDLE_TIME:
                    self.reset_activity = 0
                    self.reset_long_break()
                    self.reset_idle_time()

            print(self.reset_activity, self.idle_seconds,
                  self.long_break_time)
            time.sleep(1)


pausa = Pausa()
