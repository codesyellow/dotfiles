import psutil
import shutil
import os.path
from libqtile.log_utils import logger
# from .variables import home

CPU_ICON = ""
CPU_TEMP_ICON = ""
MEM_ICON = ""
ROOT_ICON = ""
HOME_ICON = ""
HDD_ICON = ""
PYMOR_ICON = ""
GAMEON_ICON = ""
MIN_CPU_USAGE = 80
MIN_MEM_USAGE = 80
MIN_TEMP = 80
MIN_ROOT_SPACE = 10
MIN_HOME_SPACE = 10
MIN_HDD_SPACE = 30

POMODORO_TIME_PATH = "/tmp/pomodoro_time"


def is_process_running(process_name):
    return process_name in (p.name() for p in psutil.process_iter())


def file_exist(file):
    return os.path.isfile(file)


def get_pango(type, icon_args, info_args):
    bar = "<span size='x-large' foreground='#4c566a'>|</span>"
    icon = f"<span size='{icon_args[0]}' foreground='#EF5A6F' rise='{
        icon_args[1]}'>{icon_args[2]}</span>"
    if type == "icon":
        output = f"{bar} {icon}"
        return output
    else:
        output = f"{bar} {icon} <span rise='{
            info_args[0]}' foreground='#EF5A6F'>{info_args[1]}</span>"
        return output


def cpu_temp():
    temperature = int(psutil.sensors_temperatures()["coretemp"][0][1])
    if temperature >= MIN_TEMP:
        return get_pango("full", [13000, 5550, CPU_TEMP_ICON],
                         [3800, f"{temperature}°"])
    else:
        return ""


def cpu_usage():
    cpu_usage = int(psutil.cpu_percent(2))
    if cpu_usage > MIN_CPU_USAGE:
        return get_pango("full", icon_args=[13500, 5400, CPU_ICON],
                         info_args=[3800, f"{cpu_usage}%"])
    else:
        return ""


def mem_usage():
    mem_usage = int(psutil.virtual_memory()[2])
    if mem_usage > MIN_MEM_USAGE:
        return get_pango("full", [12500, 4200,
                                  MEM_ICON], [3800, f"{mem_usage}%"])
    else:
        return ""


def root_space():
    total, used, free = shutil.disk_usage("/")
    total_free = free // (2**30)
    if total_free <= MIN_ROOT_SPACE:
        return get_pango("full", [11000, 5900,
                                  ROOT_ICON], [3800, f"{total_free}G"])
    else:
        return ""


def home_space():
    total, used, free = shutil.disk_usage("/home")
    total_free = free // (2**30)
    if total_free <= MIN_HOME_SPACE:
        return get_pango("full", [12500, 2800,
                                  HOME_ICON], [2500, f"{total_free}G"])
    else:
        return ""


def hdd_space():
    total, used, free = shutil.disk_usage("/home/digo/.HDD")
    total_free = free // (2**30)
    if total_free <= MIN_HDD_SPACE:
        return get_pango(
            "full",
            [22500, 220, HDD_ICON],
            [3800, f"{total_free}G"])
    else:
        return ""


def easyeffects_is_on():
    pass


def game_is_on():
    if file_exist("/tmp/gameon"):
        return get_pango("icon", [14000, 4700, GAMEON_ICON], [])
    else:
        return ""


def pomodoro():
    if file_exist(POMODORO_TIME_PATH):
        pomodoro_time = open(POMODORO_TIME_PATH, "r").read()
        return get_pango(
            "full",
            [11000, -6400, PYMOR_ICON],
            [-8000, pomodoro_time])
    else:
        return ""
