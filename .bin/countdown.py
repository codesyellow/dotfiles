#!/home/digo/.bin/.venv/bin/python
import time
import os
from datetime import timedelta
from plyer import notification


def clear():
    os.system('clear')


COUNTDOWN_PATH = "/tmp/countdown_timer"

if os.path.isfile(COUNTDOWN_PATH):
    print("Countdown is running!")
    exit(0)

if os.path.exists("/tmp/countdown_cancel"):
    os.remove("/tmp/countdown_cancel")


of_type = [
    "m",
    "s",
]


def noti(text, message):
    notification.notify(
        title=text,
        message=message,
    )


def start_countdown(user_time):
    while user_time > 0:
        if os.path.exists("/tmp/countdown_cancel"):
            break
        time.sleep(1)
        user_time -= 1
        to_display = str(timedelta(seconds=user_time))[2:]
        with open(COUNTDOWN_PATH, mode="w") as timer:
            timer.write(to_display)
    os.remove(COUNTDOWN_PATH)
    noti("Ended!", "You did it!")
    check_time()


def check_time():
    clear()
    user_choose = input(
        "What do you want to do? M for minutes, S for seconds(Empty = M): ").lower()

    if user_choose not in of_type and user_choose != "":
        print("Should be m or s or b.")
        exit(1)

    user_time = int(input("How many?: "))

    if user_choose == "m" or user_choose == "":
        if os.path.exists("/tmp/countdown_cancel"):
            os.remove("/tmp/countdown_cancel")

        noti("Countdown started", f"{user_time} Minutes")
        start_countdown(user_time * 60)
    else:
        if os.path.exists("/tmp/countdown_cancel"):
            os.remove("/tmp/countdown_cancel")

        start_countdown(user_time)


check_time()
