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
        layout="max",
        matches=[Match(wm_class=re.compile(rf"^({wks1class_rules})$"))],
    ),
    Group(
        icons[1],
        layout="max",
        matches=[
            Match(wm_class=re.compile(rf"^({wks2class_rules})$")),
            Match(title=re.compile(rf"^({wks2title_rules})$")),
        ],
    ),
    Group(
        icons[2],
        layout="max",
        matches=[Match(wm_class=re.compile(rf"^({wks3class_rules})$"))],
    ),
    Group(
        icons[3],
        layout="max",
        matches=[
            Match(wm_class=re.compile(rf"^({wks4class_rules})$")),
            Match(title=re.compile(rf"^({wks4title_rules})$")),
        ],
    ),
    Group(
        icons[4],
        layout="max",
        matches=[Match(wm_class=re.compile(rf"^({wks5class_rules})$"))],
    ),
    Group(
        icons[5],
        layout="max",
        matches=[Match(wm_class=re.compile(rf"^({wks6class_rules})$"))],
    ),
    Group(
        icons[6],
        layout="max",
        matches=[Match(wm_class=re.compile(rf"^({wks7class_rules})$"))],
    ),
    ScratchPad("scratchpad", scratchpads),
]
