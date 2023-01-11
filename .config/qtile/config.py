import os, subprocess
from libqtile import bar, layout, hook, widget
from libqtile.config import Click, Drag, Group, ScratchPad, DropDown, Key, Match, Screen, KeyChord
from libqtile.lazy import lazy
from libqtile.backend.wayland import InputConfig
from libqtile.log_utils import logger

#Colors for the bar
def init_colors():
    return [["#2e3440", "#2e3440"], # color 0  background color
            ["#2e3440", "#2e3440"], # color 1  dark grayish blue
            ["#3b4252", "#3b4252"], # color 2  very dark grayish blue
            ["#434c5e", "#434c5e"], # color 3  very dark grayish blue
            ["#4c566a", "#4c566a"], # color 4  very dark grayish blue
            ["#d8dee9", "#d8dee9"], # color 5  grayish blue
            ["#e5e9f0", "#e5e9f0"], # color 6  light grayish blue
            ["#eceff4", "#eceff4"], # color 7  light grayish blue
            ["#8fbcbb", "#8fbcbb"], # color 8  grayish cyan
            ["#88c0d0", "#88c0d0"], # color 9  desaturated cyan
            ["#81a1c1", "#81a1c1"], # color 10 desaturated blue
            ["#5e81ac", "#5e81ac"], # color 11 dark moderate blue
            ["#bf616a", "#bf616a"], # color 12 slightly desaturated red
            ["#d08770", "#d08770"], # color 13 desaturated red
            ["#ebcb8b", "#ebcb8b"], # color 14 soft orange
            ["#a3be8c", "#a3be8c"], # color 15 desaturated green
            ["#b48ead", "#b48ead"]] # color 16 grayish magenta

colors = init_colors()

bg ='2D353B'
fg ='4F585f'
act ='D3C6AA'
pad = 10
inac='475258'
mod = "mod4"
runner = 'kickoff'
terminal = 'alacritty'

@hook.subscribe.client_focus
def opacity(c):
    for x in c.qtile.current_group.windows:
#        logger.warning(x.get_wm_class()[0])
        if not x.has_focus: 
            x.cmd_opacity(0.5) 
        elif x.name == 'scratchpad':
            x.cmd_opacity(0.8)
        else: 
            x.cmd_opacity(1)
        if x.get_wm_class()[0] == 'firefox':
            x.cmd_opacity(1)

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

wl_input_rules = {
    "type:keyboard": InputConfig(kb_options="ctrl:nocaps,compose:ralt", kb_layout="br(nodeadkeys)"),
}

def my_layouts():
    return [ 
            layout.MonadWide(
                align=1,
                border_focus=act,
                border_normal=inac,
                new_client_position='before_current',
                ratio=.7,
                single_border_width=0,
                single_margin=0,
                ),
            layout.Max(),
    ]

def my_widgets():
    return [
            widget.GroupBox(
                active=act,
                inactive=inac,
                highlight_method='block',
                block_highlight_text_color=bg,
            ),
            widget.CurrentLayoutIcon(),
            # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
            # widget.StatusNotifier(),
            widget.Spacer(),
            widget.Clock(format='%d/%m/%y %H:%M'),
            widget.Spacer(),
            widget.DF(
                foreground=colors[14],
                visible_on_warn=False,
            ),
            widget.Spacer(length=2),
            widget.CPU(
                foreground=colors[12],
                format='{freq_current}GHz|{load_percent}%',
            ),
            widget.Spacer(length=-4),
            widget.Memory(
                foreground=colors[16],
                format='{MemUsed: .0f}{mm}',
            ),
            widget.Spacer(length=4),
            widget.QuickExit(
                default_text='🚪', countdown_format='{}'
            ),
            widget.Spacer(length=6),
    ]

my_rules = [
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
]

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod, "shift"], "h", lazy.layout.swap_left()),
    Key([mod, "shift"], "l", lazy.layout.swap_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "m", lazy.layout.shrink()),
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "o", lazy.layout.maximize()),
    Key([mod, "shift"], "space", lazy.layout.flip()),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "t", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "f", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    # apps
    Key([mod, 'shift'], "d", lazy.spawn('volume.sh down'), desc="Launch runner"),
    Key([mod, 'shift'], "a", lazy.spawn('volume.sh up'), desc="Launch runner"),
    Key([mod], "d", lazy.spawn(runner), desc="Launch runner"),
    Key([mod, 'shift'], "a", lazy.spawn('volume.sh up'), desc="Raise volume"),
    Key([mod, 'shift'], "d", lazy.spawn('volume.sh down'), desc="Lower volume"),
    Key([mod, 'shift'], "g", lazy.function(change_info_status), desc="Lower volume"),
    KeyChord([mod], "s", [
        Key([], "u", lazy.group['scratchpad'].dropdown_toggle('term'))
    ])
]

def latest_group(qtile):
    qtile.current_screen.set_group(qtile.current_screen.previous_group)

keys += [Key([mod], "Tab", lazy.function(latest_group))]

groups = [
    Group("", layout="max",        matches=[Match(wm_class=["navigator", "firefox", "vivaldi-stable", "chromium", "brave"])]),
    Group("", layout="monadwide",  matches=[Match(wm_class=["Emacs", "geany", "subl"])]),
    Group("", layout="monadwide",  matches=[Match(wm_class=["inkscape", "nomacs", "ristretto", "nitrogen"])]),
    Group("", layout="monadwide",  matches=[Match(wm_class=["qpdfview", "thunar", "nemo", "caja", "pcmanfm"])]),
    Group("", layout="max",        matches=[Match(wm_class=["telegramDesktop"])]),
    Group("", layout="max"),
    Group("", layout="max",        matches=[Match(wm_class=["spotify", "pragha", "clementine", "deadbeef", "audacious"]), Match(title=["VLC media player"])]),
    Group("", layout="max"),
    ScratchPad("scratchpad", [
        # define a drop down terminal.
        # it is placed in the upper third of screen by default.
        DropDown("term", "alacritty -t scratchpad"),

        # define another terminal exclusively for ``qtile shell` at different position
        ]),
    Group("a"),
]

for k, group in zip(["1", "2", "3", "4", "5", "6", "7", "8"], groups):
    keys.append(Key([mod], k, lazy.group[group.name].toscreen()))
    keys.append(Key([mod, 'shift'], k, lazy.window.togroup(group.name)))

layouts = my_layouts()

widget_defaults = dict(
    background=colors[0],
    font="CaskadiaCove Nerd Font",
    fontsize=15,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            my_widgets()
            ,
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
cursor_warp = True
floating_layout = layout.Floating(float_rules=my_rules)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.

# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
