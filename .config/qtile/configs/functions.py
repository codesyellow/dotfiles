from libqtile.config import Match

def desconnect_ds4():  
    qtile.cmd_spawn('dsbattery -d')

def latest_group(qtile):
    qtile.current_screen.set_group(qtile.current_screen.previous_group)

def focus_main(qtile):
    window = qtile.current_group.layout.focus_first()
    qtile.current_group.focus(window)

def has_class(c):
    return Match(wm_class=c)

def has_name(c):
    return Match(title=c)

