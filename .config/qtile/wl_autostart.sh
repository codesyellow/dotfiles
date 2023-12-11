#!/bin/bash
wlsunset -T 4000 -g 1.1 &
swww init &
paplay ~/.audios/retro-audio-logo-94648.mp3 &
dunst &
flatpak run com.github.wwmm.easyeffects --gapplication-service &
wl-copy &
/usr/lib/polkit-kde-authentication-agent-1 &
wl-paste --watch cliphist store &
blueman-applet &
recharge_ps4.sh &
/usr/lib/xdg-desktop-portal-wlr &
flatpak run com.github.wwmm.easyeffects -l 'LoudnessEqualizer' &
