import os, subprocess
from libqtile import qtile
from configs.bindings import *
from configs.layouts import *
from configs.groups import *
from configs.hooks import *
from configs.widgets import *
from configs.screens import *
from libqtile.backend.wayland import InputConfig

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True


wl_input_rules = {
    "*": InputConfig(left_handed=False, pointer_accel=True),
    "type:keyboard": InputConfig(kb_options="grp:ctrl_alt_toggle", kb_layout="br,br", kb_variant="nodeadkeys"),
}

wmname = "LG3D"
