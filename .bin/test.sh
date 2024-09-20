#!/bin/sh
window_name=''

while true; do
  current_window_class=$(xprop -id $(xdotool getwindowfocus) | grep "WM_CLASS(STRING)" | awk -F '"' '{print $4}')
  if [[ "$window_name" != "$current_window_class" ]]; then
    window_name=$current_window_class
    current_workspace=$(xprop -root _NET_CURRENT_DESKTOP | awk '/_NET_CURRENT_DESKTOP/ {print $3}')
    echo "$current_window_class"
  fi

  sleep 2
done
