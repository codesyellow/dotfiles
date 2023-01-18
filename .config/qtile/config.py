import os, subprocess
from libqtile import bar, layout, hook, widget
from libqtile.config import Click, Drag, Group, ScratchPad, DropDown, Key, Match, Screen, KeyChord
from libqtile.lazy import lazy
from libqtile.backend.wayland import InputConfig
from libqtile.log_utils import logger

# important variables
mod = "mod4"
pad = 10
runner = 'kickoff'
terminal = 'alacritty'
icons = [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
]

# functions
def latest_group(qtile):
    qtile.current_screen.set_group(qtile.current_screen.previous_group)

def swap_main(qtile):
    qtile.current_layout.cmd_swap_main()

@lazy.function
def set_layout(qtile):
    group_layout = qtile.current_layout.info()['name']
    g_name = qtile.current_group.name
    my_bar = qtile.current_screen.top
    if group_layout == 'max' and not g_name == icons[0]:
        if g_name == icons[1] or g_name == icons[5]:
            qtile.cmd_to_layout_index(0)
            return my_bar.show(True)
        else:
            #logger.warning(dir(bar))
            qtile.cmd_to_layout_index(2)
            return my_bar.show(True)
    qtile.cmd_to_layout_index(1)
    my_bar.show(False)

def my_layouts():
    return [
            layout.MonadWide(
                border_focus=colors[12],
                border_normal=colors[4],
                border_width=2,
                new_client_position='before_current',
                ratio=.6,
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
                active=colors[12],
                block_highlight_text_color=colors[5],
                highlight_method='block',
                inactive=colors[4],
            ),
            widget.CurrentLayoutIcon(),
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
                default_text='🚪', countdown_format=''
            ),
            widget.Spacer(length=6),
]

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

# hooks
@hook.subscribe.client_focus
def opacity(c):
    for x in c.qtile.current_group.windows:
        set_opacity = x.cmd_opacity
        wm_class = x.get_wm_class()[0]
        if not x.has_focus:
            set_opacity(0.5) 
        else:
            set_opacity(1) 
        if wm_class == 'firefox' or wm_class == 'qutebrowser':
            set_opacity(1) 

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

@hook.subscribe.client_managed
def center_float(c):
    if c.floating:
        c.cmd_center()

#@hook.subscribe.client_managed
#def make_float(c):
  #  for x in c.qtile.current_group.windows:
  #      if x.get_wm_class()[0] == 'com.github.wwmm.easyeffects':
  #          logger.warning(dir(x))
  #          x.cmd_enable_floating()

# rules
wl_input_rules = {
    "type:keyboard": InputConfig(kb_options="ctrl:nocaps,compose:ralt", kb_layout="br(nodeadkeys)"),
}

# bindings
keys = [
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
    Key([mod], "9", lazy.layout.reset()),
    Key([mod, 'shift'], "s", lazy.function(swap_main)),
    Key([mod, "shift"], "space", lazy.layout.flip()),
    Key( [mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod], "t", lazy.spawn(terminal)),
    # Toggle between different layouts as defined below
    Key([mod], "0", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),
    Key([mod, "control"], "r", lazy.reload_config()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),
    # apps
    Key([mod], "f", set_layout),
    Key([mod, 'shift'], "m", lazy.spawn('alacritty -t fm-video -e lf /home/cse/.courses')),
    Key([mod, 'shift'], "e", lazy.spawn('alacritty -t fm-pdf -e lf /home/cse/.ebooks')),
    Key([mod], "d", lazy.spawn(runner)),
    Key([mod, 'shift'], "a", lazy.spawn('volume.sh up')),
    Key([mod, 'shift'], "d", lazy.spawn('volume.sh down')),
    Key([mod, 'shift'], "t", lazy.spawn(terminal + ' --config-file /home/cse/.config/alacritty/clima.yml -t clima')),
    Key([mod], "Tab", lazy.function(latest_group)),
    KeyChord([mod], "s", [
        Key([], "u", lazy.group['scratchpad'].dropdown_toggle('term')),
        Key([], "t", lazy.group['scratchpad'].dropdown_toggle('trayer')),
        Key([], "m", lazy.group['scratchpad'].dropdown_toggle('btop')),
    ])
]

groups = [
    Group("", layout="max", matches=[Match(wm_class=["navigator", "firefox", "brave"])]),
    Group("", layout="monadwide", matches=[Match(wm_class=["Emacs"])]),
    Group("", layout="treetab", matches=[Match(wm_class=['mpv']), 
                                            Match(title=['fm-video'])]),
    Group("", layout="treetab", matches=[Match(wm_class=['zathura']), 
                                            Match(title=['fm-pdf'])]),
    Group("", layout="treetab", matches=[Match(wm_class=["audacious"])]),
    Group("", layout="monadwide", matches=[Match(wm_class=["Alacritty"])]),
    Group("", layout="treetab", matches=[Match(wm_class=["heroic", "Steam"]), 
                                            Match(title=['Steam - Self Updater', 
                                                         'Steam setup', 'Steam'] )]),
    ScratchPad("scratchpad", [
        # add a alternative config file for transparency to work properly on wayland
        DropDown("term", "alacritty --config-file /home/cse/.config/alacritty/alacritty2.yml -t scratchpad", y=0.6),
        DropDown("trayer", "trayer --widthtype request", x=0.5, y=0.9),
        DropDown("btop", terminal + " -t btop -e btop", height=0.6, y=0.2),
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

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

floating_layout = layout.Floating(
    border_focus = colors[9],
    border_normal = '#98971a',
    border_width = 2,
    margin = 2,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="pavucontrol"),  # ssh-askpass
        Match(wm_class="com.github.wwmm.easyeffects"),  # ssh-askpass
        Match(wm_class="ProtonUp-Qt"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True

wmname = "LG3D"
