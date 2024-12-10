import psutil
import shutil
import os.path
import subprocess
from libqtile.log_utils import logger
from .functions import set_pango
# from .variables import home

CPU_ICON = ""
CPU_TEMP_ICON = ""
MEM_ICON = ""
ROOT_ICON = ""
HOME_ICON = ""
HDD_ICON = ""
POMODORO_ICON = ""
GAMEON_ICON = ""
EASYEFFECTS_EQUALIZER_ICON = ""
EASYEFFECTS_BASS_ICON = ""
UPDATES_ICON = "󰇚"

MIN_CPU_USAGE = 80
MIN_MEM_USAGE = 90
MIN_TEMP = 80
MIN_ROOT_SPACE = 10
MIN_HOME_SPACE = 10
MIN_HDD_SPACE = 30
MIN_UPDATES = 20

BAR_COLOR = "#4c566a"
NORMAL_COLOR = "#d8dee9"
WARNING_COLOR = "#EF5A6F"

POMODORO_TIME_PATH = "/tmp/pomodoro_time"
EASYEFFECTS_PRESET_PATH = "/home/digo/.config/.easy_preset"


def is_process_running(process_name):
    return process_name in (p.name() for p in psutil.process_iter())


def file_exist(file):
    return os.path.isfile(file)


def cpu_temp():
    temperature = int(psutil.sensors_temperatures()["coretemp"][0][1])
    if temperature >= MIN_TEMP:
        return set_pango(
            colors=[BAR_COLOR, WARNING_COLOR],
            size=[20000, 13000, 3000],
            position=[0, 4000, 2700],
            icon_image=CPU_TEMP_ICON,
            text=f"{temperature}°"
        )
    else:
        return ""


def cpu_usage():
    cpu_usage = int(psutil.cpu_percent(2))
    if cpu_usage > MIN_CPU_USAGE:
        return set_pango(
            colors=[BAR_COLOR, WARNING_COLOR],
            size=[20000, 13000, 3000],
            position=[0, 4000, 2700],
            icon_image=CPU_ICON,
            text=f"{cpu_usage}%"
        )
    else:
        return ""


def mem_usage():
    mem_usage = int(psutil.virtual_memory()[2])
    if mem_usage > MIN_MEM_USAGE:
        return set_pango(
            colors=[BAR_COLOR, WARNING_COLOR],
            size=[20000, 13000, 3000],
            position=[0, 3000, 2700],
            icon_image=MEM_ICON,
            text=f"{mem_usage}%"
        )
    else:
        return ""


def root_space():
    total, used, free = shutil.disk_usage("/")
    total_free = free // (2**30)
    if total_free <= MIN_ROOT_SPACE:
        return set_pango(
            colors=[BAR_COLOR, WARNING_COLOR],
            size=[20000, 13000, 3000],
            position=[0, 4400, 2700],
            icon_image=ROOT_ICON,
            text=f"{total_free}G"
        )
    else:
        return ""


def home_space():
    total, used, free = shutil.disk_usage("/home")
    total_free = free // (2**30)
    if total_free <= MIN_HOME_SPACE:
        return set_pango(
            colors=[BAR_COLOR, WARNING_COLOR],
            size=[20000, 11000, 3000],
            position=[0, 4700, 2700],
            icon_image=HOME_ICON,
            text=f"{total_free}G"
        )
    else:
        return ""


def hdd_space():
    total, used, free = shutil.disk_usage("/home/digo/.HDD")
    total_free = free // (2**30)
    if total_free <= MIN_HDD_SPACE:
        return set_pango(
            colors=[BAR_COLOR, WARNING_COLOR],
            size=[20000, 23000, 3000],
            position=[0, 2200, 6500],
            icon_image=HDD_ICON,
            text=f"{total_free}G"
        )
    else:
        return ""


def easyeffects_is_on():
    if file_exist(EASYEFFECTS_PRESET_PATH):
        easy_preset = open(EASYEFFECTS_PRESET_PATH, "r").read().strip()
        if easy_preset == "LoudnessEqualizer":
            return set_pango(
                colors=[BAR_COLOR, NORMAL_COLOR],
                size=[20000, 13000],
                position=[4000, 6000],
                icon_image=EASYEFFECTS_EQUALIZER_ICON,
                text=""
            )
        else:
            return set_pango(
                colors=[BAR_COLOR, WARNING_COLOR],
                size=[20000, 14000],
                position=[4000, 6000],
                icon_image=EASYEFFECTS_BASS_ICON,
                text=""
            )
    else:
        return ""


def game_is_on():
    if file_exist("/tmp/gameon"):
        return set_pango(
            colors=[BAR_COLOR, WARNING_COLOR],
            size=[20000, 14000],
            position=[4000, 6000],
            icon_image=GAMEON_ICON,
            text=""
        )
    else:
        return ""


def pomodoro():
    if file_exist(POMODORO_TIME_PATH):
        pomodoro_time = open(POMODORO_TIME_PATH, "r").read()
        return set_pango(
            colors=[BAR_COLOR, WARNING_COLOR],
            size=[30000, 13000, 3000],
            position=[0, -700, -2200],
            icon_image=POMODORO_ICON,
            text=pomodoro_time
        )
    else:
        return ""


def check_updates():
    """Return the number of updates available for the system"""
    updates_available = subprocess.check_output(
        "checkupdates | wc -l", shell=True).decode('utf-8')

    if int(updates_available) >= MIN_UPDATES:
        return set_pango(
            colors=[BAR_COLOR, WARNING_COLOR],
            size=[30000, 16000, 3000],
            position=[0, -2700, -2000],
            icon_image=UPDATES_ICON,
            text=updates_available
        )
