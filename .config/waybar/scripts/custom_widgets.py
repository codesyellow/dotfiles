#!/usr/bin/env python3
import sys
import json
import psutil
import shutil
import os
import subprocess

HOME = os.path.expanduser("~/")
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

MIN_CPU_USAGE = 90
MIN_MEM_USAGE = 90
MIN_TEMP = 80
MIN_ROOT_SPACE = 10
MIN_HOME_SPACE = 10
MIN_HDD_SPACE = 30
MIN_UPDATES = 20

BAR_COLOR = "#4c566a"
NORMAL_COLOR = "#d8dee9"
WARNING_COLOR = "#EF5A6F"

POMODORO_TIME_PATH = "/tmp/pomo_timer"
EASYEFFECTS_PRESET_PATH = f"{HOME}/.config/.easy_preset"
STRETCH_TIME_PATH = "/tmp/stretch"
STRETCH_STOP_PATH = "/tmp/stop"


def display_json(state, widget):
    state = "warning"
    display = {
        "text": widget(),
        "tooltip": f"{widget}",
        "class": state,
    }
    print(json.dumps(display))


def set_pango(colors, size, position, icon_image, text, **kwargs):
    """Set the pango by passing three list, icon_image and the text:
        one for COLORS for bar,icon and text,
        size for bar, icon and text,
        position bar, icon and text,
        icon image and text"""
    bar = f"<span rise='{position[0]}' size='{
        size[0]}' foreground='{colors[0]}'>|</span>"
    icon = f"<span size='{size[1]}' foreground='{colors[1]}' rise='{
        position[1]}'>{icon_image}</span>"
    if kwargs.get("bar_pos") == "right" and text != "":
        output = f" {icon} <span rise='{
            position[2]}' foreground='{colors[1]}'>{text}</span> {bar} "
        return output
    elif kwargs.get("bar_pos") == "right" and text == "":
        output = f"{icon} {bar} "
        return output
    if text == "":
        output = f" {bar} {icon}"
        return output
    else:
        output = f" {bar} {icon} <span rise='{
            position[2]}' foreground='{colors[1]}'>{text}</span>"
        return output


def is_process_running(process_name):
    return process_name in (p.name() for p in psutil.process_iter())


def file_exist(file):
    return os.path.isfile(file)


def get_command_output(command):
    return subprocess.check_output(
        command, shell=True).decode('utf-8')


