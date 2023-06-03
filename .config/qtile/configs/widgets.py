#from libqtile import widget
from qtile_extras import widget
from .variables import colors, my_font, exit_icon_font

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
            format='%d|%b %H:%M %a',
            ),
        widget.Spacer(length=4),
        widget.CheckUpdates(
            distro='Arch',
            foreground=colors[13],
            no_update_string='No updates',
            ),
        widget.Spacer(length=4),
        widget.KeyboardLayout(
            configured_keyboards=['br nodeadkeys', 'br'],
            display_map={
                'br nodeadkeys':'BRNDK',
                },
            foreground=colors[17],
            option='compose:menu,grp_led:scroll',
            ),
        widget.Spacer(length=4),
        widget.Net(
            foreground=colors[18],
            format=' {down} |  {up}',
            ),
        widget.Spacer(length=4),
        widget.ALSAWidget(
            bar_colour_high=colors[13],
            bar_colour_loud=colors[12],
            bar_colour_mute=colors[0],
            bar_colour_normal=colors[16],
            font=my_font,
            foreground=colors[15],
            mode='bar',
            update_interval=2,
            ),
        widget.PulseVolume(
            font=my_font,
            foreground=colors[15]
            ),
        widget.Spacer(length=4),
        widget.DF(
            font=my_font,
            foreground=colors[16],
            partition='/',
            visible_on_warn=False,
            ),
        widget.DF(
            font=my_font,
            foreground=colors[16],
            partition='/home',
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
