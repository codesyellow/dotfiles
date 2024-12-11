from logging import Logger
import os
from libqtile.log_utils import logger

FONT = "Symbols Nerd Font"
RUNNER = "rofi -show run"
TERM = "kitty"
ALT_MOD = "mod3"
COLORS = {
    "bg_color": "#2e3440",
    "fg_color": "#d8dee9",
    "alt_color": "#EF5A6F",
    "bg1_color": "#4c566a",
}
MOD = "mod4"
WSIZE = 18
BROWSER = "brave"
HOME = os.path.expanduser("~/")
log = logger
scratch_tmux = "tmux attach-session -t scratch || tmux new-session -s scratch"
scratch_zellij = "zellij -s scratch"
vimwiki = f"{TERM} -T scratchpad -e vim {HOME}.vimwiki/notes/index.wiki"
neorg = f"{TERM} -T to_top -e nvim {HOME}.notes/index.norg"
neorg_habits = f"{TERM} -T scratchpad -e nvim {HOME}.notes/habits.norg"
tmux_term = f"{TERM} -T tmux -e tmux"
zellij_term = f"{TERM} -T zellij -e zellij"
calc = "python -ic """
icons = [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
]
widget_icons = [
    '<span size="12000"> </span>',
    '<span foreground="#EF5A6F" size="12000"> </span>',
]
pad = 10
sterm = "st"

# qtile default variables
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"
