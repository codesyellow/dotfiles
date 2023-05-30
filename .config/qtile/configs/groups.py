from libqtile.config import Group, Key, ScratchPad
from .variables import icons, mod 
from .functions import has_class, has_name
from .bindings import keys
from .scratchpad import scratchpads
from libqtile.lazy import lazy

groups = [
    Group(icons[0], layout='max', matches=[has_class(['navigator', 'firefox', 'Brave-browser', 'qutebrowser', 'org.qutebrowser.qutebrowser'])]),
    Group(icons[1], layout='monadwide', matches=[has_class(['Emacs'])]),
    Group(icons[2], layout='treetab', matches=[has_class(['mpv', 'Microsoft-edge'])]), 
    Group(icons[3], layout='treetab', matches=[has_class(['zathura'])]), 
    Group(icons[4], layout='treetab', matches=[has_class(['audacious'])]),
    Group(icons[5], layout='monadwide', matches=[has_class(['Alacritty', 'foot'])]),
    Group(icons[6], layout='treetab', matches=[has_class(['heroic', 'Steam', 'amazon games ui.exe', 'bottles', 'ProtonUp-Qt', 'lutris', 'amazongamessetup.exe']), 
                                            has_name(['Steam - Self Updater', 
                                                         'Steam setup', 'Steam', 'Sign in to Steam'] )]),
    ScratchPad('scratchpad', scratchpads),
]

for k, group in zip(['1', '2', '3', '4', '5', 'q', 'g'], groups):
    keys.append(Key([mod], k, lazy.group[group.name].toscreen()))
    keys.append(Key([mod, 'shift'], k, lazy.window.togroup(group.name)))


