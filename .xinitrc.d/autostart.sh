#!/bin/sh
xrandr --output VGA-1 --gamma 1.0:0.88:0.50 --brightness 0.95 &
hsetroot -cover ~/.wallpapers/forest_stairs.jpg &
xset led on &
keyd-application-mapper -d
dunst &
unclutter &
run_xidlehook &
safeeyes &
picom --animations --focus-exclude "! name~=''" &
nm-applet &
cpupower frequency-set -g performance &
run_xidlehook &
easyeffects -l 'LoudnessEqualizer' &
dbus-update-activation-environment --systemd DBUS_SESSION_BUS_ADDRESS DISPLAY XAUTHORITY &
alsactl --file ~/.config/asound.state restore &
emulate_xbox.sh &
