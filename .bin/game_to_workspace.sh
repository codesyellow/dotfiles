#!/bin/bash

no_launchers="/tmp/gtw_no_launcher"
did_move=false

while true; do
  steam=$(pidof 'steam')
  lutris=$(pidof 'lutris')
  heroic=$(pidof 'heroic')

  if [[ -n "$steam" ]] || [[ -n "$lutris" ]] || [[ -n "$heroic" ]]; then
    game_list=$(cat /home/cie/.config/game_list)
    if [[ -f "$no_launchers" ]]; then
      echo "remove no launcher file"
      rm "$no_launchers"
    fi

    current_window_class=$(xprop -id $(xdotool getwindowfocus) | grep "WM_CLASS(STRING)" | awk -F '"' '{print $4}')
    current_workspace=$(xprop -root _NET_CURRENT_DESKTOP | awk '/_NET_CURRENT_DESKTOP/ {print $3}')

    if [[ "$game_list" == *"$current_window_class"* ]] && [[ ! "$current_workspace" == "4" ]]; then
      if [[ "$did_move" == false ]]; then  
        echo "$(date)"
        echo "$current_window_class"
        xdotool key --clearmodifiers Super+Shift+w g
        did_move=true
      fi
    else
      did_move=false
    fi
  else
    if [[ ! -f "$no_launchers" ]]; then
      echo "No gaming launcher is running."
      touch "$no_launchers"
    fi
    did_move=false
  fi

  sleep 3
done
