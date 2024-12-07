import os, subprocess
from libqtile import widget, qtile
from .variables import group_font, widget_icons, wsize, colors
from .functions import tabbed
from libqtile.log_utils import logger

my_widgets = [
    widget.Volume(
        fontsize=18,
        fmt='<span size="24000" rise="4500" foreground="#d8dee9"></span> <span rise="9000" size="13500" foreground="#d8dee9">{}</span>',
        update_interval=5,
    ),
    widget.GenPollText(
        func=lambda: subprocess.check_output(
            os.path.expanduser("~/.config/qtile/configs/widgets/mem.sh")
        ).decode("utf-8"),
        fontsize=wsize,
        font=group_font,
        update_interval=15,
    ),
    widget.GenPollText(
        func=lambda: subprocess.check_output(
            os.path.expanduser("~/.config/qtile/configs/widgets/cpu.sh")
        ).decode("utf-8"),
        fontsize=wsize,
        font=group_font,
        update_interval=2,
    ),
    widget.GenPollText(
        func=lambda: subprocess.check_output(
            os.path.expanduser("~/.config/qtile/configs/widgets/disk-root.sh")
        ).decode("utf-8"),
        fontsize=wsize,
        font=group_font,
        update_interval=15,
    ),
    widget.GenPollText(
        func=lambda: subprocess.check_output(
            os.path.expanduser("~/.config/qtile/configs/widgets/pymor.sh")
        ).decode("utf-8"),
        fontsize=wsize,
        font=group_font,
        update_interval=5,
    ),
    widget.GenPollText(
        func=lambda: subprocess.check_output(
            os.path.expanduser("~/.config/qtile/configs/widgets/stretch.sh")
        ).decode("utf-8"),
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
        func=lambda: subprocess.check_output(
            os.path.expanduser("~/.config/qtile/configs/widgets/easy.sh")
        ).decode("utf-8"),
        fontsize=wsize,
        update_interval=2,
    ),
    widget.TextBox(
        fmt=f'<span size="x-large" foreground="{colors["bg1_color"]}">|</span>',
        fontsize=19,
    ),
    widget.GenPollText(
        func=lambda: subprocess.check_output(
            os.path.expanduser("~/.config/qtile/configs/widgets/gameon.sh")
        ).decode("utf-8"),
        font=group_font,
        padding=5,
        fontsize=wsize,
        update_interval=2,
    ),
    widget.GenPollText(
        func=tabbed,
        foreground=colors["alt_color"],
        padding=5,
        fontsize=wsize,
        font=group_font,
        update_interval=2,
    ),
    widget.GenPollText(
        background=colors["bg_color"],
        func=lambda: subprocess.check_output(
            os.path.expanduser("~/.config/qtile/configs/widgets/variant.sh")
        ).decode("utf-8"),
        fontsize=wsize,
        update_interval=2,
    ),
    widget.GenPollText(
        background=colors["bg_color"],
        func=lambda: subprocess.check_output(
            os.path.expanduser("~/.config/qtile/configs/widgets/updates.sh")
        ).decode("utf-8"),
        padding=5,
        fontsize=wsize,
        update_interval=60,
    ),
    widget.GenPollText(
        func=lambda: subprocess.check_output(
            os.path.expanduser("~/.config/qtile/configs/widgets/santos.sh")
        ).decode("utf-8"),
        fontsize=wsize,
        mouse_callbacks={
            "Button1": lambda: qtile.spawn("touch /tmp/stop_santos_widget")
        },
        update_interval=30,
    ),
    widget.GenPollText(
        func=lambda: subprocess.check_output(
            os.path.expanduser("~/.config/qtile/configs/widgets/tmux_kill.mjs")
        ).decode("utf-8"),
        fontsize=wsize,
        mouse_callbacks={"Button1": lambda: qtile.spawn("tmux_kill.mjs 'kill'")},
        update_interval=30,
    ),
    widget.Clock(
        fontsize=wsize,
        format=f'<span size="14000" rise="3000">%d</span><span size="x-large" foreground="{colors["bg1_color"]}">|</span><span size="14000" rise="3500">%H:%M</span><span size="x-large" foreground="{colors["bg1_color"]}">|</span><span size="12800" text_transform="uppercase" rise="3000">%a</span>',
    ),
    widget.GenPollText(
        func=lambda: subprocess.check_output(
            os.path.expanduser("~/.config/qtile/configs/widgets/temp.sh")
        ).decode("utf-8"),
        fontsize=wsize,
        update_interval=5,
    ),
    widget.GenPollText(
        background=colors["bg_color"],
        func=lambda: subprocess.check_output(
            os.path.expanduser("~/.config/qtile/configs/widgets/disk-home.sh")
        ).decode("utf-8"),
        padding=5,
        fontsize=wsize,
        update_interval=30,
    ),
    widget.GenPollText(
        func=lambda: subprocess.check_output(
            os.path.expanduser("~/.config/qtile/configs/widgets/disk-hdd.sh")
        ).decode("utf-8"),
        fontsize=wsize,
        update_interval=60,
    ),
]

widget_defaults = dict(
    background=colors["bg_color"],
    font="JetBrainMono Nerd Font",
    foreground=colors["fg_color"],
    padding=4,
)

extension_defaults = widget_defaults.copy()
