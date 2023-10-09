#!/bin/bash
light-keys.sh &
swaybg -i ~/.wallpapers/house.jpg &
dunst &
easyeffects --gapplication-service &
wl-copy &
/usr/lib/polkit-kde-authentication-agent-1 &
wl-paste --watch cliphist store &
swayidle -w \
    timeout 300 'swaylock -i ~/.wallpapers/house.jpg' \
    before-sleep 'swaylock -i ~/.wallpapers/house.jpg' &
sway-audio-idle-inhibit &
swayosd-server &
paplay ~/.audios/retro-audio-logo-94648.mp3 &
blueman-applet &
easyeffects -l 'LoudnessEqualizer' &
recharge_ps4.sh &
