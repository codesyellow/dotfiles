from libqtile.lazy import lazy
from libqtile.config import Click, Drag, Key
from .variables import MOD, ALT_MOD, TERM

keys = [
    Key([MOD], "j", lazy.group.next_window()),
    Key([MOD], "k", lazy.group.prev_window()),
    Key([MOD, "shift"], "k", lazy.layout.shuffle_down()),
    Key([MOD, "shift"], "j", lazy.layout.shuffle_up()),
    Key([MOD, "control"], "r", lazy.reload_config()),
    Key([MOD, "control"], "q", lazy.shutdown()),
    Key([MOD], "f", lazy.window.toggle_fullscreen()),
    Key([MOD], 'l', lazy.next_screen()),
    Key([MOD], 'h', lazy.prev_screen()),
    Key([MOD, "shift"], "f", lazy.window.toggle_floating()),
    Key([MOD], "c", lazy.window.center()),
    Key([MOD, "shift"], "e", lazy.core.change_vt(2)),
    Key([MOD], "Tab", lazy.screen.toggle_group()),
    Key([MOD], "t", lazy.spawn(f"{TERM} -T zellij -e zellij")),
    # Key([MOD], "t", lazy.spawn(f"{TERM} -T tmux -e tmux")),
    Key([MOD], "return", lazy.spawn(TERM)),
    Key([ALT_MOD], "t", lazy.spawn(TERM)),
]

mouse = [
    Drag(
        [MOD],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [MOD], "Button3", lazy.window.set_size_floating(),
        start=lazy.window.get_size()
    ),
    Click([MOD], "Button2", lazy.window.bring_to_front()),
]
