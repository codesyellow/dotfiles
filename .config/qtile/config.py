import os, subprocess
# imports
from libqtile import layout, bar, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord, ScratchPad, DropDown
from libqtile.lazy import lazy
from qtile_extras import widget
from libqtile.backend.wayland import InputConfig
from configs.variables import *
from configs.hooks import *
from configs.scratchpads import *
from configs.functions import *
from configs.layouts import *

wl_input_rules = {
    "*": InputConfig(left_handed=False, pointer_accel=True),
    "type:keyboard": InputConfig(kb_options="ctrl:nocaps,compose:ralt"),
}

groups = [
        Group(icons[0], layout='max', matches=[has_class(['navigator', 'firefox', 'Brave-browser', 'qutebrowser', 'org.qutebrowser.qutebrowser', 'floorp'])]),
        Group(icons[1], layout='monadwide', matches=[has_class(['Emacs', 'code'])]),
        Group(icons[2], layout='treetab', matches=[has_class(['mpv', 'Microsoft-edge', 'YouTube Music'])]), 
        Group(icons[3], layout='treetab', matches=[has_class(['zathura'])]), 
        Group(icons[4], layout='treetab', matches=[has_class(['audacious'])]),
        Group(icons[5], layout='monadwide', matches=[has_class(['Alacritty', 'st'])]),
        Group(icons[6], layout='treetab', matches=[has_class(['heroic', 'Steam', 'amazon games ui.exe', 'bottles', 'ProtonUp-Qt', 'lutris', 'amazongamessetup.exe', 'net.davidotek.pupgui2']), 
                                                   has_name(['Steam - Self Updater', 
                                                             'Steam setup', 'Steam', 'Sign in to Steam'] )]),
                                                   Group(icons[7], layout='max', matches=[has_class(['Waydroid'])]),
                                                   ScratchPad('scratchpad', scratchpads),
                                                   ]
# bindings
keys = [
        Key([mod], 'j', lazy.layout.down()),
        Key([mod], 'k', lazy.layout.up()),
        Key([mod, 'shift'], 'k', lazy.layout.shuffle_down()),
        Key([mod, 'shift'], 'j', lazy.layout.shuffle_up()),
        Key([mod, 'shift'], 's', lazy.layout.swap_main()),
        Key([mod, 'shift'], 'space', lazy.layout.flip()),
        Key([mod], 't', lazy.spawn(term)),
        Key([alt_mod], 't', lazy.spawn(term)),
        Key([mod, 'shift'], 'c', lazy.window.kill()),
        Key([mod, 'control'], 'r', lazy.reload_config()),
        Key([mod, 'control'], 'q', lazy.shutdown()),
        Key([mod], 'b', lazy.group.focus_back()),
        # apps
        Key([mod], 'f', lazy.window.toggle_fullscreen()),
        Key([mod, 'shift'], 'f', lazy.window.toggle_floating()),
        Key([mod], 'c', lazy.window.center()),
        Key([mod, 'shift'], 'm', lazy.spawn('alacritty -t fm-video -e lf /home/cse/.courses')),
        Key([mod, 'shift'], 'e', lazy.core.change_vt(2)),
        Key([alt_mod], 'd', lazy.spawn(runner)),
        KeyChord([mod], "v", [
            Key([], 'j', lazy.spawn('volume.sh down')),
            Key([], 'k', lazy.spawn('volume.sh up')),
            Key([], 'm', lazy.spawn('swayosd-client --output-volume mute-toggle')),
            ],
                 mode=True,
                 name="󰕾"
                 ),
        Key([mod], "space", lazy.widget["keyboardlayout"].next_keyboard(), desc="Next keyboard layout."),
        #Key([mod], 'e', lazy.spawn(term + ' --class code -e lvim -c "cd ~/.code | NvimTreeToggle"')),
        KeyChord([mod], 'e',[
            Key([], 'r', lazy.spawn(runner)),
            KeyChord([], 'g', [
                Key([], 's', lazy.spawn('steam')),
                Key([], 'h', lazy.spawn('heroic')),
                Key([], 'w', lazy.spawn('waydroid show-full-ui')),
                Key([], 'd', lazy.spawn('dsbattery -d')),
                Key([], 'r', lazy.spawn('flatpak run io.github.vinegarhq.Vinegar player')),
                ],
                     name="󱎓"
                     ),
            KeyChord([], 'p', [
                Key([], 'l', lazy.spawn('pymor -l 3')),
                Key([], 's', lazy.spawn('pymor')),
                Key([], 'c', lazy.spawn('pymor -c')),
                ],
                 name="󰁫"
                     ),
            Key([], 'n', lazy.spawn('dunstctl close-all')),
            ],

                 name="󰳽"
                 ),
    Key([mod], 'Tab', lazy.function(latest_group)),
    Key([mod, 'shift'], 'p', lazy.function(focus_main)),
    KeyChord([mod], 's', [
        Key([], 'u', lazy.group['scratchpad'].dropdown_toggle('term')),
        Key([], 'g', lazy.group['scratchpad'].dropdown_toggle('gpterm')),
        Key([], 't', lazy.group['scratchpad'].dropdown_toggle('task'), lazy.spawn('task sync')),
        Key([], 'n', lazy.group['scratchpad'].dropdown_toggle('neorg')),
        Key([], 'm', lazy.group['scratchpad'].dropdown_toggle('btop')),
        Key([], 'i', lazy.group['scratchpad'].dropdown_toggle('tt')),
        ],
             name="󰊠"
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
             name=""
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
             name=""
             ),

# actions
    KeyChord([mod], 'a', [
        Key([], 'h', lazy.core.hide_cursor()),
        Key([], 's', lazy.core.unhide_cursor()),
        KeyChord([], 'l', [
            Key([], 'k', lazy.layout.shuffle_down()),
            Key([], 'j', lazy.layout.shuffle_up()),
            Key([], 's', lazy.layout.swap_main()),
            Key([], 'space', lazy.layout.flip()),
            ],
                 name=''),
        KeyChord([], 'w', [
            Key([], 'k', lazy.window.kill()),
            KeyChord([], "r", [
                Key([], 'i', lazy.layout.grow()),
                Key([], 'd', lazy.layout.shrink()),
                Key([], 'n', lazy.layout.normalize()),
                Key([], 'm', lazy.layout.maximize()),
                Key([], 'r', lazy.layout.reset()),
                ],
                     mode=True,
                     name=""
                     ),
            ],
                 name=''),
        KeyChord([], 'q', [
            Key([], 'r', lazy.reload_config()),
            Key([], 'q', lazy.shutdown()),
            ],
                 name=''),
        KeyChord([], 'e', [
            Key([], 'e', lazy.spawn('flatpak run com.github.wwmm.easyeffects -l LoudnessEqualizer')),
            Key([], 'b', lazy.spawn('flatpak run com.github.wwmm.easyeffects -l "my-heavy-bass"')),
            ],
                 name=""
                 ),
        ],
             name=""
             ),
]

