from libqtile import hook, qtile
from libqtile.log_utils import logger
import re

if qtile.core.name == "wayland":
    # create a function to close winedbg.exe/Program Error
    @hook.subscribe.client_managed
    def gamesFullscreen(c):
        for x in c.qtile.current_group.windows:
            if re.search("^steam_app.", x.get_wm_class()[0]) and not x.name == 'Amazon Games':
                x.cmd_enable_fullscreen()

@hook.subscribe.client_focus
def opacity(c):
    for x in c.qtile.current_group.windows:
        wm_class = x.get_wm_class()[0]
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
            if x.get_wm_class()[0] == 'Navigator' or x.get_wm_class()[0] == 'Brave-browser':
                x.cmd_set_size_floating(500,680)
            x.cmd_center()

