import os, subprocess
from libqtile import widget, qtile
from .variables import bg, fg, al, my_font, exit_icon_font, group_font, widget_icons, wsize
from .functions import tabbed
from libqtile.log_utils import logger

my_widgets = [
    widget.GroupBox(
        active=fg,
        block_highlight_text_color=al,
        disable_drag=True,
        markup=True,
        spacing=4,
        highlight_method='text',
        this_current_screen_border=al,
        urgent_text=al,
        highlight_color=[bg,al],
        font=group_font,
        fontsize=wsize,
        inactive='#4c566a',
        foreground='#444',
        use_mouse_wheel=False,
        padding_x=4,
    ),
    widget.CurrentLayoutIcon(),
    widget.Spacer(),
    widget.Clock(
        fontsize=wsize,
        format=f'<span size="14000" rise="3000">%d</span> <span size="x-large" foreground="#d8dee9">|</span> <span size="14000" rise="3500">%H:%M</span> <span size="x-large" foreground="#d8dee9">|</span> <span size="12800" text_transform="uppercase" rise="3000">%a</span>',
    ),
    widget.Spacer(),
    widget.Chord(
        foreground=al,
        fontsize=wsize,
    ),
    widget.QuickExit(
        default_text=f'{widget_icons[2]}', countdown_format=f'{widget_icons[3]}',
        countdown_start=10,
    ),
    widget.GenPollText(
        func=lambda: subprocess.check_output(os.path.expanduser("~/.config/qtile/configs/widgets/easy.sh")).decode("utf-8"),
        fontsize=wsize,
        update_interval=2,
    ),
    widget.GenPollText(
        func=lambda: subprocess.check_output(os.path.expanduser("~/.config/qtile/configs/widgets/gameon.sh")).decode("utf-8"),
        padding=5,
        fontsize=wsize,
        update_interval=2,
    ),
    widget.TextBox(
        fmt='<span size="x-large" foreground="#d8dee9">|</span>',
        fontsize=19,
    ),
    widget.GenPollText(
        func=tabbed,
        foreground=al,
        padding=5,
        fontsize=wsize,
        update_interval=2,
    ),
    widget.GenPollText(
        background=bg,
        func=lambda: subprocess.check_output(os.path.expanduser("~/.config/qtile/configs/widgets/variant.sh")).decode("utf-8"),
        fontsize=wsize,
        update_interval=2,
    ),
    widget.GenPollText(
        background=bg,
        func=lambda: subprocess.check_output(os.path.expanduser("~/.config/qtile/configs/widgets/updates.sh")).decode("utf-8"),
        padding=5,
        fontsize=wsize,
        update_interval=60,
    ),
    widget.GenPollText(
        func=lambda: subprocess.check_output(os.path.expanduser("~/.config/qtile/configs/widgets/stretch.sh")).decode("utf-8"),
        fontsize=wsize,
        update_interval=1,
    ),
    widget.GenPollText(
        func=lambda: subprocess.check_output(os.path.expanduser("~/.config/qtile/configs/widgets/pymor.sh")).decode("utf-8"),
        fontsize=wsize,
        update_interval=5,
    ),
    widget.GenPollText(
        func=lambda: subprocess.check_output(os.path.expanduser("~/.config/qtile/configs/widgets/santos.sh")).decode("utf-8"),
        fontsize=wsize,
        update_interval=30,
    ),
    widget.Volume(
        fontsize=18,
        fmt='<span size="14000" rise="4000" foreground="#d8dee9"></span> <span rise="4500" size="13500" foreground="#d8dee9"> {}</span>',
        update_interval=5
    ),
    widget.GenPollText(
        func=lambda: subprocess.check_output(os.path.expanduser("~/.config/qtile/configs/widgets/temp.sh")).decode("utf-8"),
        fontsize=wsize,
        update_interval=5,
    ),
    widget.GenPollText(
        func=lambda: subprocess.check_output(os.path.expanduser("~/.config/qtile/configs/widgets/cpu.sh")).decode("utf-8"),
        fontsize=wsize,
        update_interval=2,
    ),
    widget.GenPollText(
        func=lambda: subprocess.check_output(os.path.expanduser("~/.config/qtile/configs/widgets/mem.sh")).decode("utf-8"),
        fontsize=wsize,
        update_interval=15,
    ),
    widget.GenPollText(
        func=lambda: subprocess.check_output(os.path.expanduser("~/.config/qtile/configs/widgets/disk-root.sh")).decode("utf-8"),
        fontsize=wsize,
        update_interval=15,
    ),
   widget.GenPollText(
        background=bg,
        func=lambda: subprocess.check_output(os.path.expanduser("~/.config/qtile/configs/widgets/disk-home.sh")).decode("utf-8"),
        padding=5,
        fontsize=wsize,
        update_interval=30,
    ),
    widget.GenPollText(
        func=lambda: subprocess.check_output(os.path.expanduser("~/.config/qtile/configs/widgets/disk-hdd.sh")).decode("utf-8"),
        fontsize=wsize,
        update_interval=60,
    ),
    widget.Spacer(length=6),
]

widget_defaults = dict(
    background=bg,
    font='JetBrainMono Nerd Font',
    foreground=fg,
    padding=4,
)

extension_defaults = widget_defaults.copy()
