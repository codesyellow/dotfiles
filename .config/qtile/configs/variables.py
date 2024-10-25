import os
from libqtile import layout, qtile

alt_mod = "mod3"
bg = '#2e3440'
fg = '#d8dee9'
al = '#EF5A6F'
browser = 'com.brave.Browser'
exit_icon_font = 'Font Awesome 6 Free Regular'
icons = [
        '<span size="14000"></span> ',
        '',
        '<span size="15000"></span>',
        '<span size="15000"></span>',
        '<span size="15000" rise="3000"></span> ',
        '<span size="14000"></span>',
        ]
widget_icons = [
        '   ',
        '  ',
        '<span size="12000"> </span>',
        '<span foreground="#EF5A6F" size="12000"> </span>',
        ]
home = os.path.expanduser('~/')
mod = "mod4"
pad = 10
group_font = 'Font Awesome 6 Free Regular'
runner = ''
sterm = ''
wsize = 18
if qtile.core.name == "x11":
    sterm = 'st'
if qtile.core.name == "wayland":
    sterm = 'alacritty'

if qtile.core.name == "x11":
    runner = f"dmenu_run -nb {bg} -z 540 -x 215 -y -1 -sb {bg} -shb {bg} -nhb {bg} -shf {al} -nhf {al} -fn dmenufont -p "
elif qtile.core.name == "wayland":
    runner = f"bemenu-run -c -l 10 -i -M 300 --fn 'IBM Plex Mono 14' -p '' --hp 8 --nb {bg} --nf '#fff' --ab {bg} -- │ hf {bg} --hb {bg} --fb {bg} -B 1 --bdr {bg}"
term = "alacritty"

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
