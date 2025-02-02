from libqtile import bar
import psutil
import shutil
import subprocess
from .functions import set_pango, file_exist, get_command_output, get_pango
from .variables import HOME

CPU_ICON = ""
SANTOS_FC = "󰒸"
CPU_TEMP_ICON = ""
DS4_ICON = "󰊴"
MEM_ICON = ""
ROOT_ICON = ""
HOME_ICON = ""
HDD_ICON = ""
POMODORO_ICON = ""
PAUSA_ICON = ""
COUNTDOWN_ICON = ""
GAMEON_ICON = ""
EASYEFFECTS_EQUALIZER_ICON = ""
EASYEFFECTS_BASS_ICON = ""
UPDATES_ICON = "󰇚"
KEYBOARD_ICONS = ""
STRETCH_ICON = ""

MIN_CPU_USAGE = 90
MIN_MEM_USAGE = 90
MIN_TEMP = 90
MIN_ROOT_SPACE = 10
MIN_HOME_SPACE = 10
MIN_HDD_SPACE = 10
MIN_UPDATES = 20

BAR_COLOR = "#4c566a"
NORMAL_COLOR = "#d8dee9"
WARNING_COLOR = "#EF5A6F"

POMODORO_TIME_PATH = "/tmp/pomo_timer"
COUNTDOWN_PATH = "/tmp/countdown_timer"
EASYEFFECTS_PRESET_PATH = f"{HOME}/.config/easyeffects_preset"
STRETCH_TIME_PATH = "/tmp/stretch"
STRETCH_STOP_PATH = "/tmp/stop"


