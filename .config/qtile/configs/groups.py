from libqtile.config import Group, ScratchPad
from .variables import icons
from .functions import has_class, has_name
from .scratchpads import scratchpads

groups = [
        Group(icons[0], layout='max', matches=[has_class(['navigator', 'firefox', 'Brave-browser', 'qutebrowser', 'org.qutebrowser.qutebrowser', 'floorp'])]),
        Group(icons[1], layout='max', matches=[has_class(['audacious'])]), 
        Group(icons[2], layout='max', matches=[has_class(['Alacritty', 'st', ])]),
        Group(icons[3], layout='max', matches=[has_class(['heroic', 'Steam', 'amazon games ui.exe', 'bottles', 'ProtonUp-Qt', 'lutris', 'amazongamessetup.exe', 'net.davidotek.pupgui2']),
                                               has_name(['Steam - Self Updater', 
                                                             'Special Offers',
                                                             'Steam setup', 'Steam', 'Sign in to Steam'] )]),
        Group(icons[4], layout='max', matches=[has_class(['Youtube Music', 'youtube music'])]),
        Group(icons[5], layout='max', matches=[has_class(['zathura', 'mpv', 'Microsoft-edge', 'anki'])]),
                                                   ScratchPad('scratchpad', scratchpads),
                                                   ]


