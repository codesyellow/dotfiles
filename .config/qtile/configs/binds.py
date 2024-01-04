from libqtile.lazy import lazy
from libqtile.config import Click, Drag, Key, KeyChord 
from .variables import mod, alt_mod, runner, term
from .functions import latest_group, focus_main
from libqtile import  qtile
from .groups import groups

# bindings
keys = [
        Key([mod], 'j', lazy.layout.down()),
        Key([mod], 'k', lazy.layout.up()),
        Key([mod, 'shift'], 'k', lazy.layout.shuffle_down()),
        Key([mod, 'shift'], 'j', lazy.layout.shuffle_up()),
        Key([mod], 't', lazy.spawn(term)),
        Key([alt_mod], 't', lazy.spawn(term)),
        Key([mod, 'control'], 'r', lazy.reload_config()),
        Key([mod, 'control'], 'q', lazy.shutdown()),
        # apps
        Key([mod], 'f', lazy.window.toggle_fullscreen()),
        Key([mod, 'shift'], 'f', lazy.window.toggle_floating()),
        Key([mod], 'c', lazy.window.center()),
        Key([mod, 'shift'], 'm', lazy.spawn('alacritty -t fm-video -e lf /home/cse/.courses')),
        Key([mod, 'shift'], 'e', lazy.core.change_vt(2)),
        KeyChord([mod], "v", [
            Key([], 'j', lazy.spawn('swayosd-client --output-volume lower')), 
            Key([], 'k', lazy.spawn('swayosd-client --output-volume raise')),
            Key([], 'm', lazy.spawn('swayosd-client --output-volume mute-toggle')),
            ],
                 mode=True,
                 name="󰕾"
                 ),
        Key([mod], "space", lazy.widget["keyboardlayout"].next_keyboard(), desc="Next keyboard layout."),
        #Key([mod], 'e', lazy.spawn(term + ' --class code -e lvim -c "cd ~/.code | NvimTreeToggle"')),
        # exec
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
            KeyChord([], 's', [
                Key([], 'a', lazy.spawn('anki')),
                Key([], 'm', lazy.spawn('maps.sh')),
                Key([], 'v', lazy.spawn('ankiv.sh')),
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
        Key([], 'v', lazy.group['scratchpad'].dropdown_toggle('vimiv')),
        Key([], 'f', lazy.group['scratchpad'].dropdown_toggle('nnn')),
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
                          Key([], 'a', lazy.group[groups[7].name].toscreen()),
                          Key([], 'm', lazy.group[groups[8].name].toscreen()),
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
                                   Key([], 'a',  lazy.window.togroup(groups[7].name)),
                                   Key([], 'm',  lazy.window.togroup(groups[8].name)),
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
            Key([], 'm', lazy.function(focus_main)),
            Key([], 'b', lazy.group.focus_back()),
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
            Key([], '.', lazy.shutdown()),
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

mouse = [
        Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
        Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
        Click([mod], "Button2", lazy.window.bring_to_front()),
        ]

