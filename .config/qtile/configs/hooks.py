from libqtile import hook
from libqtile.log_utils import logger

@hook.subscribe.client_focus
def opacity(c):
    for x in c.qtile.current_group.windows:
        wm_class = x.get_wm_class()[1]
        if (wm_class == 'firefox' 
            or wm_class == 'org.qutebrowser.qutebrowser'
            or wm_class == 'qutebrowser'):
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
            if x.get_wm_class()[0] == 'Navigator' or x.get_wm_class()[1] == 'Brave-browser':
                x.cmd_set_size_floating(500,680)
            x.cmd_center()

