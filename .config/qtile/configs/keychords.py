# type: ignore
from libqtile.lazy import lazy
from libqtile.config import KeyChord, Key
from .binds import keys
from .variables import mod, runner, browser, colors
from .functions import focus_main
from .groups import groups
from libqtile import qtile

# exec
keys.append(KeyChord([mod], 'e', [
    Key([], 'r', lazy.spawn(runner)),
    Key([], 'v', lazy.spawn("mpvtube.sh")),
    Key([], 'b', lazy.spawn(browser)),
    Key([], 'n', lazy.spawn('dunstctl close-all')),
    Key([], 't', lazy.spawn('stretch.sh -t 15 -s 12 -w 3')),
    KeyChord([], 's', [
        Key([], 'a', lazy.spawn('anki')),
        Key([], 'm', lazy.spawn('maps.sh')),
        Key([], 'v', lazy.spawn('ankiv.sh')),
    ], name=f'<span size="16000" rise="4000">󰑴</span> <span size="x-large" foreground="{colors["bg1_color"]}">|</span>'),
    KeyChord([], 'p', [
        Key([], 'l', lazy.spawn('pymor -t 20 -f 3')),
        Key([], 's', lazy.spawn('pymor -t 20')),
        Key([], 'c', lazy.spawn('pymor -c')),
    ], name=f'<span rise="2500" size="17000">󰁫</span> <span size="x-large" foreground="{colors["bg1_color"]}">|</span>'
    ),
], name=f'<span size="13000" rise="3000"></span> <span size="x-large" foreground="{colors["bg1_color"]}">|</span>'))

# scratchpds
keys.append(
    KeyChord([mod], 's', [
        Key([], 'u', lazy.group['scratchpad'].dropdown_toggle('term')),
        Key([], 'i', lazy.group['scratchpad'].dropdown_toggle('ai')),
        # Key([], 's', lazy.group['scratchpad'].dropdown_toggle('trayer')),
        Key([], 'w', lazy.group['scratchpad'].dropdown_toggle('zap')),
        Key([], 'c', lazy.group['scratchpad'].dropdown_toggle('cmus')),
        Key([], 't', lazy.group['scratchpad'].dropdown_toggle('task')),
        Key([], 'n', lazy.group['scratchpad'].dropdown_toggle('notes')),
        Key([], 'h', lazy.group['scratchpad'].dropdown_toggle('habits')),
        Key([], 'm', lazy.group['scratchpad'].dropdown_toggle('btop')),
        Key([], 'p', lazy.group['scratchpad'].dropdown_toggle('pulsemixer')),
        Key([], 'v', lazy.group['scratchpad'].dropdown_toggle('vimiv')),
        Key([], 'r', lazy.group['scratchpad'].dropdown_toggle('countdown')),
        Key([], 'f', lazy.group['scratchpad'].dropdown_toggle('yazi')),
        Key([], 'e', lazy.group['scratchpad'].dropdown_toggle('tt')),
        KeyChord([], 's', [
            Key([], 'p', lazy.group['scratchpad'].dropdown_toggle('ankivPT')),
            Key([], 'e', lazy.group['scratchpad'].dropdown_toggle('ankivEN')),
        ], name=f'<span size="16000" rise="4000">󰑴</span> <span size="x-large" foreground="{colors["bg1_color"]}">|</span>'),
        Key([], 'g', lazy.group['scratchpad'].dropdown_toggle('calc')),
    ], name=f'<span size="16000" rise="4000">󰊠</span> <span size="x-large" foreground="{colors["bg1_color"]}">|</span>'))

# toworkspace
keys.append(
    KeyChord([mod], 'w', [
        Key([], 't', lazy.group[groups[0].name].toscreen()),
        Key([], 'v', lazy.group[groups[1].name].toscreen()),
        Key([], 'b', lazy.group[groups[2].name].toscreen()),
        Key([], 'l', lazy.group[groups[3].name].toscreen()),
        Key([], 'm', lazy.group[groups[4].name].toscreen()),
        Key([], 's', lazy.group[groups[5].name].toscreen()),
        Key([], 'g', lazy.group[groups[6].name].toscreen()),
    ], name=f'<span rise="3000" size="13000"></span> <span size="x-large" foreground="{colors["bg1_color"]}">|</span>'))

