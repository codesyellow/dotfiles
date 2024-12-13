from libqtile import widget
from .variables import FONT, WSIZE, COLORS
from .custom_widgets import Custom_Widgets

custom_widgets = Custom_Widgets()

my_widgets = [
    widget.Volume(
        fontsize=18,
        fmt='<span size="24000" rise="4500" foreground="#d8dee9"></span> <span rise="9000" size="13500" foreground="#d8dee9">{}</span>',
        update_interval=5,
    ),
    widget.GenPollText(
        func=custom_widgets.mem_usage,
        fontsize=WSIZE,
        font=FONT,
        update_interval=15,
    ),
    widget.GenPollText(
        func=custom_widgets.cpu_usage,
        fontsize=WSIZE,
        font=FONT,
        update_interval=1,
    ),
    widget.GenPollText(
        func=custom_widgets.cpu_temp,
        font=FONT,
        padding=5,
        fontsize=WSIZE,
        update_interval=5,
    ),
    widget.GenPollText(
        func=custom_widgets.root_space,
        fontsize=WSIZE,
        font=FONT,
        update_interval=15,
    ),
    widget.GenPollText(
        func=custom_widgets.pomodoro,
        fontsize=WSIZE,
        font=FONT,
        update_interval=5,
    ),
    widget.GenPollText(
        func=custom_widgets.game_is_on,
        fontsize=WSIZE,
        font=FONT,
        update_interval=2,
    ),
    widget.GenPollText(
        func=custom_widgets.do_stretch,
        fontsize=WSIZE,
        update_interval=1,
    ),
    widget.Spacer(),
    widget.GroupBox(
        active=COLORS["fg"],
        block_highlight_text_color=COLORS["alt"],
        disable_drag=True,
        markup=True,
        spacing=2,
        highlight_method="text",
        this_current_screen_border=COLORS["alt"],
        urgent_text=COLORS["alt"],
        highlight_color=[COLORS["bg"], COLORS["alt"]],
        font=FONT,
        fontsize=WSIZE,
        inactive=COLORS["bg1"],
        foreground="#444",
        use_mouse_wheel=False,
    ),
    widget.Spacer(),
    widget.Chord(
        foreground=COLORS["alt"],
        fontsize=WSIZE,
        font=FONT,
    ),
    widget.QuickExit(
        default_text='<span size="12000"> </span>',
        countdown_format='<span foreground="#EF5A6F" size="12000"> </span>',
        countdown_start=10,
    ),
    widget.GenPollText(
        func=custom_widgets.easyeffects_is_on,
        fontsize=WSIZE,
        update_interval=2,
    ),
    widget.GenPollText(
        background=COLORS["bg"],
        func=custom_widgets.check_keyboard_variant,
        fontsize=WSIZE,
        update_interval=2,
    ),
    widget.GenPollText(
        background=COLORS["bg"],
        func=custom_widgets.check_updates,
        padding=5,
        fontsize=WSIZE,
        update_interval=60,
    ),
    widget.GenPollText(
        background=COLORS["bg"],
        func=custom_widgets.home_space,
        padding=5,
        fontsize=WSIZE,
        update_interval=30,
    ),
    widget.GenPollText(
        func=custom_widgets.hdd_space,
        fontsize=WSIZE,
        update_interval=60,
    ),
    widget.TextBox(
        fmt=f'<span size="x-large" foreground="{
            COLORS["bg1"]}">|</span>',
        fontsize=19,
    ),
    widget.Clock(
        fontsize=WSIZE,
        format=f'<span size="14000" rise="3000">%d</span><span size="x-large" foreground="{COLORS["bg1"]}">-</span><span size="14000" rise="3500">%H:%M</span><span size="x-large" foreground="{
            COLORS["bg1"]}">-</span><span size="12800" text_transform="uppercase" rise="3000">%a</span>',
    ),
]
