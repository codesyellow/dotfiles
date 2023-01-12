#!/bin/sh
mkfifo /tmp/wobpipe && tail -f /tmp/wobpipe | wob &
easyeffects --gapplication-service &
wlsunset -t 4000 &
swaybg -i ~/.wallpapers/mountains.jpg &
dunst &
