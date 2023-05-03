from libqtile.config import Group, ScratchPad, Key, DropDown
from .variables import icons, mod
from .functions import has_class, has_name
from .bindings import keys
from libqtile.lazy import lazy

groups = [
    Group(icons[0], layout="max", matches=[has_class(['navigator', 'firefox', 'Brave-browser', 'qutebrowser', 'org.qutebrowser.qutebrowser'])]),
    Group(icons[1], layout="monadwide", matches=[has_class(['Emacs'])]),
    Group(icons[2], layout="treetab", matches=[has_class(['mpv'])]), 
    Group(icons[3], layout="treetab", matches=[has_class(['zathura'])]), 
    Group(icons[4], layout="treetab", matches=[has_class(["audacious"])]),
    Group(icons[5], layout="monadwide", matches=[has_class(["Alacritty"])]),
    Group(icons[6], layout="treetab", matches=[has_class(["heroic", "Steam", 'amazon games ui.exe', 'bottles', 'ProtonUp-Qt', 'lutris']), 
                                            has_name(['Steam - Self Updater', 
                                                         'Steam setup', 'Steam', 'Sign in to Steam'] )]),
    ScratchPad("scratchpad", [
        # add a alternative config file for transparency to work properly on wayland
        DropDown("term", "alacritty --config-file /home/codesyellow/.config/alacritty/alacritty2.yml -t scratchpad", y=0.6),
        DropDown("gpterm", "alacritty --title chatgpt -e tgpt chat", height=0.9, width=0.5, opacity=0.9, x=0.25),
        ]
    ),
]

for k, group in zip(["1", "2", "3", "4", "5", "q", "g"], groups):
    keys.append(Key([mod], k, lazy.group[group.name].toscreen()))
    keys.append(Key([mod, 'shift'], k, lazy.window.togroup(group.name)))