class Custom_Widgets:
    def check_keyboard_variant(self):
        """Return keyboard current
            variant if it's: US(INTL) or returns nothing"""

        devices_output = subprocess.check_output(
            ["hyprctl", "devices", "-j"]).decode("utf-8")

        devices = json.loads(devices_output)

        keyboards = devices.get("keyboards", [])
        is_intl_active = any(kb.get("active_keymap", "").find(
            "intl") != -1 for kb in keyboards)
        if is_intl_active:
            return set_pango(
                colors=[BAR_COLOR, WARNING_COLOR],
                size=[14000, 14000, 3000],
                position=[0, 500, 0],
                icon_image=KEYBOARD_ICONS,
                text="INTL",
                bar_pos="right",
            )
        else:
            return ""

    def check_updates(self):
        """Return the number of updates available for the system"""
        updates_available = get_command_output("checkupdates | wc -l")

        if int(updates_available) >= MIN_UPDATES:
            return set_pango(
                colors=[BAR_COLOR, WARNING_COLOR],
                size=[14000, 12000, 3000],
                position=[1000, 500, -400],
                icon_image=UPDATES_ICON,
                text=updates_available.strip(),
                bar_pos="right",
            )
        else:
            return ""

    def game_is_on(self):
        if file_exist("/tmp/gameon"):
            return set_pango(
                colors=[BAR_COLOR, WARNING_COLOR],
                size=[14000, 14000],
                position=[0, 0],
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
                size=[14000, 12000, 3000],
                position=[0, 1600, 0],
                icon_image=CPU_TEMP_ICON,
                text=f"{temperature}°",
                bar_pos="right",
            )
        else:
            return ""

    def cpu_usage(self):
        cpu_usage = int(psutil.cpu_percent(2))
        if cpu_usage > MIN_CPU_USAGE:
            return set_pango(
                colors=[BAR_COLOR, WARNING_COLOR],
                size=[10000, 13000, 3000],
                position=[0, -1900, -2000],
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
                size=[10000, 13000, 3000],
                position=[0, -2800, -2500],
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
                size=[10000, 13000, 3000],
                position=[0, 0, -1000],
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
                size=[14000, 11000, 3000],
                position=[0, 200, -1000],
                icon_image=HOME_ICON,
                text=f"{total_free}G",
                bar_pos="right"
            )
        else:
            return ""

    def hdd_space(self):
        total, used, free = shutil.disk_usage(f"{HOME}/.HDD")
        total_free = free // (2**30)
        if total_free <= MIN_HDD_SPACE:
            return set_pango(
                colors=[BAR_COLOR, WARNING_COLOR],
                size=[14000, 14000, 3000],
                position=[0, 0, -500],
                icon_image=HDD_ICON,
                text=f"{total_free}G",
                bar_pos="right"
            )
        else:
            return ""

    def easyeffects_is_on(self):
        if file_exist(EASYEFFECTS_PRESET_PATH):
            with open(EASYEFFECTS_PRESET_PATH, "r") as easy_preset:
                if easy_preset.read().strip() != "LoudnessEqualizer":
                    #                    return set_pango(
                    #                        colors=[BAR_COLOR, NORMAL_COLOR],
                    #                        size=[14000, 13000],
                    #                        position=[4000, 2000],
                    #                        icon_image=EASYEFFECTS_EQUALIZER_ICON,
                    #                        text="",
                    #                        bar_pos="right",
                    #                    )
                    return set_pango(
                        colors=[BAR_COLOR, WARNING_COLOR],
                        size=[14000, 14000],
                        position=[1000, 0],
                        icon_image=EASYEFFECTS_BASS_ICON,
                        text="",
                        bar_pos="right"
                    )
                else:
                    # return set_pango(
                    #    colors=[BAR_COLOR, WARNING_COLOR],
                    #    size=[20000, 14000],
                    #    position=[4000, 6000],
                    #    icon_image=EASYEFFECTS_BASS_ICON,
                    #    text=""
                    # )
                    return ""
        else:
            return ""

    def pomodoro(self):
        if file_exist(POMODORO_TIME_PATH):
            with open(POMODORO_TIME_PATH, "r") as pomodoro_time:
                colors = [BAR_COLOR, WARNING_COLOR]
                if file_exist("/tmp/pomo_pause"):
                    colors = [BAR_COLOR, NORMAL_COLOR]
                elif file_exist("/tmp/pomo_long_pause"):
                    colors = [BAR_COLOR, NORMAL_COLOR]

                return set_pango(
                    colors=colors,
                    size=[14000, 12000, 3000],
                    position=[0, 1800, 0],
                    icon_image=POMODORO_ICON,
                    text=pomodoro_time.read().strip()
                )
        else:
            return set_pango(
                colors=[BAR_COLOR, NORMAL_COLOR],
                size=[14000, 12000, 3000],
                position=[0, 1800, 0],
                icon_image=POMODORO_ICON,
                text="00:00"
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
                size=[14000, 13000, 3000],
                position=[0, -400, -1000],
                icon_image=STRETCH_ICON,
                text=current_text)
        else:
            return ""


cw = Custom_Widgets()


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"text": "Error", "tooltip": "No argument provided"}))
        sys.exit(1)

    module = sys.argv[1]

    if module == "cpu":
        state = "warning"
        cpu = {
            "text": cw.cpu_usage(),
            "tooltip": "CPU",
            "class": state,
        }
        print(json.dumps(cpu))
    elif module == "mem":
        display_json("warning", cw.mem_usage)
    elif module == "temp":
        display_json("warning", cw.cpu_temp)
    elif module == "root":
        display_json("warning", cw.root_space)
    elif module == "home":
        display_json("warning", cw.home_space)
    elif module == "hdd":
        display_json("warning", cw.hdd_space)
    elif module == "gameon":
        display_json("warning", cw.game_is_on)
    elif module == "easy":
        display_json("warning", cw.easyeffects_is_on)
    elif module == "updates":
        display_json("warning", cw.check_updates)
    elif module == "variant":
        display_json("warning", cw.check_keyboard_variant)
    elif module == "pomodoro":
        display_json("warning", cw.pomodoro)
    elif module == "stretch":
        display_json("warning", cw.do_stretch)
    else:
        print(json.dumps(
            {"text": "Unknown", "tooltip": f"No module for '{module}'"}))


if __name__ == "__main__":
    main()
