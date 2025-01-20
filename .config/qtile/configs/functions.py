from re import VERBOSE
from libqtile import qtile
from .variables import COLORS, GROUP_ICONS, VERTICAL_MONITOR_GROUPS
from libqtile.log_utils import logger
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
    current_focused_clients = qtile.current_group.last_focused
    all_clients = qtile.current_group.tiled_windows
    filtered_clients = [
        client.name.split(" ")[0] for client in all_clients if client != current_focused_clients]
    if len(filtered_clients) >= 3:
        filtered_clients = filtered_clients[:2]

    if len(filtered_clients) > 0:
        return f'<span size="x-large" foreground="{COLORS["bg1"]}">| </span><span rise="5000" foreground="#EF5A6F"> </span><span rise="4000">{", ".join(filtered_clients)}</span>'
    else:
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


def go_to_group(name: str):
    def _inner(qtile):
        if len(qtile.screens) == 1:
            qtile.groups_map[name].toscreen()
            return

        if name in VERTICAL_MONITOR_GROUPS:
            qtile.focus_screen(1)
            qtile.groups_map[name].toscreen()
        else:
            qtile.focus_screen(0)
            qtile.groups_map[name].toscreen()

    return _inner


def go_to_group_and_move_window(name: str):
    def _inner(qtile):
        if len(qtile.screens) == 1:
            qtile.current_window.togroup(name, switch_group=True)
            return

        if name in GROUP_ICONS:
            qtile.current_window.togroup(name, switch_group=False)
            qtile.focus_screen(0)
            qtile.groups_map[name].toscreen()
        else:
            qtile.current_window.togroup(name, switch_group=False)
            qtile.focus_screen(1)
            qtile.groups_map[name].toscreen()

    return _inner
