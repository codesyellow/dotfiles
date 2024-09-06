#!/bin/bash

game_list="/home/cie/.config/game_list"
if [[ ! -f "$game_list" ]]; then
  touch $game_list
fi

game=$1
is_match=false
game_to_move=''

while IFS= read -r line; do
  current_window_class=$(xprop -id $(xdotool getwindowfocus) | grep "WM_CLASS(STRING)" | awk -F '"' '{print $4}')
  current_workspace=$(xprop -root _NET_CURRENT_DESKTOP | awk '/_NET_CURRENT_DESKTOP/ {print $3}')

  if [ "$line" == "$current_window_class" ] && [[ ! "$current_workspace" == "4" ]]; then
    is_match=true
    game_to_move=$line
  fi

done <"$game_list"

if [[ $is_match == 'true' ]]; then
  echo "Moved window with class '$game_to_move' to the desired workspace."
  xdotool key --clearmodifiers Super+Shift+w g
  exit 0
else
  echo "Game is already on the right workspace or the game_list is empty"
  exit 0
fi
