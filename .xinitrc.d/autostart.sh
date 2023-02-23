#!/bin/sh
easyeffects --gapplication-service &
xrandr --output VGA-1 --gamma 1.0:0.88:0.50 --brightness 0.95 &
hsetroot -cover ~/.wallpapers/house.jpg &
xset led on &
keyd-application-mapper -d
dunst &
unclutter &
run_xidlehook &
safeeyes &
picom --experimental-backend &
nm-applet &
cpupower frequency-set -g performance &
run_xidlehook &
easyeffects -l 'LoudnessEqualizer' &
alsactl --file ~/.config/asound.state restore &
# this is for fixing firefox slow startup
dbus-update-activation-environment --systemd DBUS_SESSION_BUS_ADDRESS DISPLAY XAUTHORITY &
emulate_xbox.sh &
alacritty &
