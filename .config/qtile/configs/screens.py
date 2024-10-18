from libqtile.config import Screen 
from libqtile import bar
from .widgets import my_widgets

screens = [
        Screen(
            top=bar.Bar(
                my_widgets
                ,
                20,
                background='#2e3440',
                ),
            ),
        ]