class Custom_Widgets:
    def check_keyboard_variant(self, texty: int = 0, icony: int = 0, icon_size=15000, bar_pos="left", bary: int = 0):
        """Return keyboard current
            variant if it's: US(INTL) or returns nothing"""
        keyboard_variant = get_command_output("xkb-switch -p").strip()
        if keyboard_variant == "us(intl)":
            return get_pango(
                text="INTL",
                texty=texty,
                icon_image=KEYBOARD_ICONS,
                colors=[BAR_COLOR, WARNING_COLOR],
                icony=icony,
                icon_size=icon_size,
                bar_pos=bar_pos,
            )
        else:
            return ""

    def check_updates(self, texty: int, icony: int, icon_size: int, bar_pos: str = "left"):
        """Return the number of updates available for the system"""
        updates_available = get_command_output("checkupdates | wc -l").strip()

        if int(updates_available) >= MIN_UPDATES:
            return get_pango(
                text=updates_available.strip(),
                texty=texty,
                icon_image=UPDATES_ICON,
                colors=[BAR_COLOR, WARNING_COLOR],
                icony=icony,
                icon_size=icon_size,
                bar_pos=bar_pos,
            )
        else:
            return ""

    def ds4_bat(self, texty: int, icony: int, icon_size: int, bar_pos: str = "left"):
        """Return ds4 bat"""
        ds4 = subprocess.check_output([
            "dsbattery"
        ]).decode("utf-8").strip()
        text = ""
        style = "full"
        if len(ds4) > 0:
            text = ds4.split()[1]
        else:
            text = ""
            style = "icon"

        return get_pango(
            text=text,
            texty=texty,
            icon_image=DS4_ICON,
            icony=icony,
            icon_size=icon_size,
            bar_pos=bar_pos,
            style=style,
        )

    def santos_widget(self):
        """Return Santos FC info"""
        try:
            with open("/tmp/santos_widget") as data:
                santos_info = data.read().strip()
        except FileNotFoundError:
            return ""
        else:
            if file_exist("/tmp/santos_widget"):
                return set_pango(
                    colors=[BAR_COLOR, NORMAL_COLOR],
                    size=[0, 16000, 3000],
                    position=[0, 1000, 2000],
                    icon_image=SANTOS_FC,
                    text=santos_info,
                )
            else:
                return ""

    def game_is_on(self, texty: int = 0, icony: int = 0, icon_size=15000, bar_pos="right", bary: int = 0):
        if file_exist("/tmp/gameon"):
            return get_pango(
                colors=[BAR_COLOR, WARNING_COLOR],
                texty=texty,
                style="icon",
                icony=icony,
                icon_size=icon_size,
                icon_image=GAMEON_ICON,
                text="",
                bar_pos=bar_pos
            )
        else:
            return ""

    def cpu_temp(self, texty: int = 0, icony: int = 0, icon_size=15000, bar_pos="right", bary: int = 0):
        temperature = int(psutil.sensors_temperatures()["coretemp"][0][1])
        if temperature >= MIN_TEMP:
            return get_pango(
                colors=[BAR_COLOR, WARNING_COLOR],
                text=f"{temperature}°",
                icon_image=CPU_TEMP_ICON,
                icony=icony,
                icon_size=icon_size,
                texty=texty,
                bar_pos=bar_pos
            )
        else:
            return ""

    def cpu_usage(self, texty: int = 0, icony: int = 0, icon_size=15000, bar_pos="right", bary: int = 0):
        cpu_usage = int(psutil.cpu_percent(2))
        if cpu_usage > MIN_CPU_USAGE:
            return get_pango(
                colors=[BAR_COLOR, WARNING_COLOR],
                text=f"{cpu_usage}%",
                icon_image=CPU_ICON,
                icony=icony,
                icon_size=icon_size,
                texty=texty,
                bar_pos=bar_pos
            )
        else:
            return ""

    def mem_usage(self, texty: int = 0, icony: int = 0, icon_size=15000, bar_pos="right", bary: int = 0):
        mem_usage = int(psutil.virtual_memory()[2])
        if mem_usage > MIN_MEM_USAGE:
            return get_pango(
                colors=[BAR_COLOR, WARNING_COLOR],
                text=f"{mem_usage}%",
                icon_image=MEM_ICON,
                icony=icony,
                icon_size=icon_size,
                texty=texty,
                bar_pos=bar_pos
            )
        else:
            return ""

    def root_space(self, texty: int = 0, icony: int = 0, icon_size=15000, bar_pos="right", bary: int = 0):
        total, used, free = shutil.disk_usage("/")
        total_free = free // (2**30)
        if total_free <= MIN_ROOT_SPACE:
            return get_pango(
                colors=[BAR_COLOR, WARNING_COLOR],
                text=f"{total_free}G",
                icon_image=ROOT_ICON,
                icony=icony,
                icon_size=icon_size,
                texty=texty,
                bar_pos=bar_pos
            )
        else:
            return ""

    def home_space(self, texty: int = 0, icony: int = 0, icon_size=15000, bar_pos="right", bary: int = 0):
        total, used, free = shutil.disk_usage("/home")
        total_free = free // (2**30)
        if total_free <= MIN_HOME_SPACE:
            return get_pango(
                colors=[BAR_COLOR, WARNING_COLOR],
                text=f"{total_free}G",
                icon_image=HOME_ICON,
                icony=icony,
                icon_size=icon_size,
                texty=texty,
                bar_pos=bar_pos
            )
        else:
            return ""

    def hdd_space(self, texty: int = 0, icony: int = 0, icon_size=15000, bar_pos="right", bary: int = 0):
        total, used, free = shutil.disk_usage(f"{HOME}/.HDD")
        total_free = free // (2**30)
        if total_free <= MIN_HDD_SPACE:
            return get_pango(
                colors=[BAR_COLOR, WARNING_COLOR],
                text=f"{total_free}G",
                icon_image=HDD_ICON,
                icony=icony,
                icon_size=icon_size,
                texty=texty,
                bar_pos=bar_pos
            )
        else:
            return ""

    def easyeffects_is_on(self, texty: int = 0, icony: int = 0, icon_size=15000, bar_pos="right", bary: int = 0):
        icon_image = EASYEFFECTS_EQUALIZER_ICON
        colors = []

        if file_exist(EASYEFFECTS_PRESET_PATH):
            with open(EASYEFFECTS_PRESET_PATH, "r") as easy_preset:
                if easy_preset.read().strip() == "LoudnessEqualizer":
                    colors = [BAR_COLOR, NORMAL_COLOR]
                else:
                    colors = [BAR_COLOR, WARNING_COLOR]
                    icon_image = EASYEFFECTS_BASS_ICON
                return get_pango(
                    colors=colors,
                    texty=texty,
                    style="icon",
                    icony=icony,
                    icon_size=icon_size,
                    icon_image=icon_image,
                    text="",
                    bar_pos=bar_pos
                )
        else:
            return ""

    def countdown(self, texty: int = 0, icony: int = 0, icon_size=15000, bar_pos="right", bary: int = 0):
        if file_exist(COUNTDOWN_PATH):
            with open(COUNTDOWN_PATH, "r") as timer:
                return get_pango(
                    text=timer.read().strip(),
                    icon_image=COUNTDOWN_ICON,
                    colors=[BAR_COLOR, WARNING_COLOR],
                    icon_size=icon_size,
                    texty=texty,
                    icony=icony,
                    bar_pos=bar_pos
                )
        else:
            return ""

    def pomodoro(self, texty: int = 0, icony: int = 0, icon_size=15000, bar_pos="right", bary: int = 0):
        colors = [BAR_COLOR, NORMAL_COLOR]
        text = "0:00:00"
        if file_exist(POMODORO_TIME_PATH):
            with open(POMODORO_TIME_PATH, "r") as pomodoro_time:
                if file_exist("/tmp/pomo_pause"):
                    colors = [BAR_COLOR, WARNING_COLOR]
                elif file_exist("/tmp/pomo_long_pause"):
                    colors = [BAR_COLOR, WARNING_COLOR]

                text = pomodoro_time.read().strip()
        return get_pango(
            text=text,
            icon_image=POMODORO_ICON,
            colors=colors,
            icon_size=icon_size,
            texty=texty,
            icony=icony,
            bar_pos=bar_pos
        )

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
