from libqtile.lazy import lazy
from libqtile.config import KeyChord, Key
from .binds import keys
from .variables import mod, runner
from .functions import focus_main
from .groups import groups
from libqtile import  qtile

# exec
keys.append(KeyChord([mod], 'e',[
    Key([], 'r', lazy.spawn(runner)),
    Key([], 'v', lazy.spawn("mpvtube.sh")),
    Key([], 'n', lazy.spawn('dunstctl close-all')),
    KeyChord([], 's', [
        Key([], 'a', lazy.spawn('anki')),
        Key([], 'm', lazy.spawn('maps.sh')),
        Key([], 'v', lazy.spawn('ankiv.sh')),
    ], name="  |"),
    KeyChord([], 'p', [
        Key([], 'l', lazy.spawn('pymor -t 20 -f 3')),
        Key([], 's', lazy.spawn('pymor -t 20')),
        Key([], 'c', lazy.spawn('pymor -c')),
    ], name="󰁫  |"
             ),
], name="  |"))

# scratchpds 
keys.append(
    KeyChord([mod], 's', [
        Key([], 'u', lazy.group['scratchpad'].dropdown_toggle('term')),
        Key([], 'i', lazy.group['scratchpad'].dropdown_toggle('ai')),
        Key([], 's', lazy.group['scratchpad'].dropdown_toggle('trayer')),
        Key([], 'g', lazy.group['scratchpad'].dropdown_toggle('gpterm')),
        Key([], 'w', lazy.group['scratchpad'].dropdown_toggle('zap')),
        Key([], 'c', lazy.group['scratchpad'].dropdown_toggle('cmus')),
        Key([], 't', lazy.group['scratchpad'].dropdown_toggle('task')),
        Key([], 'n', lazy.group['scratchpad'].dropdown_toggle('neorg')),
        Key([], 'm', lazy.group['scratchpad'].dropdown_toggle('btop')),
        Key([], 'v', lazy.group['scratchpad'].dropdown_toggle('vimiv')),
        Key([], 'f', lazy.group['scratchpad'].dropdown_toggle('nnn')),
        Key([], 'e', lazy.group['scratchpad'].dropdown_toggle('tt')),
    ], name="󰊠  |"))

# toworkspace
keys.append(
KeyChord([mod], 'w', [
    Key([], 'b', lazy.group[groups[0].name].toscreen()),
    Key([], 'v', lazy.group[groups[1].name].toscreen()),
    Key([], 't', lazy.group[groups[2].name].toscreen()),
    Key([], 'g', lazy.group[groups[3].name].toscreen()),
    Key([], 'm', lazy.group[groups[4].name].toscreen()),
    Key([], 'e', lazy.group[groups[5].name].toscreen()),
    ], name="  |"))

keys.append(
    KeyChord([mod, 'shift'], 'w', [
        Key([], 'b',  lazy.window.togroup(groups[0].name)),
        Key([], 'v',  lazy.window.togroup(groups[1].name)),
        Key([], 't',  lazy.window.togroup(groups[2].name)),
        Key([], 'g',  lazy.window.togroup(groups[3].name)),
        Key([], 'm',  lazy.window.togroup(groups[4].name)),
        Key([], 'e',  lazy.window.togroup(groups[5].name)),
    ], name="  |"))

# action
keys.append(
    KeyChord([mod], 'a', [
        #Key([], 'h', lazy.core.hide_cursor()),
        #Key([], 's', lazy.core.unhide_cursor()),
        Key([], 'k', lazy.window.kill()),
        KeyChord([], "r", [
                Key([], 'i', lazy.layout.grow()),
                Key([], 'd', lazy.layout.shrink()),
                Key([], 'n', lazy.layout.normalize()),
                Key([], 'm', lazy.layout.maximize()),
                Key([], 'r', lazy.layout.reset()),
            ], mode=True, name="  |"),
        KeyChord([], 'l', [
            Key([], 'k', lazy.layout.shuffle_down()),
            Key([], 'j', lazy.layout.shuffle_up()),
            Key([], 's', lazy.layout.swap_main()),
            Key([], 'm', lazy.function(focus_main)),
            Key([], 'b', lazy.group.focus_back()),
            Key([], 'space', lazy.layout.flip()),
        ], name='  |'),
        KeyChord([], 'q', [
            Key([], 'r', lazy.reload_config()),
            Key([], 'e', lazy.shutdown()),
            Key([], 'i', lazy.spawn('getwindow.sh')),
        ], name='  |'),
        KeyChord([], 'e', [
            Key([], 'l', lazy.spawn('easyeffects -l LoudnessEqualizer')),
            Key([], 'b', lazy.spawn('easyeffects -l "HeavyBass"')),
        ], name=""),
    ], name="  |"))

# audio
if qtile.core.name == "x11":
    keys.append(KeyChord([mod], "v", [
        Key([], 'j', lazy.spawn('volume.sh down')),
        Key([], 'k', lazy.spawn('volume.sh up')),
        Key([], 'm', lazy.spawn('volume.sh mute')),
        ], mode=True, name="󰕾  |"))

elif qtile.core.name == "wayland":
    keys.append(KeyChord([mod], "v", [
        Key([], 'j', lazy.spawn('swayosd-client --output-volume lower')),
        Key([], 'k', lazy.spawn('swayosd-client --output-volume raise')),
        Key([], 'm', lazy.spawn('swayosd-client --output-volume mute-toggle')),
        ], mode=True, name="󰕾  |"))

