from libqtile import qtile
from .variables import colors


def desconnect_ds4():
    qtile.cmd_spawn("dsbattery -d")


def run_easy():
    qtile.cmd_spawn(
        "flatpak run com.github.wwmm.easyeffects --gapplication-service")


def stop_easy():
    qtile.cmd_spawn("killall easyeffects")


def latest_group(qtile):
    qtile.current_screen.set_group(qtile.current_screen.previous_group)


def focus_main(qtile):
    window = qtile.current_group.layout.focus_first()
    qtile.current_group.focus(window)


def tabbed():
    if qtile.current_group and qtile.current_group.tiled_windows:
        num_windows = len(qtile.current_group.tiled_windows)
        if num_windows <= 1:
            return ""
        else:
            return f'<span size="x-large" foreground="{colors["bg1_color"]}">| </span><span rise="5000" foreground="#EF5A6F"> </span><span rise="4000">{str(num_windows)}</span>'
    return ""


def set_pango(colors, size, position, icon_image, text):
    """Set the pango by passing three list, icon_image and the text:
        one for colors for bar,icon and text,
        size for bar, icon and text,
        position bar, icon and text,
        icon image and text"""
    bar = f"<span rise='{position[0]}' size='{
        size[0]}' foreground='{colors[0]}'>|</span>"
    icon = f"<span size='{size[1]}' foreground='{colors[1]}' rise='{
        position[1]}'>{icon_image}</span>"
    if text == "":
        output = f"{bar} {icon}"
        return output
    else:
        output = f"{bar} {icon} <span rise='{
            position[2]}' foreground='{colors[1]}'>{text}</span>"
        return output
