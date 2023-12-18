import os
from libqtile.config import Match
from libqtile import layout

alt_mod = "mod1"
bg = '#00000090'
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
        'WWW',
        '</>',
        'VID',
        'BOOKS',
        'EDIT',
        'TERMINAL',
        'GAMES',
        'ANDROID',
        ]
home = os.path.expanduser('~/')
#runner = "dmenu_run -nb '#272E33' -nf '#D3C6AA' -sb '#D3C6AA' -sf '#1E2326' -fn 'JetBrainMono Nerd Font' -dim 0.2"
# variables
mod = "mod4"
my_font = 'JetBrainMono Nerd Font'
pad = 10
runner = "bemenu-run -c -l 10 -i -M 300 --fn 'IBM Plex Mono 14' -p '' --hp 8 --nb '#10000000' --nf '#fff' --ab '#66000000' -- │ hf '#66000000' --hb '#66000000' --fb '#66000000' -B 1 --bdr '#66000000'"
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
            ]
        )
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"
