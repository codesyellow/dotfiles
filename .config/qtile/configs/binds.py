from libqtile.lazy import lazy
from libqtile.config import Click, Drag, Key
from .variables import mod, alt_mod, term, sterm
from .functions import latest_group, focus_main

keys = [
    Key([mod], 'j', lazy.layout.down()),
    Key([mod], 'k', lazy.layout.up()),
    Key([mod, 'shift'], 'k', lazy.layout.shuffle_down()),
    Key([mod, 'shift'], 'j', lazy.layout.shuffle_up()),
    Key([mod, 'control'], 'r', lazy.reload_config()),
    Key([mod, 'control'], 'q', lazy.shutdown()),
    Key([mod], 'f', lazy.window.toggle_fullscreen()),
    Key([mod, 'shift'], 'f', lazy.window.toggle_floating()),
    Key([mod], 'c', lazy.window.center()),
    Key([mod, 'shift'], 'e', lazy.core.change_vt(2)),
    Key([mod], "space", lazy.widget["keyboardlayout"].next_keyboard()),
    Key([mod], 'Tab', lazy.function(latest_group)),
    Key([mod, 'shift'], 'p', lazy.function(focus_main)),
    Key([mod], 'Return', lazy.spawn(sterm)),
    Key([mod], 't', lazy.spawn(f'{sterm} -T tmux -c tmux -e tmux')),
    Key([alt_mod], 't', lazy.spawn(term)),
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