keys.append(
    KeyChord([mod, 'shift'], 'w', [
        Key([], 't',  lazy.window.togroup(groups[0].name)),
        Key([], 'v',  lazy.window.togroup(groups[1].name)),
        Key([], 'b',  lazy.window.togroup(groups[2].name)),
        Key([], 'l',  lazy.window.togroup(groups[3].name)),
        Key([], 'm',  lazy.window.togroup(groups[4].name)),
        Key([], 's',  lazy.window.togroup(groups[5].name)),
        Key([], 'g',  lazy.window.togroup(groups[6].name)),
    ], name=f'<span rise="2000" size="14000"></span> <span size="x-large" foreground="{colors["bg1_color"]}">|</span>'))

# action
keys.append(
    KeyChord([mod], 'a', [
        Key([], 'k', lazy.window.kill()),
        Key([], 'b', lazy.hide_show_bar()),
        KeyChord([], "r", [
            Key([], 'i', lazy.layout.grow()),
            Key([], 'd', lazy.layout.shrink()),
            Key([], 'n', lazy.layout.normalize()),
            Key([], 'm', lazy.layout.maximize()),
            Key([], 'r', lazy.layout.reset()),
        ], mode=True, name=f'<span size="14000"rise="4000"></span> <span size="x-large" foreground="{colors["bg1_color"]}"> |</span>'),
        KeyChord([], 'l', [
            Key([], 'k', lazy.layout.shuffle_down()),
            Key([], 'j', lazy.layout.shuffle_up()),
            Key([], 's', lazy.layout.swap_main()),
            Key([], 'm', lazy.function(focus_main)),
            Key([], 'b', lazy.group.focus_back()),
            Key([], 'space', lazy.layout.flip()),
        ], name=f'<span size="13000"rise="4000"></span> <span size="x-large" foreground="{colors["bg1_color"]}">|</span>'),
        KeyChord([], 'q', [
            Key([], 'r', lazy.reload_config()),
            Key([], 'e', lazy.shutdown()),
            Key([], 'i', lazy.spawn('getwindow.sh')),
        ], name=f'<span size="13000" rise="4000"></span> <span size="x-large" foreground="{colors["bg1_color"]}">|</span>'),
        KeyChord([], 'e', [
            Key([], 'l', lazy.spawn('easyeffects -l LoudnessEqualizer')),
            Key([], 'b', lazy.spawn('easyeffects -l "HeavyBass"')),
        ], name=f'<span size="13000"rise="4000"></span> <span size="x-large" foreground="{colors["bg1_color"]}">|</span>'),
    ], name=f'<span size="13000"rise="4000"></span> <span size="x-large" foreground="{colors["bg1_color"]}">|</span>'))

# audio
if qtile.core.name == "x11":
    keys.append(KeyChord([mod], "v", [
        Key([], 'j', lazy.spawn('changevolume.sh "-" 5')),
        Key([], 'k', lazy.spawn('changevolume.sh 5')),
        Key([], 'm', lazy.spawn('changevolume.sh "m"')),
    ], name=f'<span size="15000" rise="4000">󰕾</span> <span size="x-large" foreground="{colors["bg1_color"]}">|</span>'))

elif qtile.core.name == "wayland":
    keys.append(KeyChord([mod], "v", [
        Key([], 'j', lazy.spawn('swayosd-client --output-volume lower')),
        Key([], 'k', lazy.spawn('swayosd-client --output-volume raise')),
        Key([], 'm', lazy.spawn('swayosd-client --output-volume mute-toggle')),
    ], mode=True, name=f'<span size="17000" rise="2000">󰕾</span> <span size="x-large" foreground="#d8dee9"> |</span>')),
