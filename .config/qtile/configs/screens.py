from libqtile.config import Screen
from libqtile import bar 
from .widgets import my_widgets

screens = [
        Screen(
            bottom=bar.Bar(
                my_widgets
                ,
                20,
                ),
            ),
        ]

