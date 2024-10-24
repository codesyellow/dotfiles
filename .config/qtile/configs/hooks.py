import os, subprocess
from libqtile import hook, qtile
from libqtile.log_utils import logger

if qtile.core.name == "wayland":
    @hook.subscribe.startup_once
    def autostart():
        home = os.path.expanduser('~/.config/qtile/wl_autostart.sh')
        subprocess.Popen([home])
else:
    @hook.subscribe.startup_once
    def autostart():
        home = os.path.expanduser('~/.config/qtile/autostart.sh')
        subprocess.Popen([home])

@hook.subscribe.client_focus
def opacity(c):
    for x in c.qtile.current_group.windows:
        wm_class = x.get_wm_class()[0]
        if (wm_class == 'firefox'
            or wm_class == 'org.qutebrowser.qutebrowser'
            or wm_class == 'qutebrowser'
            or wm_class == 'Brave-browser'):
            x.set_opacity(1)
        if x.has_focus and x.name == 'scratchpad' or x.name == 'pulsemixer':
            for w in x.group.windows:
                w.opacity = 1
        elif not x.has_focus:
            x.set_opacity(0.5)
        else:
            x.opacity = 1

@hook.subscribe.client_new
def new_client(client):
    if client.get_wm_class()[0] == "xdg-desktop-portal-lxqt":
        client.set_size_floating(800,500)

@hook.subscribe.client_killed
def client_killed(client):
  try:
    subprocess.run(["canberra-gtk-play", "-f", "/usr/share/sounds/Smooth/stereo/window-close.oga"])
  except FileNotFoundError:
    logger.warning(f"Error: Sound file not found")
  except subprocess.CalledProcessError as e:
    logger.warning(f"Error playing sound: {e}")

@hook.subscribe.client_managed
def client_managed(client):
  try:
    subprocess.run(["canberra-gtk-play", "-f", "/usr/share/sounds/Smooth/stereo/window-new.oga"])
  except FileNotFoundError:
    logger.warning(f"Error: Sound file not found")
  except subprocess.CalledProcessError as e:
    logger.warning(f"Error playing sound: {e}")
