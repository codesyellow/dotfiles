from libqtile.config import DropDown, Match
from .variables import home, sterm
from libqtile.log_utils import logger
scratchpads = [
    DropDown(
        'term',
        f'alacritty -t scratchpad --config-file {home}.config/alacritty/scratchpad.toml',
        y=0.48,
        height=0.5,
    ),
    DropDown(
        'trayer',
        'trayer --widthtype pixel --transparent true --alpha 255 --distance 10',
        y=0,
        on_focus_lost_hide=True
    ),
    DropDown(
        'task',
        f'{sterm} -T scratchpad -c right_side -e taskwarrior-tui',
        height=0.940,
        width=0.3,
        opacity=0.5,
        x=0.690,
        y=0.01,
        on_focus_lost_hide=False
    ),
    DropDown(
        'ai',
        f'{sterm} -T scratchpad -c right_side -e aichat',
        height=0.940,
        width=0.3,
        opacity=0.5,
        x=0.690,
        y=0.01,
        on_focus_lost_hide=False
    ),
    DropDown(
        'pulsemixer',
        f'{sterm} -T scratchpad -c right_side -e pulsemixer',
        height=0.5,
        width=0.3,
        opacity=0.5,
        x=0.690,
        y=0.01,
        on_focus_lost_hide=False
    ),
    DropDown(
        'zap',
        'flatpak run com.github.eneshecan.WhatsAppForLinux',
        match=Match(wm_class=['Whatsapp-for-linux'][0]),
        height=0.9,
        width=0.8,
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
        'yazi',
        f'{sterm} -T scratchpad -e yazi',
        height=0.9,
        width=0.9,
        opacity=0.5,
        x=0.05,
        y=0.03,
        on_focus_lost_hide=True
    ),
    DropDown(
        'cmus',
        f'{sterm} -T scratchpad -e cmus',
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
        'notes',
        f'{sterm} -T scratchpad -e vim {home}.vimwiki/notes/index.wiki',
        height=0.9,
        width=0.9,
        opacity=0.5,
        x=0.05,
        y=0.03,
        on_focus_lost_hide=False
    ),
    DropDown(
        'habits',
        f'{sterm} -T scratchpad -e vim {home}.vimwiki/habits/index.wiki',
        height=0.5,
        width=0.5,
        opacity=0.5,
        x=0.25,
        y=0.2,
        on_focus_lost_hide=False
    )]

