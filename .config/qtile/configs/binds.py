from libqtile.lazy import lazy
from libqtile.config import Click, Drag, Key
from .variables import mod, alt_mod, term
from .functions import latest_group, focus_main

keys = [
        Key([mod], 'j', lazy.layout.down()),
        Key([mod], 'k', lazy.layout.up()),
        Key([mod, 'shift'], 'k', lazy.layout.shuffle_down()),
        Key([mod, 'shift'], 'j', lazy.layout.shuffle_up()),
        Key([mod], 't', lazy.spawn(term)),
        Key([alt_mod], 't', lazy.spawn(term)),
        Key([mod, 'control'], 'r', lazy.reload_config()),
        Key([mod, 'control'], 'q', lazy.shutdown()),
        # apps
        Key([mod], 'f', lazy.window.toggle_fullscreen()),
        Key([mod, 'shift'], 'f', lazy.window.toggle_floating()),
        Key([mod], 'c', lazy.window.center()),
        Key([mod, 'shift'], 'm', lazy.spawn('alacritty -t fm-video -e lf /home/cse/.courses')),
        Key([mod, 'shift'], 'e', lazy.core.change_vt(2)),
        Key([mod], "space", lazy.widget["keyboardlayout"].next_keyboard(), desc="Next keyboard layout."),
        #Key([mod], 'e', lazy.spawn(term + ' --class code -e lvim -c "cd ~/.code | NvimTreeToggle"')),
        # exec
    Key([mod], 'Tab', lazy.function(latest_group)),
    Key([mod, 'shift'], 'p', lazy.function(focus_main)),
]

mouse = [
        Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
        Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
        Click([mod], "Button2", lazy.window.bring_to_front()),
        ]

