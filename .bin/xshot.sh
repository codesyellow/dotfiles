#!/usr/bin/env bash

PIC_PATH="$HOME/.pictures"

mkdir -p "$PIC_PATH"
DATE="$(date +'%Y%m%d%H%M%S')"

if [[ "$1" == "region" ]]; then
  scrot -s "$PIC_PATH/ps_$DATE.jpg" \
    && dunstify "Region screenshot was taken!"

elif [[ "$1" == "zoom" ]]; then
  TMP="$(mktemp).png"
  scrot -s "$TMP"
  convert "$TMP" -resize 200% -filter Mitchell "$TMP"
  imv -u nearest_neighbour "$TMP"
  rm "$TMP"

elif [[ "$1" == "mon" ]]; then
  sleep 1
  scrot -m "$PIC_PATH/ps_mon_$DATE.jpg" \
    && dunstify "Screenshot of current monitor was taken"

elif [[ "$1" == "edit" ]]; then
  TMP="$(mktemp).png"
  sleep 1
  scrot -s "$TMP"
  gimp "$TMP" &

else
  sleep 1
  scrot "$PIC_PATH/ps_$DATE.png" \
    && dunstify "Full screenshot was taken!"
fi
