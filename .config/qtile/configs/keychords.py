from libqtile.lazy import lazy
from libqtile.config import KeyChord, Key
from .variables import MOD, RUNNER, BROWSER, COLORS
from .groups import groups
from .binds import keys
from .functions import go_to_group, go_to_group_and_move_window


def keychord_name(icon, size, rise):
    icon = f"<span size='{size}' rise='{rise}'>{icon}</span>"
    bar = f"<span size='x-large' foreground='{COLORS['bg1']}'>|</span>"
    return f"{icon} {bar}"


keychords = [
    KeyChord([MOD], 'e', [
        Key([], 'r', lazy.spawn(RUNNER)),
        Key([], 'v', lazy.spawn("mpvtube.sh")),
        Key([], 'b', lazy.spawn(BROWSER)),
        Key([], 'n', lazy.spawn('dunstctl close-all')),
        Key([], 't', lazy.spawn('stretch.sh -t 15 -s 12 -w 3')),
        KeyChord([], 's', [
            Key([], 'a', lazy.spawn('anki')),
            Key([], 'm', lazy.spawn('maps.sh')),
            Key([], 'v', lazy.spawn('ankiv.sh')),
        ], name=keychord_name(icon="󰑴", size="16000", rise="4000")),
        KeyChord([], 'p', [
            Key([], 'l', lazy.spawn('pymor -t 20 -f 3')),
            Key([], 's', lazy.spawn('pymor -t 20')),
            Key([], 'c', lazy.spawn('pymor -c')),
        ], name=keychord_name(icon="󰁫", size="17000", rise="2500")),
    ], name=keychord_name(icon="", size="13000", rise="3000")),

    KeyChord([MOD], 's', [
        Key([], 'u', lazy.group['scratchpad'].dropdown_toggle('term')),
        Key([], 'i', lazy.group['scratchpad'].dropdown_toggle('ai')),
        # Key([], 's', lazy.group['scratchpad'].dropdown_toggle('trayer')),
        Key([], 'w', lazy.group['scratchpad'].dropdown_toggle('zap')),
        Key([], 'c', lazy.group['scratchpad'].dropdown_toggle('cmus')),
        Key([], 'l', lazy.group['scratchpad'].dropdown_toggle('lowfi')),
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
            Key([], 'm', lazy.group['scratchpad'].dropdown_toggle('ankivMATH')),
        ], name=keychord_name(icon="󰑴", size="16000", rise="4000")),
        Key([], 'g', lazy.group['scratchpad'].dropdown_toggle('calc')),
    ], name=keychord_name(icon="󰊠", size="15000", rise="3600")),
    KeyChord([MOD], 'm', [
        Key([], 'l', lazy.next_screen()),
        Key([], 'h', lazy.prev_screen()),
    ], name=keychord_name(icon="󰊠", size="15000", rise="3600")),
    KeyChord([MOD], 'w', [
        Key([], 't', lazy.function(go_to_group(groups[0].name))),
        Key([], 'i', lazy.function(go_to_group(groups[1].name))),
        Key([], 'r', lazy.function(go_to_group(groups[2].name))),
        Key([], 'v', lazy.function(go_to_group(groups[3].name))),
        Key([], 'b', lazy.function(go_to_group(groups[4].name))),
        Key([], 'l', lazy.function(go_to_group(groups[5].name))),
        Key([], 's', lazy.function(go_to_group(groups[6].name))),
        Key([], 'g', lazy.function(go_to_group(groups[7].name))), ],
        name=keychord_name(icon="", size="13000", rise="3000")),

    KeyChord([MOD, 'shift'], 'w', [
        Key([], 't',  lazy.function(go_to_group_and_move_window(groups[0].name))),
        Key([], 'i',  lazy.function(go_to_group_and_move_window(groups[1].name))),
        Key([], 'r',  lazy.function(go_to_group_and_move_window(groups[2].name))),
        Key([], 'v',  lazy.function(go_to_group_and_move_window(groups[3].name))),
        Key([], 'b',  lazy.function(go_to_group_and_move_window(groups[4].name))),
        Key([], 'l',  lazy.function(go_to_group_and_move_window(groups[5].name))),
        Key([], 's',  lazy.function(go_to_group_and_move_window(groups[6].name))),
        Key([], 'g',  lazy.function(go_to_group_and_move_window(groups[7].name))),
    ], name=keychord_name(icon="", size="14000", rise="2000")),

    KeyChord([MOD], 'a', [
        Key([], 'k', lazy.window.kill()),
        Key([], 'b', lazy.hide_show_bar()),
        KeyChord([], "r", [
            Key([], 'i', lazy.layout.grow()),
            Key([], 'd', lazy.layout.shrink()),
            Key([], 'n', lazy.layout.normalize()),
            Key([], 'm', lazy.layout.maximize()),
            Key([], 'r', lazy.layout.reset()),
        ], mode=True, name=keychord_name(icon="", size="14000", rise="4000")),
        KeyChord([], 'l', [
            Key([], 'k', lazy.layout.shuffle_down()),
            Key([], 'j', lazy.layout.shuffle_up()),
            Key([], 's', lazy.layout.swap_main()),
            Key([], 'b', lazy.group.focus_back()),
            Key([], 'space', lazy.layout.flip()),
        ], name=keychord_name(icon="", size="13000", rise="4000")),
        KeyChord([], 'q', [
            Key([], 'r', lazy.reload_config()),
            Key([], 'e', lazy.shutdown()),
            Key([], 'i', lazy.spawn('getwindow.sh')),
        ], name=keychord_name(icon="", size="14000", rise="4000")),
        KeyChord([], 'e', [
            Key([], 'l', lazy.spawn('easyeffects -l LoudnessEqualizer')),
            Key([], 'b', lazy.spawn('easyeffects -l "HeavyBass"')),
        ], name=keychord_name(icon="", size="13000", rise="4000")),
    ], name=keychord_name(icon="", size="13000", rise="3500")),

    KeyChord([MOD], "v", [
        Key([], 'j', lazy.spawn('changevolume.sh - 5')),
        Key([], 'k', lazy.spawn('changevolume.sh 5')),
        Key([], 'm', lazy.spawn('changevolume.sh m')),
    ], name=keychord_name(icon="󰕾", size="15000", rise="4000")),
]

for keychord in keychords:
    keys.append(keychord)
