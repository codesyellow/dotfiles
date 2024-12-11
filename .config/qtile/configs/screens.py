from libqtile.config import Screen
from libqtile import bar
from .widgets import my_widgets
from .variables import COLORS

screens = [
    Screen(
        top=bar.Bar(
            my_widgets,
            20,
            background=COLORS["bg_color"],
        ),
    ),
]
