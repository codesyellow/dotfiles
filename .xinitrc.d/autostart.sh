#!/bin/sh
picom &
xrandr --output VGA-1 --gamma 1.0:0.88:0.50 --brightness 0.95 &
hsetroot -cover ~/.wallpapers/house.jpg &
flatpak run com.github.wwmm.easyeffects --gapplication-service &
dunst &
unclutter &
run_xidlehook &
picom --experimental-backends &
flatpak run com.github.wwmm.easyeffects -l 'LoudnessEqualizer' &
dbus-update-activation-environment --systemd DBUS_SESSION_BUS_ADDRESS DISPLAY XAUTHORITY &
udiskie &
recharge_ps4.sh &
