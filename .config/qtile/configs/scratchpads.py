from os import altsep, name
from libqtile.config import DropDown, Match
from .variables import HOME, ALT_TERM, ZELLIJ_SCRATCHPAD
from .functions import get_terminal

calculator = DropDown(
    "calc",
    f'{get_terminal(terminal=ALT_TERM, name="from_top",
                    font_size=25)} -e python -ic ""',
    height=0.2,
    width=0.5,
    x=0.25,
    y=0.02,
)

dropdown_terminal = DropDown(
    "term",
    f"{get_terminal(terminal=ALT_TERM, name="from_top",
                    font_size=16)} -A 0.7 -e {ZELLIJ_SCRATCHPAD}",
    y=0.01,
    x=0.050,
    height=0.6,
    width=0.9,
)

countdown = DropDown(
    "countdown",
    f'{get_terminal(terminal=ALT_TERM, name="from_top",
                    font_size=25)} -e tclock_timer.sh',
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
    f"{get_terminal(terminal=ALT_TERM, name="from_left",
                    font_size=16)} -e taskwarrior-tui",
    height=0.940,
    width=0.3,
    opacity=0.5,
    x=0.02,
    y=0.01,
    on_focus_lost_hide=False,
)

aichat = DropDown(
    "ai",
    f"{get_terminal(terminal=ALT_TERM, name="from_right",
                    font_size=16)} -e aichat",
    height=0.940,
    width=0.3,
    opacity=0.5,
    x=0.690,
    y=0.01,
    on_focus_lost_hide=False,
)

pulsemixer = DropDown(
    "pulsemixer",
    f"{get_terminal(terminal=ALT_TERM, name="from_right",
                    font_size=18)} -e pulsemixer",
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
    f"{get_terminal(terminal=ALT_TERM, name="from_bottom",
                    font_size=16)} -e btop",
    height=0.9,
    width=0.9,
    x=0.05,
    y=0.03,
    on_focus_lost_hide=True,
)

yazy = DropDown(
    "yazi",
    f"{get_terminal(terminal=ALT_TERM, name="from_top",
                    font_size=16)} -e yazi",
    height=0.9,
    width=0.9,
    opacity=0.5,
    x=0.05,
    y=0.03,
    on_focus_lost_hide=True,
)

cmus = DropDown(
    "cmus",
    f"{get_terminal(terminal=ALT_TERM, name="from_top",
                    font_size=18)} -T scratchpad -c cmus -e cmus",
    height=0.9,
    width=0.9,
    opacity=0.5,
    x=0.05,
    y=0.03,
    on_focus_lost_hide=True,
)

anki_portuguese = DropDown(
    "ankivPT",
    f'{get_terminal(terminal=ALT_TERM, name="from_bottom",
                    font_size=16)} -e anki-vim portuguese',
    height=0.5,
    width=0.9,
    opacity=0.5,
    x=0.05,
    y=0.45,
    on_focus_lost_hide=True,
)

anki_english = DropDown(
    "ankivEN",
    f'{get_terminal(terminal=ALT_TERM, name="from_bottom",
                    font_size=16)} -e anki-vim english',
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
    f"{ALT_TERM} -T scratchpad -e tt -t 60",
    height=0.9,
    width=0.9,
    opacity=0.5,
    x=0.05,
    y=0.03,
    on_focus_lost_hide=False,
)

note_taking = DropDown(
    "notes",
    f"{get_terminal(ALT_TERM, name="from_top", font_size=16)
       } -e nvim {HOME}.notes/index.norg",
    height=0.5,
    width=0.9,
    opacity=0.5,
    x=0.05,
    y=0.03,
    on_focus_lost_hide=False,
)

habit_tracking = DropDown(
    "habits",
    f"{get_terminal(terminal=ALT_TERM, name="from_top",
                    font_size=18)}  -e nvim {HOME}.notes/habits.norg",
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
