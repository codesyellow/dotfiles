import os, subprocess
from libqtile import bar, layout, hook, widget, qtile
from libqtile.config import Click, Drag, Group, ScratchPad, DropDown, Key, Match, Screen, KeyChord
from libqtile.lazy import lazy
from libqtile.backend.wayland import InputConfig
from libqtile.log_utils import logger

# to do
## focus main window
    ## maybe focus by name in group doc
## change virtual console
## if on max show number of windows on widget
## not transparency when scratchpad on top of a terminal window
# wayland
## hide cursor automacally

# important variables
bar_icons_font = 'Symbols Nerd Font Mono'
browser = 'qutebrowser'
mod = 'mod3'
alt_mod = 'mod4'
icons = [
    '',
    '',
    '',
    '',
    '',
    '',
    '',
]
my_font = 'JetBrainMono Nerd Font'
alternative_font = 'Font Awesome 6 Free'
pad = 10
if qtile.core.name == "x11":
    runner = f'dmenu_run -dim 0.3 -fn "{my_font}"' 
elif qtile.core.name == "wayland":
    runner = 'dmenu_run -h 20 -nb #2e3440 -fn "JetBrainMono Nerd Font"'
terminal = 'alacritty'
dropdown = [
        # add a alternative config file for transparency to work properly on wayland
        DropDown("term", "alacritty --config-file /home/codesyellow/.config/alacritty/alacritty2.yml -t scratchpad", y=0.6),
        DropDown("gpterm", "alacritty --class ScratchPad -e gpterm", height=0.9, width=0.9, opacity=0.9),
        ]

if qtile.core.name == 'wayland':
    dropdown.append(DropDown("trayer", "trayer --widthtype request --transparent true --alpha 255", x=0.5, y=0.9))

# functions
def latest_group(qtile):
    qtile.current_screen.set_group(qtile.current_screen.previous_group)

def focus_main(qtile):
    window = qtile.current_group.layout.focus_first()
    qtile.current_group.focus(window)

def swap_main(qtile):
    lazy.layout.swap_main()

def has_class(c):
    return Match(wm_class=c)

def has_name(c):
    return Match(title=c)

#Colors for the bar
def init_colors():
    return [["#272e33", "#272e33"], # color 0  background color
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
                border_focus=colors[12],
                border_normal=colors[4],
                border_width=1,
                new_client_position='before_current',
                ratio=.6,
                single_border_width=0,
                single_margin=0,
                ),
            layout.Max(),
            layout.TreeTab(
                active_bg=colors[5],
                active_fg=colors[0],
                border_width=0,
                bg_color=colors[0],
                inactive_bg=colors[0],
                place_right=True,
                section_fg=colors[0],
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
                font=my_font,
                format='%d|%b %H:%M %a',
            ),
            widget.Spacer(),
            widget.Net(
                foreground=colors[8],
                format=' {down} |  {up}',
                ),
            widget.Spacer(length=4),
            widget.PulseVolume(
                font=my_font,
                foreground=colors[11]
                ),
            widget.Spacer(length=4),
            widget.DF(
                font=my_font,
                foreground=colors[14],
                visible_on_warn=False,
            ),
            widget.Spacer(length=4),
            widget.CPU(
                font=my_font,
                foreground=colors[12],
                format='{freq_current}GHz|{load_percent}%',
            ),
            widget.Spacer(length=-4),
            widget.Memory(
                font=my_font,
                foreground=colors[16],
                format='{MemUsed: .0f}{mm}',
            ),
            widget.Spacer(length=4),
            widget.Systray(),
            widget.Spacer(length=4),
            widget.QuickExit(
                default_text='🚪', countdown_format='',
                font=alternative_font,
            ),
            widget.Spacer(length=6),
]

# hooks
@hook.subscribe.client_focus
def opacity(c):
    for x in c.qtile.current_group.windows:
        set_opacity = x.set_opacity
        wm_class = x.get_wm_class()[0]
        if (wm_class == 'firefox' 
            or wm_class == 'org.qutebrowser.qutebrowser'
            or wm_class == 'qutebrowser'):
            set_opacity(1) 
        if x.has_focus and x.name == 'scratchpad':
            for w in x.group.windows:
                w.set_opacity(1)
        elif not x.has_focus:
            set_opacity(0.5)
        elif x.has_focus:
            set_opacity(1) 
        
