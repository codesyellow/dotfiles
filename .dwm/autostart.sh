#!/bin/sh
fixrandr.sh &
xgifwallpaper -d 5 -s FILL ~/.wallpapers/coffee_rain.gif &
paplay ~/.audios/retro-audio-logo-94648.mp3 &
picom -b &
xrandr --output VGA-1 --gamma 1.0:0.88:0.50 --brightness 0.95 &
dunst &
unclutter &
run_xidlehook &
recharge_ps4.sh &
/usr/lib/polkit-kde-authentication-agent-1 &
blueman-applet &
dbus-update-activation-environment --systemd DBUS_SESSION_BUS_ADDRESS DISPLAY XAUTHORITY &
udiskie &
recharge_ps4.sh &
sleep 5 && easyeffects --gapplication-service &
