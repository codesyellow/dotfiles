#!/bin/bash
way-displays > /tmp/way-displays.${XDG_VTNR}.${USER}.log 2>&1 &
swww-daemon &
paplay ~/.audios/retro-audio-logo-94648.mp3 &
swayosd-server &
wlsunset -t 4000 &
dunst &
wl-copy &
/usr/lib/polkit-kde-authentication-agent-1 &
wl-paste --watch cliphist store &
blueman-applet &
recharge_ps4.sh &
/usr/lib/xdg-desktop-portal-wlr &
disable_keyd.sh &
sleep 5 && easyeffects --gapplication-service &
