import os
from libqtile.config import Match
from libqtile import layout, qtile

alt_mod = "mod1"
bg = '#00000095'
browser = 'floorp'
colors = ['#1E2326', # bg_dim 0
          '#272E33', # bg0 1
          '#2E383C', # bg1 2
          '#374145', # bg2 3
          '#414B50', # bg3 4
          '#495156', # bg4 5
          '#4F5B58', # bg5 6
          '#4C3743', # bg_red 7
          '#493B40', # bg_visual 8
          '#45443C', # bg_yellow 9
          '#3C4841', # bg_green 10
          '#384B55', # bg_blue 11
          '#E67E80', # red 12
          '#E69875', # orange 13
          '#DBBC7F', # yellow 14
          '#A7C080', # green 15
          '#7FBBB3', # blue 16
          '#83C092', # aqua 17
          '#D699B6', # purple 18
          '#D3C6AA', # fg 19
          '#A7C080', # statusline1 20
          '#D3C6AA', # statusline2 21
          '#E67E80', # statusline3 22
          '#7A8478', # gray0 23
          '#859289', # gray1 24
          '#9DA9A0', # gray2 25
          ]
exit_icon_font = 'Font Awesome 6 Free Regular'
icons = [
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        ]
widget_icons = [
        ' ',
        ' ',
        '',
        '',
        '',
        '',
        '',
        ]
home = os.path.expanduser('~/')
#runner = "dmenu_run -nb '#272E33' -nf '#D3C6AA' -sb '#D3C6AA' -sf '#1E2326' -fn '' -dim 0.2"
# variables
mod = "mod4"
pad = 10
group_font = 'Font Awesome 6 Free Regular'
my_font = 'JetBrainMono Nerd Font'
runner = ''
sterm = ''
if qtile.core.name == "x11":
    sterm = 'st'
if qtile.core.name == "wayland":
    sterm = 'foot'

if qtile.core.name == "x11":
    runner = 'dmenu_run'
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
