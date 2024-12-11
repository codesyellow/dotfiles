import psutil
import shutil
from libqtile.log_utils import logger
from .functions import set_pango, file_exist, get_command_output
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
KEYBOARD_ICONS = ""
STRETCH_ICON = ""

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
STRETCH_TIME_PATH = "/tmp/stretch"
STRETCH_STOP_PATH = "/tmp/stop"


class Custom_Widgets:
    def check_keyboard_variant(self):
        """Return keyboard current
            variant if it's: US(INTL) or returns nothing"""
        keyboard_variant = get_command_output("xkb-switch -p").strip()
        if keyboard_variant == "us(intl)":
            return set_pango(
                colors=[BAR_COLOR, WARNING_COLOR],
                size=[25000, 26000, 3000],
                position=[0, 4500, 10000],
                icon_image=KEYBOARD_ICONS,
                text="INTL"
            )
        else:
            return ""

    def check_updates(self):
        """Return the number of updates available for the system"""
        updates_available = get_command_output("checkupdates | wc -l")

        if int(updates_available) >= MIN_UPDATES:
            return set_pango(
                colors=[BAR_COLOR, WARNING_COLOR],
                size=[30000, 16000, 3000],
                position=[0, -2700, -2000],
                icon_image=UPDATES_ICON,
                text=updates_available
            )

    def game_is_on(self):
        if file_exist("/tmp/gameon"):
            return set_pango(
                colors=[BAR_COLOR, WARNING_COLOR],
                size=[20000, 14000],
                position=[4000, 8000],
                icon_image=GAMEON_ICON,
                text=""
            )
        else:
            return ""

    def cpu_temp(self):
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

    def cpu_usage(self):
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

    def mem_usage(self):
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

    def root_space(self):
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

    def home_space(self):
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

    def hdd_space(self):
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

    def easyeffects_is_on(self):
        if file_exist(EASYEFFECTS_PRESET_PATH):
            with open(EASYEFFECTS_PRESET_PATH, "r") as easy_preset:
                if easy_preset.read().strip() == "LoudnessEqualizer":
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

    def pomodoro(self):
        if file_exist(POMODORO_TIME_PATH):
            with open(POMODORO_TIME_PATH, "r") as pomodoro_time:
                return set_pango(
                    colors=[BAR_COLOR, WARNING_COLOR],
                    size=[30000, 13000, 3000],
                    position=[0, -700, -2200],
                    icon_image=POMODORO_ICON,
                    text=pomodoro_time.read()
                )
        else:
            return ""

    def do_stretch(self):
        current_colors = []
        current_text = ""
        if file_exist(STRETCH_TIME_PATH):
            if file_exist(STRETCH_STOP_PATH):
                current_text = "STOP!"
                current_colors = [BAR_COLOR, NORMAL_COLOR]
            else:
                current_text = "DOIT!"
                current_colors = [BAR_COLOR, WARNING_COLOR]
            return set_pango(
                colors=current_colors,
                size=[30000, 13000, 3000],
                position=[0, 9700, 8500],
                icon_image=STRETCH_ICON,
                text=current_text)
        else:
            return ""
