# imports
import os, subprocess
from libqtile import hook, layout, bar, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.log_utils import logger
from qtile_extras import widget
from libqtile.backend.wayland import InputConfig

# variables
alt_mod = "mod1"
browser = 'firefox'
exit_icon_font = 'Font Awesome 6 Free Regular'
home = os.path.expanduser('~/')
mod = "mod4"
my_font = 'JetBrainMono Nerd Font'
pad = 10
terminal = 'alacritty'
runner=''

# wayland, x11
if qtile.core.name == "x11":
    term = "urxvt"
    runner = 'dmenu_run'
elif qtile.core.name == "wayland":
    term = "foot"
    runner = 'dmenu-wl_run'
    @hook.subscribe.startup_once
    def autostart():
        home = os.path.expanduser('~/.config/qtile/wl_autostart.sh')
        subprocess.Popen([home])
    wl_input_rules = {
            "*": InputConfig(left_handed=False, pointer_accel=False),
            "type:keyboard": InputConfig(kb_options="ctrl:nocaps,compose:ralt", kb_layout=('br'), kb_variant=('nodeadkeys')),
            }

icons = [
        '',
        '󰶞',
        '',
        '',
        '',
        '',
        '',
        '',
        ]

# hooks
@hook.subscribe.client_focus
def opacity(c):
    for x in c.qtile.current_group.windows:
        wm_class = x.get_wm_class()[0]
        logger.warning(x.get_wm_class())
        if (wm_class == 'firefox' 
            or wm_class == 'org.qutebrowser.qutebrowser'
            or wm_class == 'qutebrowser'
            or wm_class == 'Brave-browser'):
            x.opacity = 1
        if x.has_focus and x.name == 'scratchpad' or x.name == 'chatgpt':
            for w in x.group.windows:
                w.opacity = 1
        elif not x.has_focus:
            x.opacity = 0.5
        else:
            x.opacity = 1 

@hook.subscribe.client_focus
def is_floating(c):
    for x in c.qtile.current_group.windows:
        if x.has_focus and x.floating and x.name != 'scratchpad' and not x.fullscreen:
            if x.get_wm_class()[0] == 'firefox' or x.get_wm_class()[0] == 'Navigator':
                x.set_size_floating(500,680)
            x.center()


scratchpads = [
        # add a alternative config file for transparency to work properly on wayland
        DropDown(
            'term', 
            f'alacritty --config-file {home}.config/alacritty/alacritty2.yml -t scratchpad',
            y=0,
            ),
        DropDown(
            'gpterm',
            'alacritty -t scratchpad -e bard-cli -i',
            height=0.995,
            width=0.3,
            opacity=0.5,
            x=0.698,
            y=0,
            on_focus_lost_hide=False
            ),
        DropDown(
            'task',
            'foot -T scratchpad -e taskwarrior-tui',
            height=0.995,
            width=0.3,
            opacity=0.5,
            x=0.698,
            y=0,
            on_focus_lost_hide=False
            ),
        DropDown(
            'btop',
            'foot -T scratchpad -e btop',
            height=0.9,
            width=0.9,
            opacity=0.5,
            x=0,
            y=0,
            on_focus_lost_hide=False
            ),
        DropDown(
            'neorg', 
            'foot -T neorg -e /usr/bin/nvim -c ":Neorg workspace home"', 
            x=0.001,
            height=0.992,
            width=0.3,
            opacity=0.9,
            on_focus_lost_hide=False),
        ]

colors = ['#1E2326', # bg_dim 0
          '#272E33', # bg0 1
          '#2E383C', # bg1 2
          '#374145', # bg2 3
          '#414B50', # bg3 4
          '#495156', # bg4 5
          '#4F5B58', # bg5 6
          '#4C3743', # bg_red 7
          '#493B40', # bg_visual 8
          '#45443C', # bg_yellow 9
          '#3C4841', # bg_green 10
          '#384B55', # bg_blue 11
          '#E67E80', # red 12
          '#E69875', # orange 13
          '#DBBC7F', # yellow 14
          '#A7C080', # green 15
          '#7FBBB3', # blue 16
          '#83C092', # aqua 17
          '#D699B6', # purple 18
          '#D3C6AA', # fg 19
          '#A7C080', # statusline1 20
          '#D3C6AA', # statusline2 21
          '#E67E80', # statusline3 22
          '#7A8478', # gray0 23
          '#859289', # gray1 24
          '#9DA9A0', # gray2 25
          ]

def latest_group(qtile):
    qtile.current_screen.set_group(qtile.current_screen.previous_group)

def focus_main(qtile):
    window = qtile.current_group.layout.focus_first()
    qtile.current_group.focus(window)

def has_class(c):
    return Match(wm_class=c)

