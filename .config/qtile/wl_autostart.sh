#!/bin/bash
wlsunset -t 4000 -g 1.1 &
light-keys.sh &
swaybg -i ~/.wallpapers/house.jpg &
dunst &
flatpak run com.github.wwmm.easyeffects --gapplication-service &
wl-copy &
/usr/lib/polkit-kde-authentication-agent-1 &
wl-paste --watch cliphist store &
swayidle -w \
    timeout 300 'swaylock -i ~/.wallpapers/house.jpg' \
    before-sleep 'swaylock -i ~/.wallpapers/house.jpg' &
sway-audio-idle-inhibit &
swayosd-server &
blueman-applet &
flatpak run com.github.wwmm.easyeffects -l 'LoudnessEqualizer' &
recharge_ps4.sh &
