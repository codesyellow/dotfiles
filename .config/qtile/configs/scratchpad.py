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
            'alacritty -t scratchpad -e edge-gpt',
            height=0.995,
            width=0.3,
            opacity=0.5,
            x=0.698,
            y=0,
            on_focus_lost_hide=False
            ),
        DropDown(
            'neorg', 
            'alacritty -t scratchpad -e nvim', 
            x=0.001,
            height=0.992,
            width=0.3,
            opacity=0.9,
            on_focus_lost_hide=False),
        ]
