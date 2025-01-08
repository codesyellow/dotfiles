from libqtile import qtile
from .variables import COLORS
import psutil
import os.path
import subprocess
import os


def start_pomodoro():
    script_path = os.path.expanduser("~/.bin/pomodoro.py")
    subprocess.Popen(["python3", script_path])


def stop_timers(file):
    f = open(f"/tmp/{file}", "w")
    f.close()


def get_terminal(name, terminal="st", font_size=16):
    font_name = 'CaskaydiaCove Nerd Font Mono'
    class_letter = "-c"
    name_letter = "-T"
    if terminal.lower() == "alacritty":
        return f'alacritty -T {name} --class {name}"'

    terminal_with_names = f"{terminal} {name_letter} {
        name} {class_letter} {name}"
    return f'{terminal_with_names} -f "{font_name}:pixelsize={font_size}"'


def desconnect_ds4():
    qtile.cmd_spawn("dsbattery -d")


def tabbed():
    if qtile.current_group and qtile.current_group.tiled_windows:
        num_windows = len(qtile.current_group.tiled_windows)
        if num_windows <= 1:
            return ""
        else:
            return f'<span size="x-large" foreground="{COLORS["bg1"]}">| </span><span rise="5000" foreground="#EF5A6F"> </span><span rise="4000">{str(num_windows)}</span>'
    return ""


def set_pango(colors, size, position, icon_image, text):
    """Set the pango by passing three list, icon_image and the text:
        one for COLORS for bar,icon and text,
        size for bar, icon and text,
        position bar, icon and text,
        icon image and text"""
    bar = f"<span rise='{position[0]}' size='{
        size[0]}' foreground='{colors[0]}'>|</span>"
    icon = f"<span size='{size[1]}' foreground='{colors[1]}' rise='{
        position[1]}'>{icon_image}</span>"
    if size[0] == 0:
        output = f"{icon} <span rise='{
            position[2]}' foreground='{colors[1]}'>{text}</span>"
        return output

    elif text == "":
        output = f"{bar} {icon}"
        return output
    else:
        output = f"{bar} {icon} <span rise='{
            position[2]}' foreground='{colors[1]}'>{text}</span>"
        return output


def is_process_running(process_name):
    return process_name in (p.name() for p in psutil.process_iter())


def file_exist(file):
    return os.path.isfile(file)


def get_command_output(command):
    return subprocess.check_output(
        command, shell=True).decode('utf-8')
