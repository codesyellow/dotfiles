import re
from libqtile.config import Group, ScratchPad, Match
from .variables import icons
from .scratchpads import scratchpads
from .rules import (
    wks1class_rules,
    wks2class_rules,
    wks3class_rules,
    wks4class_rules,
    wks5class_rules,
    wks6class_rules,
    wks7class_rules,
    wks2title_rules,
    wks4title_rules,
)

groups = [
    Group(
        icons[0],
        matches=[Match(wm_class=re.compile(rf"^({wks1class_rules})$"))],
    ),
    Group(
        icons[1],
        matches=[
            Match(wm_class=re.compile(rf"^({wks2class_rules})$")),
            Match(title=re.compile(rf"^({wks2title_rules})$")),
        ],
    ),
    Group(
        icons[2],
        matches=[Match(wm_class=re.compile(rf"^({wks3class_rules})$"))],
    ),
    Group(
        icons[3],
        matches=[
            Match(wm_class=re.compile(rf"^({wks4class_rules})$")),
            Match(title=re.compile(rf"^({wks4title_rules})$")),
        ],
    ),
    Group(
        icons[4],
        matches=[Match(wm_class=re.compile(rf"^({wks5class_rules})$"))],
    ),
    Group(
        icons[5],
        matches=[Match(wm_class=re.compile(rf"^({wks6class_rules})$"))],
    ),
    Group(
        icons[6],
        matches=[Match(wm_class=re.compile(rf"^({wks7class_rules})$"))],
    ),
    ScratchPad("scratchpad", scratchpads),
]
