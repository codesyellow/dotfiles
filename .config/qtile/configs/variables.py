import os
from libqtile.config import Match
from libqtile import layout, qtile

alt_mod = "mod1"
bg = '#2e3440'
fg = '#d8dee9'
al = '#EF5A6F'
browser = 'firefox'
exit_icon_font = 'Font Awesome 6 Free Regular'
icons = [
        '',
        '',
        '',
        ' ',
        ' ',
        '<span size="14000"> </span>',
        ]
widget_icons = [
        '   ',
        '  ',
        '<span size="13000"> </span>',
        '<span size="13000"> </span>',
        ]
home = os.path.expanduser('~/')
mod = "mod4"
pad = 10
group_font = 'Font Awesome 6 Free Regular'
my_font = 'JetBrainMono Nerd Font'
runner = ''
sterm = ''
wsize = 18
if qtile.core.name == "x11":
    sterm = 'st'
if qtile.core.name == "wayland":
    sterm = 'alacritty'

if qtile.core.name == "x11":
    runner = f"dmenu_run -nb {bg} -z 530 -x 220 -y 0 -sb {bg} -shb {bg} -nhb {bg} -shf {al} -nhf {al} -fn dmenufont -p  "
elif qtile.core.name == "wayland":
    runner = f"bemenu-run -c -l 10 -i -M 300 --fn 'IBM Plex Mono 14' -p '' --hp 8 --nb {bg} --nf '#fff' --ab {bg} -- │ hf {bg} --hb {bg} --fb {bg} -B 1 --bdr {bg}"
term = "alacritty"

# qtile default variables
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
        float_rules=[
            # Run the utility of `xprop` to see the wm class and name of an X client.
            *layout.Floating.default_float_rules,
            Match(wm_class="confirmreset"),  # gitk
            Match(wm_class="makebranch"),  # gitk
            Match(wm_class="maketag"),  # gitk
            Match(wm_class="ssh-askpass"),  # ssh-askpass
            Match(title="branchdialog"),  # gitk
            Match(title="pinentry"),  # GPG key password entry
            Match(wm_class='blueman-manager'),
            Match(wm_class='org.kde.polkit-kde-authentication-agent-1'),
            Match(wm_class='CachyOSHello'),
            Match(wm_class='org.cachyos.cachyos-kernel-manager'),
            Match(title='anki-vim'),
            Match(title='maps'),
            ]
        )
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"
