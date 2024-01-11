from libqtile.config import DropDown
from .variables import home
scratchpads = [
        DropDown(
            'term', 
            'alacritty -t scratchpad',
            y=0,
            ),
        DropDown(
            'gpterm',
            f'alacritty -t scratchpad -e {home}.local/share/cargo/bin/bard-rs -e {home}.env-bard',
            height=0.995,
            width=0.3,
            opacity=0.5,
            x=0.698,
            y=0,
            on_focus_lost_hide=False
            ),
        DropDown(
            'task',
            'foot -T scratchpad -e taskwarrior-tui',
            height=0.995,
            width=0.3,
            opacity=0.5,
            x=0.698,
            y=0,
            on_focus_lost_hide=False
            ),
        DropDown(
            'btop',
            'foot -T scratchpad -e btop',
            height=0.9,
            width=0.9,
            opacity=0.5,
            x=0.05,
            y=0.03,
            on_focus_lost_hide=False
            ),
        DropDown(
            'nnn',
            'foot -T scratchpad -e nnn',
            height=0.9,
            width=0.9,
            opacity=0.5,
            x=0.05,
            y=0.03,
            on_focus_lost_hide=False
            ),
        DropDown(
            'vimiv',
            f'vimiv {home}.code/',
            height=0.9,
            width=0.9,
            opacity=0.5,
            x=0.05,
            y=0.03,
            on_focus_lost_hide=False
            ),
        DropDown(
                'tt',
                'foot -T scratchpad -e tt -t 60',
                height=0.9,
                width=0.9,
                opacity=0.5,
                x=0.05,
                y=0.03,
                on_focus_lost_hide=False
                ),
        DropDown(
                'neorg', 
                f'foot -T scratchpad -e {home}.local/bin/lvim -c ":Neorg workspace home"', 
                height=0.9,
                width=0.9,
                opacity=0.5,
                x=0.05,
                y=0.03,
                on_focus_lost_hide=False
                ),
        ]

