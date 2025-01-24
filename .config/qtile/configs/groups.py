import re
from libqtile.config import Group, ScratchPad, Match
from .variables import GROUP_ICONS, VERTICAL_MONITOR_GROUPS
from .scratchpads import scratchpads
from .rules import (
    wks2class_rules,
    wks3class_rules,
    wks4class_rules,
    wks6class_rules,
    wks7class_rules,
    wks2title_rules,
    wks4title_rules,
    vertical_browser_rules,
    vertical_reading_rules,
    vertical_terminal_rules,
)

groups = [
    Group(
        VERTICAL_MONITOR_GROUPS[0],
        matches=[Match(wm_class=re.compile(
            rf"^({vertical_terminal_rules})$"))],
        screen_affinity=1
    ),
    Group(
        VERTICAL_MONITOR_GROUPS[1],
        matches=[Match(wm_class=re.compile(rf"^({vertical_browser_rules})$"))],
        screen_affinity=1
    ),
    Group(
        VERTICAL_MONITOR_GROUPS[2],
        matches=[Match(wm_class=re.compile(rf"^({vertical_reading_rules})$"))],
        screen_affinity=1
    ),
    Group(
        GROUP_ICONS[0],
        matches=[
            Match(wm_class=re.compile(rf"^({wks2class_rules})$")),
            Match(title=re.compile(rf"^({wks2title_rules})$")),
        ],
        screen_affinity=0
    ),
    Group(
        GROUP_ICONS[1],
        matches=[Match(wm_class=re.compile(rf"^({wks3class_rules})$"))],
        screen_affinity=0
    ),
    Group(
        GROUP_ICONS[2],
        matches=[
            Match(wm_class=re.compile(rf"^({wks4class_rules})$")),
            Match(title=re.compile(rf"^({wks4title_rules})$")),
        ],
        screen_affinity=0
    ),
    Group(
        GROUP_ICONS[3],
        matches=[Match(wm_class=re.compile(rf"^({wks6class_rules})$"))],
        screen_affinity=0
    ),
    Group(
        GROUP_ICONS[4],
        matches=[Match(wm_class=re.compile(rf"^({wks7class_rules})$"))],
        screen_affinity=0
    ),
    ScratchPad("scratchpad", scratchpads),
]
