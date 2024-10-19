import os, subprocess
from libqtile import widget, qtile
from .variables import bg, fg, al, my_font, exit_icon_font, group_font, widget_icons, wsize

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
        block_highlight_text_color=al,
        disable_drag=True,
        highlight_method='text',
        markup=True,
        highlight_color=al,
        foreground=fg,
        font=group_font,
        fontsize=20,
        inactive=fg,
        use_mouse_wheel=False,
    ),
    widget.CurrentLayoutIcon(
        background=bg,
    ),
    widget.Spacer(
        background=bg
    ),
    widget.Clock(
        font='JetBrainMono Nerd Font',
        fontsize=wsize,
        background=bg,
        foreground=fg,
        format='%d | %H:%M | %a',
    ),
    widget.Spacer(
        background=bg
    ),
    widget.Chord(
        background=bg,
        foreground=al,
        fontsize=wsize,
        font='JetBrainMono Nerd Font',
    ),
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
    
    widget.QuickExit(
        background=bg,
        default_text=f'{widget_icons[2]}', countdown_format=f'{widget_icons[3]}',
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


