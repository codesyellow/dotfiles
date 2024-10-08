#!/usr/bin/env bash
pausa=$(ps -ef | grep 'bash' | grep 'pausa')
dwm_bar=$(ps -ef | grep 'bash' | grep 'dwm-bar.sh')
easy=$(ps -ef | grep 'bash' | grep 'easy_always.sh')

if [[ -z "$dwm_bar" ]]; then
  dwm-bar.sh &
fi

if [[ -z "$pausa" ]]; then
  pausa -a 300 -i 60 -b 20 &
fi

if [[ -z "$easy" ]]; then
  easy_always.sh
fi

hsetroot -cover ~/.wallpapers/ign-0011.png &
alsactl --file ~/.config/asound.state restore &
paplay ~/.audios/retro-audio-logo-94648.mp3 &
xrandr --output VGA-1 --gamma 1.2:1.2:1.2 &
dunst &
unclutter &
dbus-update-activation-environment --systemd DBUS_SESSION_BUS_ADDRESS DISPLAY XAUTHORITY &
udiskie &
systemctl --user import-environment DISPLAY &
clipmenud &
/usr/lib/polkit-kde-authentication-agent-1 &
redshift -O 4000 &