def has_name(c):
    return Match(title=c)


groups = [
        Group(icons[0], layout='max', matches=[has_class(['navigator', 'firefox', 'Brave-browser', 'qutebrowser', 'org.qutebrowser.qutebrowser'])]),
        Group(icons[1], layout='monadwide', matches=[has_class(['Emacs', 'code'])]),
        Group(icons[2], layout='treetab', matches=[has_class(['mpv', 'Microsoft-edge'])]), 
        Group(icons[3], layout='treetab', matches=[has_class(['zathura'])]), 
        Group(icons[4], layout='treetab', matches=[has_class(['audacious'])]),
        Group(icons[5], layout='monadwide', matches=[has_class(['Alacritty', 'foot'])]),
        Group(icons[6], layout='treetab', matches=[has_class(['heroic', 'Steam', 'amazon games ui.exe', 'bottles', 'ProtonUp-Qt', 'lutris', 'amazongamessetup.exe']), 
                                                   has_name(['Steam - Self Updater', 
                                                             'Steam setup', 'Steam', 'Sign in to Steam'] )]),
                                                   Group(icons[7], layout='max', matches=[has_class(['Waydroid'])]),
                                                   ScratchPad('scratchpad', scratchpads),
                                                   ]
# bindings
keys = [
        Key([mod], 'h', lazy.layout.left()),
        Key([mod], 'l', lazy.layout.right()),
        Key([mod], 'j', lazy.layout.down()),
        Key([mod], 'k', lazy.layout.up()),
        Key([mod, 'shift'], 'h', lazy.layout.swap_left()),
        Key([mod, 'shift'], 'l', lazy.layout.swap_right()),
        Key([mod, 'shift'], 'j', lazy.layout.shuffle_down()),
        Key([mod, 'shift'], 'k', lazy.layout.shuffle_up()),
        KeyChord([mod], "r", [
            Key([], 'i', lazy.layout.grow()),
            Key([], 'd', lazy.layout.shrink()),
            Key([], 'n', lazy.layout.normalize()),
            Key([], 'm', lazy.layout.maximize()),
            Key([], 'r', lazy.layout.reset()),
            ],
                 mode=True,
                 name="Resize"
                 ),
        Key([mod, 'shift'], 's', lazy.layout.swap_main()),
        Key([mod, 'shift'], 'space', lazy.layout.flip()),
        Key([mod, 'shift'], 'Return', lazy.layout.toggle_split()),
        Key([mod], 't', lazy.spawn(terminal)),
        Key([alt_mod], 't', lazy.spawn(terminal)),
        Key([mod], '0', lazy.next_layout()),
        Key([mod, 'shift'], 'c', lazy.window.kill()),
        Key([mod, 'control'], 'r', lazy.reload_config()),
        Key([alt_mod, 'control'], 'r', lazy.reload_config()),
        Key([mod, 'control'], 'q', lazy.shutdown()),
        Key([mod], 'b', lazy.group.focus_back()),
        # apps
        Key([mod], 'f', lazy.window.toggle_fullscreen()),
        Key([mod, 'shift'], 'f', lazy.window.toggle_floating()),
        Key([mod], 'c', lazy.window.center()),
        Key([mod, 'shift'], 'm', lazy.spawn('alacritty -t fm-video -e lf /home/cse/.courses')),
        Key([mod, 'shift'], 'e', lazy.core.change_vt(2)),
        Key([mod], 'd', lazy.spawn(runner)),
        Key([alt_mod], 'd', lazy.spawn(runner)),
        KeyChord([mod], "v", [
            Key([], 'k', lazy.spawn('swayosd-client --output-volume raise')),
            Key([], 'j', lazy.spawn('swayosd-client --output-volume lower')),
            ],
                 mode=True,
                 name="Volume"
                 ),
        Key([mod], "space", lazy.widget["keyboardlayout"].next_keyboard(), desc="Next keyboard layout."),
        #Key([mod], 'e', lazy.spawn(terminal + ' --class code -e nvim -c "cd ~/.code | NvimTreeToggle"')),
        KeyChord([mod], 'e',[
            KeyChord([], 'g', [
                Key([], 's', lazy.spawn('steam')),
                Key([], 'h', lazy.spawn('heroic')),
                Key([], 'w', lazy.spawn('waydroid show-full-ui')),
                ]),
            Key([], 'p', lazy.spawn('pymor -l 3')),
            Key([], 'n', lazy.spawn('dunstctl close-all')),
            ],

                 name="EXEC"
                 ),
    Key([mod], 'Tab', lazy.function(latest_group)),
    Key([mod, 'shift'], 'p', lazy.function(focus_main)),
    KeyChord([mod], 's', [
        Key([], 'u', lazy.group['scratchpad'].dropdown_toggle('term')),
        Key([], 'g', lazy.group['scratchpad'].dropdown_toggle('gpterm')),
        Key([], 't', lazy.group['scratchpad'].dropdown_toggle('task')),
        Key([], 'n', lazy.group['scratchpad'].dropdown_toggle('neorg')),
        Key([], 'm', lazy.group['scratchpad'].dropdown_toggle('btop')),
        ],
             name="SCRATCH"
             ),
    KeyChord([mod], 'w', [ 
                          Key([], 'b', lazy.group[groups[0].name].toscreen()),
                          Key([], 'c', lazy.group[groups[1].name].toscreen()),
                          Key([], 'v', lazy.group[groups[2].name].toscreen()),
                          Key([], 'r', lazy.group[groups[3].name].toscreen()),
                          Key([], 'e', lazy.group[groups[4].name].toscreen()),
                          Key([], 't', lazy.group[groups[5].name].toscreen()),
                          Key([], 'g', lazy.group[groups[6].name].toscreen()),
                          Key([], 'w', lazy.group[groups[7].name].toscreen()),
                          ],
             name="WKS"
             ),
    KeyChord([mod, 'shift'], 'w', [ 
                                   Key([], 'b',  lazy.window.togroup(groups[0].name)),
                                   Key([], 'c',  lazy.window.togroup(groups[1].name)),
                                   Key([], 'v',  lazy.window.togroup(groups[2].name)),
                                   Key([], 'r',  lazy.window.togroup(groups[3].name)),
                                   Key([], 'e',  lazy.window.togroup(groups[4].name)),
                                   Key([], 't',  lazy.window.togroup(groups[5].name)),
                                   Key([], 'g',  lazy.window.togroup(groups[6].name)),
                                   Key([], 'w',  lazy.window.togroup(groups[7].name)),
                                   ],
             name="MWKS"
             ),

# actions
    KeyChord([mod], 'a', [
        Key([], 'h', lazy.core.hide_cursor()),
        Key([], 's', lazy.core.unhide_cursor()),
        Key([], 'e', lazy.spawn('easy_preset.sh LoudnessEqualizer')),
        Key([], 'b', lazy.spawn('easy_preset.sh "HeavyBass"')),
        KeyChord([], 'l', [
            Key([], 'o', lazy.spawn('xset led on')),
            Key([], 'f', lazy.spawn('xset led off')),
            ])
        ]),
]

