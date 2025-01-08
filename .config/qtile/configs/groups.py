import re
from libqtile.config import Group, ScratchPad, Match
from .variables import GROUP_ICONS
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
        GROUP_ICONS[0],
        matches=[Match(wm_class=re.compile(rf"^({wks1class_rules})$"))],
        layout="max"
    ),
    Group(
        GROUP_ICONS[1],
        matches=[
            Match(wm_class=re.compile(rf"^({wks2class_rules})$")),
            Match(title=re.compile(rf"^({wks2title_rules})$")),
        ],
    ),
    Group(
        GROUP_ICONS[2],
        matches=[Match(wm_class=re.compile(rf"^({wks3class_rules})$"))],
    ),
    Group(
        GROUP_ICONS[3],
        matches=[
            Match(wm_class=re.compile(rf"^({wks4class_rules})$")),
            Match(title=re.compile(rf"^({wks4title_rules})$")),
        ],
    ),
    Group(
        GROUP_ICONS[4],
        matches=[Match(wm_class=re.compile(rf"^({wks5class_rules})$"))],
    ),
    Group(
        GROUP_ICONS[5],
        matches=[Match(wm_class=re.compile(rf"^({wks6class_rules})$"))],
    ),
    Group(
        GROUP_ICONS[6],
        layout="max",
        matches=[Match(wm_class=re.compile(rf"^({wks7class_rules})$"))],
    ),
    ScratchPad("scratchpad", scratchpads),
]