if qtile.core.name == "wayland":
    @hook.subscribe.startup_once
    def autostart():
        home = os.path.expanduser('~/.config/qtile/wl_autostart.sh')
        subprocess.Popen([home])

@hook.subscribe.client_managed
def center_float(c):
    if c.floating:
        c.cmd_center()

if qtile.core.name == "wayland":
    wl_input_rules = {
        "*": InputConfig(pointer_accel=False),
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
    Key([mod, 'shift'], "s", lazy.layout.swap_main()),
    Key([mod, "shift"], "space", lazy.layout.flip()),
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod], "t", lazy.spawn(terminal)),
    Key([alt_mod], "t", lazy.spawn(terminal)),
    Key([mod], "0", lazy.next_layout()),
    Key([mod, 'shift'], "c", lazy.window.kill()),
    Key([mod, "control"], "r", lazy.reload_config()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),
    Key([mod], "b", lazy.group.focus_back()),
    # apps
    Key([mod], "w", lazy.spawn(browser)),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod, 'shift'], "f", lazy.window.toggle_floating()),
    Key([mod], "c", lazy.window.center()),
    Key([mod, 'shift'], "m", lazy.spawn('alacritty -t fm-video -e lf /home/cse/.courses')),
    Key([mod, 'shift'], "e", lazy.core.change_vt(1)),
    Key([mod], "d", lazy.spawn(runner)),
    Key([alt_mod], "d", lazy.spawn(runner)),
    Key([mod, 'shift'], "a", lazy.spawn('volume.sh up')),
    Key([mod, 'shift'], "d", lazy.spawn('volume.sh down')),
    Key([mod, 'shift'], "t", lazy.spawn(terminal + ' --config-file /home/cse/.config/alacritty/clima.yml -t clima')),
    Key([mod], "Tab", lazy.function(latest_group)),
    Key([mod, 'shift'], "p", lazy.function(focus_main)),
    KeyChord([mod], "s", [
        Key([], "u", lazy.group['scratchpad'].dropdown_toggle('term')),
        Key([], "g", lazy.group['scratchpad'].dropdown_toggle('gpterm')),
        Key([], "t", lazy.group['scratchpad'].dropdown_toggle('trayer')),
        Key([], "m", lazy.group['scratchpad'].dropdown_toggle('btop')),
    ]),
    # actions
    KeyChord([mod], "a", [
        Key([], "h", lazy.core.hide_cursor()),
        Key([], "s", lazy.core.unhide_cursor()),
        Key([], "e", lazy.spawn('easyeffects -l LoudnessEqualizer')),
        Key([], "b", lazy.spawn('easyeffects -l "Heavy Bass"')),
        KeyChord([], 'l', [
            Key([], "o", lazy.spawn('xset led on')),
            Key([], "f", lazy.spawn('xset led off')),
            ])
    ]),
]


groups = [
    Group(icons[0], layout="max", matches=[has_class(['navigator', 'firefox', 'Brave-browser', 'qutebrowser', 'org.qutebrowser.qutebrowser'])]),
    Group(icons[1], layout="monadwide", matches=[has_class(['Emacs'])]),
    Group(icons[2], layout="treetab", matches=[has_class(['mpv'])]), 
    Group(icons[3], layout="treetab", matches=[has_class(['zathura'])]), 
    Group(icons[4], layout="treetab", matches=[has_class(["audacious"])]),
    Group(icons[5], layout="monadwide", matches=[has_class(["Alacritty"])]),
    Group(icons[6], layout="treetab", matches=[has_class(["heroic", "Steam", 'amazon games ui.exe', 'bottles', 'ProtonUp-Qt', 'lutris']), 
                                            has_name(['Steam - Self Updater', 
                                                         'Steam setup', 'Steam'] )]),
    ScratchPad("scratchpad", dropdown),
]

for k, group in zip(["1", "2", "3", "4", "5", "q", "g"], groups):
    keys.append(Key([mod], k, lazy.group[group.name].toscreen()))
    keys.append(Key([mod, 'shift'], k, lazy.window.togroup(group.name)))

layouts = my_layouts()

widget_defaults = dict(
    background=colors[0],
    font=bar_icons_font,
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
        has_class("pavucontrol"),
        has_class("com.github.wwmm.easyeffects"),
        has_class("net.davidotek.pupgui2"),
        has_class('moderndeck'),
        has_class('ProtonUp-Qt'),
        has_class('monophony'),
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
