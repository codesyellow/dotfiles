import os, subprocess
from libqtile import widget
from .variables import colors, bg, my_font, exit_icon_font, group_font, widget_icons
from .functions import desconnect_ds4

my_widgets = [
        widget.GroupBox(
            active=colors[15],
            background=bg,
            block_highlight_text_color=colors[1],
            disable_drag=True,
            highlight_method='text',
            highlight_color=[colors[15]],
            foreground=colors[18],
            font=group_font,
            fontsize=16,
            inactive=colors[14],
            use_mouse_wheel=False,
            ),
        widget.CurrentLayoutIcon(),
        widget.Spacer(
            background=bg
            ),
        widget.Clock(
            font=my_font,
            background=bg,
            foreground=colors[18],
            format='%d|%H:%M|%a',
            ),
        widget.Spacer(
            background=bg
            ),
        widget.Chord(
            background=bg,
            foreground=colors[20],
            ),
        widget.GenPollText(
            background=bg,
            foreground=colors[21],
            func=lambda: subprocess.check_output(os.path.expanduser("~/.bin/psbat.sh")).decode("utf-8"),
            mouse_callbacks={'Button1': desconnect_ds4 },
            update_interval=30, 
            ),
        widget.KeyboardLayout(
            background=bg,
            configured_keyboards=['us', 'us intl'],
            display_map={
                'us':f'{widget_icons[0]} US',
                'us intl':'  USI',
                },
            foreground=colors[18],
            option='compose:menu,grp_led:scroll',
            ),
        widget.DF(
            background=bg,
            font=my_font,
            foreground=colors[16],
            format=f'{widget_icons[1]}' + ' {uf}{m}',
            partition='/',
            visible_on_warn=False,
            ),
        widget.DF(
            background=bg,
            font=my_font,
            foreground=colors[19],
            partition='/home',
            format=f'{widget_icons[2]}' + '  {uf}{m}',
            visible_on_warn=False,
            ),
        widget.CPU(
            background=bg,
                font=my_font,
                foreground=colors[13],
                format=f'{widget_icons[3]}' + '  {freq_current}GHz|{load_percent}%',
                ),
        widget.Memory(
            background=bg,
                font=my_font,
                foreground=colors[14],
                format=f'{widget_icons[4]}' + '{MemUsed: .0f}{mm}',
                ),
        widget.Spacer(length=2),
        widget.StatusNotifier(),
        widget.Spacer(length=2),
        widget.QuickExit(
            background=bg,
                default_text=f'{widget_icons[5]}', countdown_format=f'{widget_icons[6]}',
                font=exit_icon_font,
                ),
        widget.Spacer(length=6),
        ]

widget_defaults = dict(
        background="#00000069",
        font=my_font,
        fontsize=14,
        padding=4,
        )

extension_defaults = widget_defaults.copy()


