from libqtile import widget
import subprocess
from .variables import colors, my_font, exit_icon_font, home
def get_cur_grp_name():
    result = subprocess.run(["/home/cie/.bin/easy_preset.sh"], capture_output=True, shell=True, text=True)
    output = result.stdout
    return output

my_widgets = [
        widget.GroupBox(
            background=colors[1],
            active=colors[20],
            block_highlight_text_color=colors[22],
            highlight_method='line',
            inactive=colors[6],
            ),
        widget.CurrentLayoutIcon(),
        widget.Spacer(),
        widget.Clock(
            font=my_font,
            format=' %d|%b  %H:%M  %a',
            ),
        widget.Spacer(length=4),
        widget.GenPollText(
            func=get_cur_grp_name,
            update_interval=1,
            foreground=colors[12],
            padding=1, 
            ),
        widget.Spacer(length=4),
        widget.KeyboardLayout(
            configured_keyboards=['br nodeadkeys', 'br'],
            display_map={
                'br nodeadkeys':' BRNDK',
                'br':' BR',
                },
            foreground=colors[17],
            option='compose:menu,grp_led:scroll',
            ),
        widget.Spacer(length=4),
        widget.Net(
            foreground=colors[18],
            format=' {down}',
            ),
        widget.Spacer(length=4),
        widget.DF(
            font=my_font,
            foreground=colors[16],
            partition='/',
            format=' {uf}{m}',
            visible_on_warn=False,
            ),
        widget.Spacer(length=2),
        widget.DF(
            font=my_font,
            foreground=colors[19],
            partition='/home',
            format=' {uf}{m}',
            visible_on_warn=False,
            ),
        widget.Spacer(length=4),
        widget.CPU(
            font=my_font,
            foreground=colors[13],
            format='  {freq_current}GHz|{load_percent}%',
            ),
        widget.Spacer(length=-4),
        widget.Memory(
            font=my_font,
            foreground=colors[14],
            format=' 󰍛{MemUsed: .0f}{mm}',
            ),
        widget.Spacer(length=4),
        widget.Systray(),
        widget.Spacer(length=4),
        widget.QuickExit(
            default_text='', countdown_format='',
            font=exit_icon_font,
            ),
        widget.Spacer(length=6),
        ]
widget_defaults = dict(
    background=colors[1],
    font=my_font,
    fontsize=14,
    padding=4,
)

extension_defaults = widget_defaults.copy()
