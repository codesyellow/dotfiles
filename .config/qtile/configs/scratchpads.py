from libqtile.config import DropDown
from .variables import home
scratchpads = [
        # add a alternative config file for transparency to work properly on wayland
        DropDown(
            'term', 
            f'alacritty --config-file {home}.config/alacritty/alacritty2.yml -t scratchpad',
            y=0,
            ),
        DropDown(
            'gpterm',
            'alacritty -t scratchpad -e bard-cli -i',
            height=0.995,
            width=0.3,
            opacity=0.5,
            x=0.698,
            y=0,
            on_focus_lost_hide=False
            ),
        DropDown(
            'task',
            'st -T scratchpad -e taskwarrior-tui',
            height=0.995,
            width=0.3,
            opacity=0.5,
            x=0.698,
            y=0,
            on_focus_lost_hide=False
            ),
        DropDown(
            'btop',
            'st -T scratchpad -e btop',
            height=0.9,
            width=0.9,
            opacity=0.5,
            x=0.05,
            y=0.03,
            on_focus_lost_hide=False
            ),
        DropDown(
            'tt',
            'st -T scratchpad -e tt -t 60',
            height=0.9,
            width=0.9,
            opacity=0.5,
            x=0.05,
            y=0.03,
            on_focus_lost_hide=False
            ),
        DropDown(
            'neorg', 
            'st -T scratchpad -e /home/cie/.local/bin/lvim -c ":Neorg workspace home"', 
            x=0.001,
            height=0.992,
            width=0.3,
            opacity=0.9,
            on_focus_lost_hide=False),
        ]

