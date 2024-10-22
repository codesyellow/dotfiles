from libqtile import qtile
from libqtile.log_utils import logger

def desconnect_ds4():
    qtile.cmd_spawn('dsbattery -d')

def run_easy():
    qtile.cmd_spawn('flatpak run com.github.wwmm.easyeffects --gapplication-service')

def stop_easy():
    qtile.cmd_spawn('killall easyeffects')

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
            return f'<span foreground="#EF5A6F">  </span>{str(num_windows)} <span foreground="#fff"> |</span>'
    return ""

