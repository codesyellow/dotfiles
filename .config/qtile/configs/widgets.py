from libqtile import widget
from libqtile.lazy import lazy
from .variables import FONT, WSIZE, COLORS, GROUP_ICONS, VERTICAL_MONITOR_GROUPS
from .custom_widgets import Custom_Widgets
from .functions import stop_timers, start_pomodoro, tabbed

custom_widgets = Custom_Widgets()

vertical_widgets = [
    widget.GroupBox(
        visible_groups=VERTICAL_MONITOR_GROUPS,
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
    widget.GenPollText(
        func=lambda: custom_widgets.ds4_bat(
            texty=6000,
            icony=5700,
            icon_size=17000,
            bar_pos="right"),
        fontsize=WSIZE,
        font=FONT,
        mouse_callbacks={
            "Button1": start_pomodoro,
            "Button3": lambda: stop_timers(file="pomo_cancel"),
        },
        update_interval=1,
    ),
    widget.GenPollText(
        func=lambda: custom_widgets.mem_usage(
            texty=5000,
            icony=5000,
            icon_size=13000,
        ),
        fontsize=WSIZE,
        font=FONT,
        update_interval=15,
    ),
    widget.GenPollText(
        func=lambda: custom_widgets.cpu_usage(
            texty=5000,
            icony=6500,
            icon_size=13000,
        ),
        fontsize=WSIZE,
        font=FONT,
        update_interval=1,
    ),
    widget.GenPollText(
        func=lambda: custom_widgets.cpu_temp(
            texty=5000,
            icony=6000,
            icon_size=13000,
        ),
        font=FONT,
        padding=5,
        fontsize=WSIZE,
        update_interval=5,
    ),
    widget.GenPollText(
        func=lambda: custom_widgets.root_space(
            texty=6000,
            icony=7500,
            icon_size=13000
        ),
        fontsize=WSIZE,
        font=FONT,
        update_interval=15,
    ),
    widget.GenPollText(
        func=lambda: custom_widgets.countdown(
            texty=5500,
            icony=7000,
            icon_size=13000,
        ),
        fontsize=WSIZE,
        font=FONT,
        mouse_callbacks={
            "Button3": lambda: stop_timers(file="countdown_cancel"),
        },
        update_interval=1,
    ),
    widget.GenPollText(
        func=lambda: custom_widgets.game_is_on(
            icony=6000
        ),
        fontsize=WSIZE,
        font=FONT,
        update_interval=2,
    ),
    widget.GenPollText(
        func=custom_widgets.do_stretch,
        fontsize=WSIZE,
        update_interval=1,
    ),
    widget.GenPollText(
        func=lambda: custom_widgets.pomodoro(
            bar_pos="right",
            texty=6000,
            icony=7000,
        ),
        fontsize=WSIZE,
        font=FONT,
        mouse_callbacks={
            "Button1": start_pomodoro,
            "Button3": lambda: stop_timers(file="pomo_cancel"),
        },
        update_interval=1,
    ),
    widget.Volume(
        fontsize=18,
        fmt='<span size="24000" rise="4500" foreground="#d8dee9"></span> <span rise="9000" size="13500" foreground="#d8dee9">{}</span>',
        update_interval=5,
    ),
    widget.TextBox(
        fmt=f'<span size="x-large" foreground="{
            COLORS["bg1"]}">|</span>',
        fontsize=19,
    ),
    widget.Clock(
        fontsize=WSIZE,
        format=f'<span size="20000" rise="2000">󱑸</span> <span size="14000" rise="4500">%H:%M</span>',
    ),
]

my_widgets = [
    widget.GroupBox(
        visible_groups=GROUP_ICONS,
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
    widget.TextBox(
        fmt=f'<span size="x-large" foreground="{
            COLORS["bg1"]}">|</span>',
        fontsize=19,
    ),
    widget.GenPollText(
        func=lambda: custom_widgets.easyeffects_is_on(
            icony=5000,
            icon_size=13500,
        ),
        fontsize=WSIZE,
        update_interval=2,
    ),
    widget.GenPollText(
        background=COLORS["bg"],
        func=lambda: custom_widgets.check_keyboard_variant(
            icon_size=25000,
            texty=8000,
            icony=3000,
            bar_pos="right"),
        fontsize=WSIZE,
        update_interval=2,
    ),
    widget.GenPollText(
        background=COLORS["bg"],
        func=lambda: custom_widgets.check_updates(
            texty=7000,
            icony=7000,
            icon_size=14000,
            bar_pos="right",
        ),
        padding=5,
        fontsize=WSIZE,
        update_interval=60,
    ),
    widget.GenPollText(
        background=COLORS["bg"],
        func=lambda: custom_widgets.home_space(
            texty=7000,
            icon_size=12000,
            icony=8000,
        ),
        padding=5,
        fontsize=WSIZE,
        update_interval=30,
    ),
    widget.GenPollText(
        func=lambda: custom_widgets.hdd_space(
            texty=7000,
            icon_size=21000,
            icony=4000,
        ),
        fontsize=WSIZE,
        update_interval=60,
    ),
    widget.GenPollText(
        background=COLORS["bg"],
        func=custom_widgets.santos_widget,
        fontsize=WSIZE,
        update_interval=2,
        width=200,
        scroll_step=2,
        scroll=True,
    ),
    widget.GenPollText(
        func=tabbed,
        fontsize=WSIZE,
        update_interval=2,
        mouse_callbacks={
            "Button3": lazy.group.next_window(),
            "Button1": lazy.group.prev_window()
        },
    ),
    widget.Clock(
        fontsize=WSIZE,
        format=f'<span size="20000" rise="2000">󱑸</span> <span size="14000" rise="4300">%d</span><span size="x-large" foreground="{COLORS["bg1"]}">-</span><span size="14000" rise="4300">%H:%M</span><span size="x-large" foreground="{
            COLORS["bg1"]}">-</span><span size="12800" text_transform="uppercase" rise="4500">%a</span>',
    ),
]
