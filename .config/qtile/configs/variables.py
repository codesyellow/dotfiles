import os
from libqtile import qtile

browser = 'brave'
mod = 'mod4'
alt_mod = 'mod1'
icons = [
    '',
    '',
    '',
    '',
    '',
    '',
    '',
]
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
my_font = 'JetBrainMono Nerd Font'
pad = 10
runner = f'dmenu_run -dim 0.3 -fn "{my_font}"'
terminal = 'alacritty'
home = os.path.expanduser('~/')
if qtile.core.name == "x11":
    runner = f'dmenu_run -dim 0.3 -fn "{my_font}"'
elif qtile.core.name == "wayland":
    runner = 'kickoff'

