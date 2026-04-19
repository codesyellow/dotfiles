#!/usr/bin/env bash

dbus-update-activation-environment --systemd DISPLAY XAUTHORITY &
caffeine &
hsetroot -fill ~/.wallpapers/skyrim.jpg &
sxhkd &
picom &
unclutter &
$HOME/.bin/dwm-bar.sh &
$HOME/.bin/dwm-layout-fix.sh &