if qtile.core.name == "x11":
    keys.append(
            KeyChord([mod], "v", [
                Key([], 'k', lazy.spawn('volume.sh down')),
                Key([], 'j', lazy.spawn('volume.sh up')),
                ],
                     mode=True,
                     name="Volume"
                     ))

layouts = [
        layout.MonadWide(
            align=1,
            border_focus=colors[12],
            border_normal=colors[15],
            border_width=2,
            new_client_position='before_current',
            ratio=.8,
            single_border_width=0,
            single_margin=0,
            ),
        layout.Max(),
        layout.TreeTab(
            active_bg=colors[12],
            active_fg=colors[0],
            border_width=0,
            bg_color='#303842',
            inactive_bg=colors[0],
            place_right=True,
            previous_on_rm=True,
            sections=[''],
            section_fg=colors[0],
            vspace=0,
            ),
        ] 

floating_layout = layout.Floating(
        border_focus = colors[4],
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
            has_class('monophony'),
            has_class('Whatsapp-for-linux'),
            has_class('tuned-gui'),
            ]
        )

def open_calendar():  # spawn calendar widget
    qtile.cmd_spawn('dsbattery -d')

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
            foreground=colors[18],
            format='%d|%H:%M|%a',
            ),
        widget.Spacer(),
        widget.Chord(
            background=colors[20],
            foreground=colors[4],
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
        widget.GenPollText(
            foreground=colors[21],
            update_interval=60, 
            func=lambda: subprocess.check_output(os.path.expanduser("~/.bin/psbat.sh")).decode("utf-8"),
            mouse_callbacks={'Button1': open_calendar }
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
        widget.StatusNotifier(),
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

screens = [
        Screen(
            top=bar.Bar(
                my_widgets
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
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
        float_rules=[
            # Run the utility of `xprop` to see the wm class and name of an X client.
            *layout.Floating.default_float_rules,
            Match(wm_class="confirmreset"),  # gitk
            Match(wm_class="makebranch"),  # gitk
            Match(wm_class="maketag"),  # gitk
            Match(wm_class="ssh-askpass"),  # ssh-askpass
            Match(title="branchdialog"),  # gitk
            Match(title="pinentry"),  # GPG key password entry
            ]
        )
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"
