from libqtile.config import DropDown
from .variables import home, sterm
scratchpads = [
        DropDown(
            'term', 
            'alacritty -t scratchpad',
            y=0,
            ),
        DropDown(
            'trayer', 
            'trayer --widthtype pixel --transparent true --alpha 255 --distance 10',
            y=0,
            on_focus_lost_hide=True
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
            f'{sterm} -T scratchpad -e taskwarrior-tui',
            height=0.995,
            width=0.3,
            opacity=0.5,
            x=0.698,
            y=0,
            on_focus_lost_hide=False
            ),
        DropDown(
            'Kuro',
            'kuro',
            height=0.9,
            width=0.3,
            opacity=0.1,
            x=0.68,
            y=0.05,
            on_focus_lost_hide=False
            ),
        DropDown(
            'noi',
            'Noi_linux_0.4.0.AppImage',
            match='noi',
            height=0.9,
            width=0.5,
            x=0.8,
            y=0.4,
            on_focus_lost_hide=False
            ),
        DropDown(
            'btop',
            f'{sterm} -T scratchpad -e btop',
            height=0.9,
            width=0.9,
            opacity=0.5,
            x=0.05,
            y=0.03,
            on_focus_lost_hide=True
            ),
        DropDown(
                'nnn',
                f'{sterm} -T scratchpad -e nnn',
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
                width=0.4,
                opacity=0.5,
                on_focus_lost_hide=False,
                x=0.8,
                y=0,
                ),
        DropDown(
                'tt',
                f'{sterm} -T scratchpad -e tt -t 60',
                height=0.9,
                width=0.9,
                opacity=0.5,
                x=0.05,
                y=0.03,
                on_focus_lost_hide=False
                ),
        DropDown(
                'neorg', 
                f'{sterm} -T scratchpad -e {home}.local/bin/lvim -c ":Neorg workspace home"', 
                height=0.9,
                width=0.5,
                opacity=0.5,
                x=0.8,
                y=0.0,
                relative=True,
                on_focus_lost_hide=False
                ),
        ]

