from libqtile.config import DropDown, Match
from .variables import HOME, sterm, scratch_zellij, calc, neorg_habits, neorg

calculator = DropDown(
    "calc",
    f'st -t to_top -f "CaskaydiaCove Nerd Font Mono:pixelsize=25" -e {calc}',
    height=0.2,
    width=0.5,
    x=0.25,
    y=0.02,
)

dropdown_terminal = DropDown(
    "term",
    f"alacritty -t to_top --config-file {
        HOME}/.config/alacritty/scratchpad.toml -e {scratch_zellij}",
    y=0.01,
    x=0.050,
    height=0.6,
    width=0.9,
)

countdown = DropDown(
    "countdown",
    'st -t to_top -f "CaskaydiaCove Nerd Font Mono:pixelsize=25" -e tclock_timer.sh',
    height=0.4,
    width=0.5,
    x=0.25,
    y=0.02,
)

trayer = DropDown(
    "trayer",
    "trayer --widthtype pixel --transparent true --alpha 255 --distance 10",
    y=0,
    on_focus_lost_hide=True,
)

todo = DropDown(
    "task",
    f"{sterm} -T scratchpad -c left_side -e taskwarrior-tui",
    height=0.940,
    width=0.3,
    opacity=0.5,
    x=0.02,
    y=0.01,
    on_focus_lost_hide=False,
)

aichat = DropDown(
    "ai",
    f"{sterm} -T scratchpad -c right_side -e aichat",
    height=0.940,
    width=0.3,
    opacity=0.5,
    x=0.690,
    y=0.01,
    on_focus_lost_hide=False,
)

pulsemixer = DropDown(
    "pulsemixer",
    f"{sterm} -T scratchpad -c right_side -e pulsemixer",
    height=0.5,
    width=0.3,
    opacity=0.5,
    x=0.690,
    y=0.01,
    on_focus_lost_hide=False,
)

whatsapp = DropDown(
    "zap",
    "wasistlos",
    match=Match(wm_class=["Wasistlos"][0]),
    height=0.9,
    width=0.8,
    y=0.03,
    on_focus_lost_hide=False,
)

btop = DropDown(
    "btop",
    f"{sterm} -T scratchpad -e btop",
    height=0.9,
    width=0.9,
    x=0.05,
    y=0.03,
    on_focus_lost_hide=True,
)

yazy = DropDown(
    "yazi",
    f"{sterm} -A 1 -t to_top -e yazi",
    height=0.9,
    width=0.9,
    opacity=0.5,
    x=0.05,
    y=0.03,
    on_focus_lost_hide=True,
)

cmus = DropDown(
    "cmus",
    f"{sterm} -T scratchpad -c cmus -e cmus",
    height=0.9,
    width=0.9,
    opacity=0.5,
    x=0.05,
    y=0.03,
    on_focus_lost_hide=True,
)

anki_portuguese = DropDown(
    "ankivPT",
    f'{sterm} -t "anki-vim" -e anki-vim portuguese',
    height=0.5,
    width=0.9,
    opacity=0.5,
    x=0.05,
    y=0.45,
    on_focus_lost_hide=True,
)

anki_english = DropDown(
    "ankivEN",
    f'{sterm} -t "anki-vim" -e anki-vim english',
    height=0.5,
    width=0.9,
    opacity=0.5,
    x=0.05,
    y=0.45,
    on_focus_lost_hide=True,
)

vimiv = DropDown(
    "vimiv",
    f"vimiv {HOME}.code/",
    height=0.9,
    width=0.7,
    opacity=0.5,
    on_focus_lost_hide=False,
    x=0.15,
    y=0.02,
)

typing_test = DropDown(
    "tt",
    f"{sterm} -T scratchpad -e tt -t 60",
    height=0.9,
    width=0.9,
    opacity=0.5,
    x=0.05,
    y=0.03,
    on_focus_lost_hide=False,
)

note_taking = DropDown(
    "notes",
    neorg,
    height=0.5,
    width=0.9,
    opacity=0.5,
    x=0.05,
    y=0.03,
    on_focus_lost_hide=False,
)

habit_tracking = DropDown(
    "habits",
    neorg_habits,
    height=0.5,
    width=0.5,
    opacity=0.5,
    x=0.25,
    y=0.2,
    on_focus_lost_hide=False,
)

scratchpads = [
    dropdown_terminal,
    calculator,
    countdown,
    trayer,
    todo,
    aichat,
    pulsemixer,
    whatsapp,
    btop,
    yazy,
    cmus,
    anki_portuguese,
    anki_english,
    vimiv,
    typing_test,
    note_taking,
    habit_tracking,
]
