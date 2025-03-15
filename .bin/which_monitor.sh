#!/usr/bin/env bash

# get the pid by checking for the path to thee ini file
mkfifo /tmp/wobpipe 2>/dev/null
wob_to_kill=$(pgrep -f '/home/digo/.config/wob/moniwob.ini')
kill -9 $wob_to_kill
wob &
tail -f /tmp/wobpipe | wob -c ~/.config/wob/moniwob.ini &
sleep 0.1
echo 1 >/tmp/wobpipe
