import os, subprocess
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


@hook.subscribe.client_new
def new_client(client):
    if client.get_wm_class()[0] == "xdg-desktop-portal-lxqt":
        client.set_size_floating(800, 500)
