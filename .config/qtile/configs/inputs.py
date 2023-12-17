from libqtile.backend.wayland import InputConfig
wl_input_rules = {
    "*": InputConfig(left_handed=False, pointer_accel=True),
    "type:keyboard": InputConfig(kb_options="ctrl:nocaps,compose:ralt"),
}


