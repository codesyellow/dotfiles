import os

alt_mod = "mod3"
term = "kitty"
colors = {
    "bg_color": "#2e3440",
    "fg_color": "#d8dee9",
    "alt_color": "#EF5A6F",
    "bg1_color": "#4c566a",
}
scratch_tmux = "tmux attach-session -t scratch || tmux new-session -s scratch"
scratch_zellij = "zellij -s scratch"
tmux_term = f"{term} -T tmux -e tmux"
zellij_term = f"{term} -T zellij -e zellij"
calc = "python -ic """
browser = "com.brave.Browser"
exit_icon_font = "Font Awesome 6 Free Regular"
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
    "   ",
    "  ",
    '<span size="12000"> </span>',
    '<span foreground="#EF5A6F" size="12000"> </span>',
]
home = os.path.expanduser("~/")
mod = "mod4"
pad = 10
group_font = " Symbols Nerd Font"
runner = "rofi -show run"
sterm = "st"
wsize = 18

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
