import os, subprocess
from libqtile import bar, layout, hook, widget
from libqtile.config import Click, Drag, Group, ScratchPad, DropDown, Key, Match, Screen, KeyChord
from libqtile.lazy import lazy
from libqtile.backend.wayland import InputConfig
from libqtile.log_utils import logger

mod = "mod4"
pad = 10
runner = 'kickoff'
terminal = 'alacritty'

@lazy.function
def set_layout(qtile):
    group_layout = qtile.current_layout.info()['name']
    logger.warning(dir(qtile.current_group.cmd_setlayout))
    logger.warning(qtile.current_group.cmd_setlayout('treetab'))
    # if layout == max go back to prev
    if group_layout == 'max':
        return qtile.cmd_prev_layout()
    qtile.cmd_to_layout_index(1)

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

def my_layouts():
    return [
            layout.MonadWide(
                align=1,
                border_focus=colors[4],
                border_normal=colors[7],
                border_width=0,
                new_client_position='before_current',
                ratio=.7,
                single_border_width=0,
                single_margin=0,
                ),
            layout.Max(),
            layout.TreeTab(
                bg_color=colors[0],
                border_width=0,
                place_right=True,
                section_fg=colors[0],
                active_bg=colors[5],
                active_fg=colors[0],
            ),
    ]

def my_widgets():
    return [
            widget.GroupBox(
                active=colors[11],
                block_highlight_text_color=colors[5],
                highlight_method='block',
                inactive=colors[4],
            ),
            widget.CurrentLayoutIcon(),
            # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
            # widget.StatusNotifier(),
            widget.Spacer(),
            widget.Clock(
                font="CaskaydiaCove Nerd Font Mono",
                format='%d/%m/%y %H:%M',
            ),
            widget.Spacer(),
            widget.DF(
                font="CaskaydiaCove Nerd Font Mono",
                foreground=colors[14],
                visible_on_warn=False,
            ),
            widget.Spacer(length=4),
            widget.CPU(
                font="CaskaydiaCove Nerd Font Mono",
                foreground=colors[12],
                format='{freq_current}GHz|{load_percent}%',
            ),
            widget.Spacer(length=-4),
            widget.Memory(
                font="CaskaydiaCove Nerd Font Mono",
                foreground=colors[16],
                format='{MemUsed: .0f}{mm}',
            ),
            widget.Spacer(length=4),
            widget.QuickExit(
                default_text='🚪', countdown_format='{}'
            ),
            widget.Spacer(length=6),
    ]

@hook.subscribe.client_focus
def opacity(c):
    for x in c.qtile.current_group.windows:
        if not x.has_focus:
            x.cmd_opacity(0.5) 
#        elif x.name == 'scratchpad':
#            x.cmd_opacity(0.8)
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

my_rules = [
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="com.github.wwmm.easyeffects"),  # ssh-askpass
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
    Key([mod, 'shift'], "f", set_layout, desc="Launch runner"),
    Key([mod, 'shift'], "m", lazy.spawn('alacritty -t fm-video -e lf /home/cse/.courses'), desc="Launch runner"),
    Key([mod, 'shift'], "e", lazy.spawn('alacritty -t fm-pdf -e lf /home/cse/.ebooks'), desc="Launch runner"),
    Key([mod], "d", lazy.spawn(runner), desc="Launch runner"),
    Key([mod, 'shift'], "a", lazy.spawn('volume.sh up'), desc="Raise volume"),
    Key([mod, 'shift'], "d", lazy.spawn('volume.sh down'), desc="Lower volume"),
    KeyChord([mod], "s", [
        Key([], "u", lazy.group['scratchpad'].dropdown_toggle('term')),
        Key([], "t", lazy.group['scratchpad'].dropdown_toggle('trayer')),
    ])
]

def latest_group(qtile):
    qtile.current_screen.set_group(qtile.current_screen.previous_group)

keys += [Key([mod], "Tab", lazy.function(latest_group))]

groups = [
    Group("", layout="max", matches=[Match(wm_class=["navigator", "firefox", "brave"])]),
    Group("", layout="monadwide", matches=[Match(wm_class=["Emacs"])]),
    Group("", layout="treetab", matches=[Match(wm_class=['mpv']), Match(title=['fm-video'])]),
    Group("", layout="treetab", matches=[Match(wm_class=['zathura']), Match(title=['fm-pdf'])]),
    Group("", layout="treetab", matches=[Match(wm_class=["audacious"])]),
    Group("", layout="monadwide", matches=[Match(wm_class=["Alacritty"])]),
    Group("", layout="treetab", matches=[Match(wm_class=["heroic", "Steam"])]),
    ScratchPad("scratchpad", [
        # add a alternative config file for transparency to work properly on wayland
        DropDown("term", "alacritty --config-file /home/cse/.config/alacritty/alacritty2.yml -t scratchpad", y=0.6),
        DropDown("trayer", "trayer --widthtype request", x=0.5, y=0.9),
        ]),
]

for k, group in zip(["1", "2", "3", "4", "5", "q", "g"], groups):
    keys.append(Key([mod], k, lazy.group[group.name].toscreen()))
    keys.append(Key([mod, 'shift'], k, lazy.window.togroup(group.name)))

layouts = my_layouts()

widget_defaults = dict(
    background=colors[0],
    font="Font Awesome 6 Free Solid",
    fontsize=14,
    padding=4,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            my_widgets()
            ,
            20,
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
cursor_warp = False
floating_layout = layout.Floating(
    border_focus = colors[9],
    border_normal = '#98971a',
    border_width = 2,
    margin = 2,
    float_rules=my_rules,
)
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
