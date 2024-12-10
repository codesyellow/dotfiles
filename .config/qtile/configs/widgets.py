import os
import subprocess
from libqtile import widget, qtile
from .variables import group_font, widget_icons, wsize, colors
from .custom_widgets import cpu_temp, cpu_usage, game_is_on, mem_usage, root_space, home_space, hdd_space, pomodoro, easyeffects_is_on, check_updates, check_keyboard_variant, do_stretch

my_widgets = [
    widget.Volume(
        fontsize=18,
        fmt='<span size="24000" rise="4500" foreground="#d8dee9"></span> <span rise="9000" size="13500" foreground="#d8dee9">{}</span>',
        update_interval=5,
    ),
    widget.GenPollText(
        func=mem_usage,
        fontsize=wsize,
        font=group_font,
        update_interval=15,
    ),
    widget.GenPollText(
        func=cpu_usage,
        fontsize=wsize,
        font=group_font,
        update_interval=1,
    ),
    widget.GenPollText(
        func=cpu_temp,
        font=group_font,
        padding=5,
        fontsize=wsize,
        update_interval=5,
    ),
    widget.GenPollText(
        func=root_space,
        fontsize=wsize,
        font=group_font,
        update_interval=15,
    ),
    widget.GenPollText(
        func=pomodoro,
        fontsize=wsize,
        font=group_font,
        update_interval=5,
    ),
    widget.GenPollText(
        func=game_is_on,
        fontsize=wsize,
        font=group_font,
        update_interval=2,
    ),
    widget.GenPollText(
        func=do_stretch,
        fontsize=wsize,
        update_interval=1,
    ),
    widget.Spacer(),
    widget.GroupBox(
        active=colors["fg_color"],
        block_highlight_text_color=colors["alt_color"],
        disable_drag=True,
        markup=True,
        spacing=2,
        highlight_method="text",
        this_current_screen_border=colors["alt_color"],
        urgent_text=colors["alt_color"],
        highlight_color=[colors["bg_color"], colors["alt_color"]],
        font=group_font,
        fontsize=wsize,
        inactive=colors["bg1_color"],
        foreground="#444",
        use_mouse_wheel=False,
    ),
    widget.Spacer(),
    widget.Chord(
        foreground=colors["alt_color"],
        fontsize=wsize,
        font=group_font,
    ),
    widget.QuickExit(
        default_text=f"{widget_icons[2]}",
        countdown_format=f"{widget_icons[3]}",
        countdown_start=10,
    ),
    widget.GenPollText(
        func=easyeffects_is_on,
        fontsize=wsize,
        update_interval=2,
    ),
    widget.GenPollText(
        background=colors["bg_color"],
        func=check_keyboard_variant,
        fontsize=wsize,
        update_interval=2,
    ),
    widget.GenPollText(
        background=colors["bg_color"],
        func=check_updates,
        padding=5,
        fontsize=wsize,
        update_interval=60,
    ),
    # widget.GenPollText(
    #    func=lambda: subprocess.check_output(
    #        os.path.expanduser("~/.config/qtile/configs/widgets/santos.sh")
    #    ).decode("utf-8"),
    #    fontsize=wsize,
    #    mouse_callbacks={
    #        "Button1": lambda: qtile.spawn("touch /tmp/stop_santos_widget")
    #    },
    #    update_interval=30,
    # ),
    widget.GenPollText(
        background=colors["bg_color"],
        func=home_space,
        padding=5,
        fontsize=wsize,
        update_interval=30,
    ),
    widget.GenPollText(
        func=hdd_space,
        fontsize=wsize,
        update_interval=60,
    ),
    widget.TextBox(
        fmt=f'<span size="x-large" foreground="{
            colors["bg1_color"]}">|</span>',
        fontsize=19,
    ),
    widget.Clock(
        fontsize=wsize,
        format=f'<span size="14000" rise="3000">%d</span><span size="x-large" foreground="{colors["bg1_color"]}">-</span><span size="14000" rise="3500">%H:%M</span><span size="x-large" foreground="{
            colors["bg1_color"]}">-</span><span size="12800" text_transform="uppercase" rise="3000">%a</span>',
    ),
]

widget_defaults = dict(
    background=colors["bg_color"],
    font="JetBrainMono Nerd Font",
    foreground=colors["fg_color"],
    padding=4,
)

extension_defaults = widget_defaults.copy()
