import os, subprocess
from libqtile import widget, qtile
from .variables import bg, fg, al, my_font, exit_icon_font, group_font, widget_icons, wsize
from .functions import tabbed

my_widgets = [
    widget.GroupBox(
        active=fg,
        block_highlight_text_color=al,
        disable_drag=True,
        highlight_method='text',
        markup=True,
        highlight_color=al,
        font=group_font,
        fontsize=20,
        inactive=fg,
        use_mouse_wheel=False,
    ),
    widget.CurrentLayoutIcon(),
    widget.Spacer(),
    widget.Clock(
        fontsize=wsize,
        format='%d | %H:%M | %a',
    ),
    widget.Spacer(),
    widget.Chord(
        foreground=al,
        fontsize=wsize,
    ),
    widget.GenPollText(
        func=lambda: subprocess.check_output(os.path.expanduser("~/.config/qtile/configs/widgets/easy.sh")).decode("utf-8"),
        padding=5,
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
        fmt='| ',
        fontsize=16,
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
        padding=5,
        fontsize=wsize,
        update_interval=2,
    ),
    widget.Volume(
        fontsize=wsize,
        fmt='  {}',
        update_interval=5
    ),
    #widget.KeyboardLayout(
    #    configured_keyboards=['us', 'us intl'],
    #    display_map={
    #        'us':f'{widget_icons[0]}US',
    #        'us intl':f'{widget_icons[0]}USI',
    #    },
    #    fontsize=wsize,
    #    option='compose:menu,grp_led:scroll',
    #),
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
    widget.GenPollText(
        func=lambda: subprocess.check_output(os.path.expanduser("~/.config/qtile/configs/widgets/disk-root.sh")).decode("utf-8"),
        fontsize=wsize,
        update_interval=15,
    ),
    widget.GenPollText(
        func=lambda: subprocess.check_output(os.path.expanduser("~/.config/qtile/configs/widgets/pymor.sh")).decode("utf-8"),
        fontsize=wsize,
        update_interval=5,
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
    widget.QuickExit(default_text=f'{widget_icons[2]}', countdown_format=f'{widget_icons[3]}'),
    widget.Spacer(length=6),
]

widget_defaults = dict(
    background=bg,
    font='JetBrainMono Nerd Font',
    foreground=fg,
    padding=4,
)

extension_defaults = widget_defaults.copy()