my_widgets = [
        widget.GroupBox(
            active=colors[20],
            background=bg,
            block_highlight_text_color=colors[1],
            disable_drag=True,
            highlight_method='line',
            highlight_color=[colors[15]],
            fontsize=14,
            inactive=colors[12],
            use_mouse_wheel=False,
            ),
        widget.CurrentLayoutIcon(),
        widget.Spacer(
            background="#00000069",
            ),
        widget.Clock(
            font=my_font,
            background=bg,
            foreground=colors[18],
            format='%d|%H:%M|%a',
            ),
        widget.Spacer(
            background="#00000069",
            ),
        widget.Chord(
            background=bg,
            foreground=colors[20],
            ),
        widget.KeyboardLayout(
            background=bg,
            configured_keyboards=['us', 'us intl'],
            display_map={
                'us':'  US',
                'us intl':'  USI',
                },
            foreground=colors[18],
            option='compose:menu,grp_led:scroll',
            ),
        widget.GenPollText(
            background=bg,
            foreground=colors[21],
            func=lambda: subprocess.check_output(os.path.expanduser("~/.bin/psbat.sh")).decode("utf-8"),
            mouse_callbacks={'Button1': desconnect_ds4 },
            update_interval=60, 
            ),
        widget.DF(
            background=bg,
            font=my_font,
            foreground=colors[16],
            format=' {uf}{m}',
            partition='/',
            visible_on_warn=False,
            ),
        widget.DF(
            background=bg,
            font=my_font,
            foreground=colors[19],
            partition='/home',
            format='  {uf}{m}',
            visible_on_warn=False,
            ),
        widget.CPU(
            background=bg,
                font=my_font,
                foreground=colors[13],
                format='  {freq_current}GHz|{load_percent}%',
                ),
        widget.Memory(
            background=bg,
                font=my_font,
                foreground=colors[14],
                format='󰍛{MemUsed: .0f}{mm}',
                ),
        widget.Spacer(length=2),
        widget.StatusNotifier(),
        widget.Spacer(length=2),
        widget.QuickExit(
            background=bg,
                default_text='', countdown_format='',
                font=exit_icon_font,
                ),
        widget.Spacer(length=6),
        ]

widget_defaults = dict(
        background="#00000069",
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
            Match(wm_class='blueman-manager'),
            Match(wm_class='org.kde.polkit-kde-authentication-agent-1'),
            Match(wm_class='CachyOSHello'),
            ]
        )
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"
