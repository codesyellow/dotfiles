import os
import subprocess
from libqtile import hook, qtile

if qtile.core.name == "wayland":

    @hook.subscribe.startup_once
    def autostart():
        home = os.path.expanduser("~/.config/qtile/wl_autostart.sh")
        subprocess.Popen([home])

else:

    @hook.subscribe.startup_once
    def autostart():
        home = os.path.expanduser("~/.config/qtile/autostart.sh")
        subprocess.Popen([home])
