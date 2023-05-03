from libqtile import bar 
from libqtile.config import Screen
from configs.bindings import keys, mouse
from configs.layouts import layouts
from configs.groups import groups
from configs.widgets import *
from configs.hooks import *
from configs.screens import *

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
