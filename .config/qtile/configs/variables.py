import os

FONT = "Symbols Nerd Font"
RUNNER = "rofi -show run"
TERM = "kitty"
ALT_MOD = "mod1"
COLORS = {
    "bg": "#2e3440",
    "fg": "#d8dee9",
    "alt": "#FF748B",
    "bg1": "#4c566a",
}
MOD = "mod4"
WSIZE = 18
BROWSER = "brave"
HOME = os.path.expanduser("~/")
TMUX_SCRATCHPAD = "bash -c 'tmux attach-session -t scratch || tmux new-session -s scratch'"
ZELLIJ_SCRATCHPAD = "bash -c 'zellij a scratch || zellij -s scratch'"
VERTICAL_MONITOR_GROUPS = [
    "",
    "",
    "",
]
GROUP_ICONS = [
    "",
    "",
    "<span size='12000' rise='-15900'></span>",
    "",
    "",
]
ALT_TERM = "st"

# qtile default variables
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"
