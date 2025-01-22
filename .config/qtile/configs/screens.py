from libqtile.config import Screen
from libqtile import bar
from .widgets import my_widgets, vertical_widgets
from .variables import COLORS
from .custom_widgets import Custom_Widgets

custom_widgets = Custom_Widgets()
screens = [
    Screen(
        top=bar.Bar(
            my_widgets,
            26,
            background=COLORS["bg"],
        ),
    ),
    Screen(
        top=bar.Bar(
            vertical_widgets,
            26,
            background=COLORS["bg"],
        ),
    ),

]
