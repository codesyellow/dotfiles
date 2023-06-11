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
            'alacritty -t scratchpad -e python3 -m EdgeGPT.EdgeGPT',
            height=0.995,
            width=0.3,
            opacity=0.5,
            x=0.698,
            y=0,
            on_focus_lost_hide=False
            ),
        DropDown(
            'translator',
            "alacritty -t scratchpad -e python3 -m EdgeGPT.EdgeGPT --prompt 'I want you to act as an English translator, spelling corrector and improver. I will speak to you in any language and you will detect the language, translate it and answer in the corrected and improved version of my text, in English. I want you to replace my simplified A0-level words and sentences with more beautiful and elegant, upper level English words and sentences. Keep the meaning same, but make them more literary. I want you to only reply the correction, the improvements and nothing else, do not write explanations.",
            height=0.5,
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
