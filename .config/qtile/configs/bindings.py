from libqtile.config import Key, KeyChord, Drag, Click
from libqtile.lazy import lazy
from .variables import mod, terminal, alt_mod, runner, browser
from .functions import latest_group, focus_main

# bindings
keys = [
    Key([mod], 'h', lazy.layout.left()),
    Key([mod], 'l', lazy.layout.right()),
    Key([mod], 'j', lazy.layout.down()),
    Key([mod], 'k', lazy.layout.up()),
    Key([mod, 'shift'], 'h', lazy.layout.swap_left()),
    Key([mod, 'shift'], 'l', lazy.layout.swap_right()),
    Key([mod, 'shift'], 'j', lazy.layout.shuffle_down()),
    Key([mod, 'shift'], 'k', lazy.layout.shuffle_up()),
    Key([mod], 'i', lazy.layout.grow()),
    Key([mod], 'm', lazy.layout.shrink()),
    Key([mod], 'n', lazy.layout.normalize()),
    Key([mod], 'o', lazy.layout.maximize()),
    Key([mod], '9', lazy.layout.reset()),
    Key([mod, 'shift'], 's', lazy.layout.swap_main()),
    Key([mod, 'shift'], 'space', lazy.layout.flip()),
    Key([mod, 'shift'], 'Return', lazy.layout.toggle_split()),
    Key([mod], 't', lazy.spawn(terminal)),
    Key([alt_mod], 't', lazy.spawn(terminal)),
    Key([mod], '0', lazy.next_layout()),
    Key([mod, 'shift'], 'c', lazy.window.kill()),
    Key([mod, 'control'], 'r', lazy.reload_config()),
    Key([alt_mod, 'control'], 'r', lazy.reload_config()),
    Key([mod, 'control'], 'q', lazy.shutdown()),
    Key([mod], 'r', lazy.spawncmd()),
    Key([mod], 'b', lazy.group.focus_back()),
    # apps
    Key([mod], 'w', lazy.spawn(browser)),
    Key([mod], 'f', lazy.window.toggle_fullscreen()),
    Key([mod, 'shift'], 'f', lazy.window.toggle_floating()),
    Key([mod], 'c', lazy.window.center()),
    Key([mod, 'shift'], 'm', lazy.spawn('alacritty -t fm-video -e lf /home/cse/.courses')),
    Key([mod, 'shift'], 'e', lazy.core.change_vt(2)),
    Key([mod], 'd', lazy.spawn(runner)),
    Key([alt_mod], 'd', lazy.spawn(runner)),
    Key([mod, 'shift'], 'a', lazy.spawn('volume.sh up')),
    Key([mod, 'shift'], 'd', lazy.spawn('volume.sh down')),
    Key([alt_mod, 'shift'], 'a', lazy.spawn('volume.sh up')),
    Key([alt_mod, 'shift'], 'd', lazy.spawn('volume.sh down')),
    Key([mod, 'shift'], 't', lazy.spawn(terminal + ' --config-file /home/cse/.config/alacritty/clima.yml -t clima')),
    Key([mod], 'Tab', lazy.function(latest_group)),
    Key([mod, 'shift'], 'p', lazy.function(focus_main)),
    KeyChord([mod], 's', [
        Key([], 'u', lazy.group['scratchpad'].dropdown_toggle('term')),
        Key([], 'g', lazy.group['scratchpad'].dropdown_toggle('gpterm')),
        Key([], 't', lazy.group['scratchpad'].dropdown_toggle('trayer')),
        Key([], 'm', lazy.group['scratchpad'].dropdown_toggle('btop')),
    ]),
    # actions
    KeyChord([mod], 'a', [
        Key([], 'h', lazy.core.hide_cursor()),
        Key([], 's', lazy.core.unhide_cursor()),
        Key([], 'e', lazy.spawn('easyeffects -l LoudnessEqualizer')),
        Key([], 'b', lazy.spawn('easyeffects -l "Heavy Bass"')),
        KeyChord([], 'l', [
            Key([], 'o', lazy.spawn('xset led on')),
            Key([], 'f', lazy.spawn('xset led off')),
            ])
    ]),
]

mouse = [
    Drag([mod], 'Button1', lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], 'Button3', lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], 'Button2', lazy.window.bring_to_front()),
]
