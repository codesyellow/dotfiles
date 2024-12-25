#!/usr/bin/env python
import time
import os
from playsound import playsound
from datetime import timedelta


if os.path.isfile("/tmp/pomo_timer"):
    print("Pomodoro is already running!")
    exit(0)
POMODORO_TIME = 25
POMODORO_PAUSE = 5
POMODORO_LONG_PAUSE = 20
BREAKS_BEFORE_LONG_PAUSE = 4
POMODORO_TIME_PATH = "/tmp/pomo_timer"
POMODORO_LONG_PAUSE_PATH = "/tmp/pomo_long_pause"
POMODORO_PAUSE_PATH = "/tmp/pomo_pause"
HOME = os.path.expanduser("~/")

pomodoro_running = True
pomodoro_countdown = POMODORO_TIME * 60
pomodoro_pause_countdown = POMODORO_PAUSE * 60
pomodoro_long_pause_countdown = POMODORO_LONG_PAUSE * 60
number_of_breaks = 0
should_take_break = False
should_take_long_break = False


playsound(f"{HOME}/.audios/pomo_start.wav", block=False)


def reset_time(time):
    return time * 60


def save_time(time):
    with open(POMODORO_TIME_PATH, mode="w") as pomo_file:
        minutes = str(timedelta(seconds=time))[2:]

        pomo_file.write(
            f"{number_of_breaks}[{minutes}]")


def remove_file(path):
    if os.path.exists(path):
        os.remove(path)


while pomodoro_running:
    if os.path.exists("/tmp/pomo_cancel"):
        break

    if should_take_break:
        pomodoro_pause_countdown -= 1
        save_time(pomodoro_pause_countdown)
        if number_of_breaks >= BREAKS_BEFORE_LONG_PAUSE:
            should_take_long_break = True
            should_take_break = False
        elif pomodoro_pause_countdown <= 0:
            playsound(f"{HOME}/.audios/pomo_pause.wav", block=False)
            if os.path.exists(POMODORO_PAUSE_PATH):
                os.remove(POMODORO_PAUSE_PATH)
            should_take_break = False
            number_of_breaks += 1
            pomodoro_pause_countdown = reset_time(POMODORO_PAUSE)
        else:
            open(POMODORO_PAUSE_PATH, "w")
    elif should_take_long_break:
        pomodoro_long_pause_countdown -= 1
        save_time(pomodoro_long_pause_countdown)
        open(POMODORO_LONG_PAUSE_PATH, "w")
        if pomodoro_long_pause_countdown <= 0:
            playsound(f"{HOME}/.audios/pomo_pause.wav", block=False)
            pomodoro_running = False
            break
    else:
        pomodoro_countdown -= 1
        save_time(pomodoro_countdown)

        if pomodoro_countdown <= 0:
            playsound(f"{HOME}/.audios/pomo_pause.wav", block=False)
            should_take_break = True
            pomodoro_countdown = reset_time(POMODORO_TIME)

    time.sleep(1)

remove_file(POMODORO_LONG_PAUSE_PATH)
remove_file(POMODORO_TIME_PATH)
remove_file("/tmp/pomo_cancel")
