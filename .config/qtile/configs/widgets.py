import os, subprocess
from libqtile import widget
from .variables import colors, bg, my_font, exit_icon_font, group_font, widget_icons, wsize
from .functions import desconnect_ds4, run_easy, stop_easy
script_path = os.path.expanduser("~/.bin/easyon.sh")
arguments = ["easyeffects"]
output = subprocess.check_output([script_path] + arguments).decode("utf-8")

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
        fontsize=20,
        inactive=colors[14],
        use_mouse_wheel=False,
    ),
    widget.CurrentLayoutIcon(
        background=bg
    ),
    widget.Spacer(
        background=bg
    ),
    widget.Clock(
        font='JetBrainMono Nerd Font',
        fontsize=wsize,
        background=bg,
        foreground='#fff',
        format='%d %H:%M',
    ),
    widget.Clock(
        font='Font Awesome 6 Free Regular',
        fontsize=15,
        foreground='#E49BFF',
        format='%a',
    ),
    widget.Spacer(
        background=bg
    ),
    widget.Chord(
        background=bg,
        foreground=colors[20],
        fontsize=wsize,
        font='JetBrainMono Nerd Font',
    ),
    widget.GenPollText(
        background=bg,
        func=lambda: subprocess.check_output(os.path.expanduser("~/.bin/psbat.sh")).decode("utf-8"),
        foreground=colors[21],
        font='JetBrainMono Nerd Font',
        mouse_callbacks={'Button1': desconnect_ds4 },
        fontsize=wsize,
        update_interval=30, 
    ),
    widget.GenPollText(
        background=bg,
        font='JetBrainMono Nerd Font',
        fontsize=wsize,
        func=lambda: subprocess.check_output(os.path.expanduser("~/.bin/easyon.sh")).decode("utf-8"),
        foreground=colors[22],
        mouse_callbacks={
            'Button1': run_easy,
            'Button2': stop_easy,
        },
        update_interval=60, 
    ),
    widget.Volume(
        background=bg,
        font='JetBrainMono Nerd Font',
        fontsize=wsize,
        fmt='  {}',
        foreground=colors[15],
    ),
    widget.KeyboardLayout(
        background=bg,
        configured_keyboards=['us', 'us intl'],
        display_map={
            'us':f'{widget_icons[0]}US',
            'us intl':f'{widget_icons[0]}USI',
        },
        font='JetBrainMono Nerd Font',
        fontsize=wsize,
        foreground=colors[18],
        option='compose:menu,grp_led:scroll',
    ),
    widget.DF(
        background=bg,
        font='JetBrainMono Nerd Font',
        fontsize=wsize,
        foreground=colors[16],
        format=f'{widget_icons[1]}'+ '{uf}{m}',
        partition='/',
        visible_on_warn=False,
    ),
    widget.ThermalSensor(
        font='JetBrainMono Nerd Font',
        fontsize=wsize,
        format=f'{widget_icons[2]}' + '{temp:.0f}{unit}',
        tag_sensor="Core 1",
    ),
    widget.CPU(
        background=bg,
        font='JetBrainMono Nerd Font',
        fontsize=wsize,
        foreground=colors[13],
        format=f'{widget_icons[3]}' + ' {load_percent}%',
    ),
    widget.Memory(
        background=bg,
        font='JetBrainMono Nerd Font',
        fontsize=wsize,
        foreground=colors[14],
        format=f'{widget_icons[4]}' + '{MemUsed:.0f}{mm}',
    ),
    widget.Systray(),
    widget.QuickExit(
        background=bg,
        default_text=f'{widget_icons[5]}', countdown_format=f'{widget_icons[6]}',
        font='JetBrainMono Nerd Font',
    ),
    widget.Spacer(length=6),
]

widget_defaults = dict(
    background="#000000",
    font='InconsolataGo Nerd Font',
    padding=4,
)

extension_defaults = widget_defaults.copy()


