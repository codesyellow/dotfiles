import os, subprocess
from libqtile import widget, qtile
from .variables import colors, bg, fg, al, my_font, exit_icon_font, group_font, widget_icons, wsize
#from .functions import desconnect_ds4, run_easy, stop_easy

def tabbed():
    if qtile.current_group and qtile.current_group.tiled_windows:
        num_windows = len(qtile.current_group.tiled_windows)
        if num_windows <= 1:
            return ""
        else:
            return "  " + str(num_windows)
    return "" 

my_widgets = [
    widget.GroupBox(
        active=fg,
        background=bg,
        block_highlight_text_color=colors[1],
        disable_drag=True,
        highlight_method='text',
        highlight_color=al,
        foreground=fg,
        font=group_font,
        fontsize=20,
        inactive=colors[14],
        use_mouse_wheel=False,
    ),
#     widget.TaskList(
#         title_width_method='uniform',
#         icon_size=0,
#         parse_text=tabbed,
# #        text_minimized="",
# #        text_maximized="",
# #        text_floating="",
#     ),
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
        foreground=fg,
        format='%d %H:%M',
    ),
    widget.Clock(
        font='Font Awesome 6 Free Regular',
        fontsize=15,
        foreground=fg,
        format='%a',
    ),
    widget.Spacer(
        background=bg
    ),
    widget.Chord(
        background=bg,
        foreground=fg,
        fontsize=wsize,
        font='JetBrainMono Nerd Font',
    ),
    # widget.GenPollText(
    #     background=bg,
    #     func=lambda: subprocess.check_output(os.path.expanduser("~/.bin/psbat.sh")).decode("utf-8"),
    #     foreground=colors[21],
    #     font='JetBrainMono Nerd Font',
    #     mouse_callbacks={'Button1': desconnect_ds4 },
    #     fontsize=wsize,
    #     update_interval=30, 
    # ),
    widget.GenPollText(
        background=bg,
        func=lambda: subprocess.check_output(os.path.expanduser("~/.config/qtile/configs/widgets/easy.sh")).decode("utf-8"),
        font='JetBrainMono Nerd Font',
        padding=5,
        fontsize=wsize,
        update_interval=2, 
    ),
    widget.GenPollText(
        background=bg,
        func=lambda: subprocess.check_output(os.path.expanduser("~/.config/qtile/configs/widgets/gameon.sh")).decode("utf-8"),
        font='JetBrainMono Nerd Font',
        padding=5,
        fontsize=wsize,
        update_interval=2, 
    ),
    widget.GenPollText(
        background=bg,
        func=tabbed,
        font='JetBrainMono Nerd Font',
        foreground="#fff",
        padding=5,
        fontsize=wsize,
        update_interval=2, 
    ),
    widget.Volume(
        background=bg,
        font='JetBrainMono Nerd Font',
        fontsize=wsize,
        fmt='  {}',
        foreground=fg,
        update_interval=5
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
        foreground=fg,
        option='compose:menu,grp_led:scroll',
    ),
   widget.GenPollText(
        background=bg,
        func=lambda: subprocess.check_output(os.path.expanduser("~/.config/qtile/configs/widgets/disk-home.sh")).decode("utf-8"),
        font='JetBrainMono Nerd Font',
        padding=5,
        fontsize=wsize,
        update_interval=30, 
    ), 
    widget.GenPollText(
        background=bg,
        func=lambda: subprocess.check_output(os.path.expanduser("~/.config/qtile/configs/widgets/disk-hdd.sh")).decode("utf-8"),
        font='JetBrainMono Nerd Font',
        fontsize=wsize,
        update_interval=60, 
    ),
    widget.GenPollText(
        background=bg,
        func=lambda: subprocess.check_output(os.path.expanduser("~/.config/qtile/configs/widgets/disk-root.sh")).decode("utf-8"),
        font='JetBrainMono Nerd Font',
        fontsize=wsize,
        update_interval=15, 
    ),
    widget.GenPollText(
        background=bg,
        func=lambda: subprocess.check_output(os.path.expanduser("~/.config/qtile/configs/widgets/pymor.sh")).decode("utf-8"),
        font='JetBrainMono Nerd Font',
        fontsize=wsize,
        update_interval=5, 
    ),
    widget.GenPollText(
        background=bg,
        func=lambda: subprocess.check_output(os.path.expanduser("~/.config/qtile/configs/widgets/temp.sh")).decode("utf-8"),
        font='JetBrainMono Nerd Font',
        fontsize=wsize,
        update_interval=5, 
    ),
    widget.GenPollText(
        background=bg,
        func=lambda: subprocess.check_output(os.path.expanduser("~/.config/qtile/configs/widgets/cpu.sh")).decode("utf-8"),
        font='JetBrainMono Nerd Font',
        fontsize=wsize,
        update_interval=2, 
    ),
    widget.GenPollText(
        background=bg,
        func=lambda: subprocess.check_output(os.path.expanduser("~/.config/qtile/configs/widgets/mem.sh")).decode("utf-8"),
        font='JetBrainMono Nerd Font',
        fontsize=wsize,
        update_interval=15, 
    ),
    
        # widget.Memory(
    #     background=bg,
    #     font='JetBrainMono Nerd Font',
    #     fontsize=wsize,
    #     foreground=fg,
    #     format=f'{widget_icons[4]}' + '{MemUsed:.0f}{mm}',
    #     update_interval=60
    # ),
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
    foreground=fg,
    padding=4,
)

extension_defaults = widget_defaults.copy()


