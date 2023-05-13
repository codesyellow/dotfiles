import os, subprocess
from libqtile import qtile
from configs.variables import wl_input_rules
from configs.bindings import *
from configs.layouts import *
from configs.groups import *
from configs.hooks import *
from configs.widgets import *
from configs.screens import *

if qtile.core.name == "wayland":
    @hook.subscribe.startup_once
    def autostart():
        home = os.path.expanduser('~/.config/qtile/wl_autostart.sh' )
        subprocess.Popen([home])

wl_input_rules = wl_input_rules
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True

wmname = "LG3D"
