from libqtile.backend.wayland import InputConfig
from libqtile import qtile

if qtile.core.name == "wayland":
    wl_input_rules = {
            "*": InputConfig(left_handed=False, pointer_accel=False),
            "type:keyboard": InputConfig(kb_options="ctrl:nocaps,compose:ralt"),
            }


