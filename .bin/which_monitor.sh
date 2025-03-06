#!/usr/bin/env bash

mkfifo /tmp/wobpipe 2>/dev/null
pkill wob
tail -f /tmp/wobpipe | wob -c ~/.config/wob/moniwob.ini &
sleep 0.1
echo 1 >/tmp/wobpipe
