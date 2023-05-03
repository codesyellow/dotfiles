from libqtile import bar, hook

@hook.subscribe.client_focus
def opacity(c):
    for x in c.qtile.current_group.windows:
        set_opacity = x.set_opacity
        wm_class = x.get_wm_class()[1]
        if (wm_class == 'firefox' 
            or wm_class == 'org.qutebrowser.qutebrowser'
            or wm_class == 'qutebrowser'):
            set_opacity(1) 
        if x.has_focus and x.name == 'scratchpad' or x.name == 'chatgpt':
            for w in x.group.windows:
                w.set_opacity(1)
        elif not x.has_focus:
            set_opacity(0.5)
        else:
            set_opacity(1) 

@hook.subscribe.client_focus
def is_floating(c):
    for x in c.qtile.current_group.windows:
        if x.has_focus and x.floating and x.name != 'scratchpad' and not x.fullscreen:
            if x.get_wm_class()[0] == 'Navigator':
                x.set_size_floating(500,680)
            x.center()

