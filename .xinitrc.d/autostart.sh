hsetroot -cover ~/.wallpapers/ign-0011.png &
alsactl --file ~/.config/asound.state restore &
xremap ~/.config/xremap/config.yml &
paplay ~/.audios/retro-audio-logo-94648.mp3 &
xrandr --output VGA-1 --gamma 1.0:0.88:0.50 --brightness 0.95 &
dunst &
unclutter &
dbus-update-activation-environment --systemd DBUS_SESSION_BUS_ADDRESS DISPLAY XAUTHORITY &
udiskie &
systemctl --user import-environment DISPLAY &
clipmenud &
/usr/lib/polkit-kde-authentication-agent-1 &
easyeffects --gapplication-service &
dwm-bar_run.sh &
