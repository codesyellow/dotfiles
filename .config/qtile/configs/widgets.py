from libqtile import widget
from .variables import FONT, widget_icons, WSIZE, COLORS
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
        active=COLORS["fg_color"],
        block_highlight_text_color=COLORS["alt_color"],
        disable_drag=True,
        markup=True,
        spacing=2,
        highlight_method="text",
        this_current_screen_border=COLORS["alt_color"],
        urgent_text=COLORS["alt_color"],
        highlight_color=[COLORS["bg_color"], COLORS["alt_color"]],
        font=FONT,
        fontsize=WSIZE,
        inactive=COLORS["bg1_color"],
        foreground="#444",
        use_mouse_wheel=False,
    ),
    widget.Spacer(),
    widget.Chord(
        foreground=COLORS["alt_color"],
        fontsize=WSIZE,
        font=FONT,
    ),
    widget.QuickExit(
        default_text=f"{widget_icons[0]}",
        countdown_format=f"{widget_icons[1]}",
        countdown_start=10,
    ),
    widget.GenPollText(
        func=custom_widgets.easyeffects_is_on,
        fontsize=WSIZE,
        update_interval=2,
    ),
    widget.GenPollText(
        background=COLORS["bg_color"],
        func=custom_widgets.check_keyboard_variant,
        fontsize=WSIZE,
        update_interval=2,
    ),
    widget.GenPollText(
        background=COLORS["bg_color"],
        func=custom_widgets.check_updates,
        padding=5,
        fontsize=WSIZE,
        update_interval=60,
    ),
    widget.GenPollText(
        background=COLORS["bg_color"],
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
            COLORS["bg1_color"]}">|</span>',
        fontsize=19,
    ),
    widget.Clock(
        fontsize=WSIZE,
        format=f'<span size="14000" rise="3000">%d</span><span size="x-large" foreground="{COLORS["bg1_color"]}">-</span><span size="14000" rise="3500">%H:%M</span><span size="x-large" foreground="{
            COLORS["bg1_color"]}">-</span><span size="12800" text_transform="uppercase" rise="3000">%a</span>',
    ),
]

widget_defaults = dict(
    background=COLORS["bg_color"],
    font=FONT,
    foreground=COLORS["fg_color"],
    padding=4,
)

extension_defaults = widget_defaults.copy()
