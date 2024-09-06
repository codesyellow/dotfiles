#!/bin/bash

game_list="$HOME/.config/game_list"
if [[ ! -f "$game_list" ]]; then
  touch $game_list
fi

game=$(xprop -id $(xdotool getwindowfocus) | grep "WM_CLASS(STRING)" | awk -F '"' '{print $4}')
is_match=false

if [ ! -f "$game_list" ]; then
  echo "game_list not found: $file"
  exit 1
fi

while IFS= read -r line; do
  if [ "$line" == "$game" ]; then
    echo "$line"
    is_match=true
  fi
done <"$game_list"

if [[ $is_match == 'true' ]]; then
  echo "Name already exist, so it won't be added to the list."
else
  echo "Name $game wasn't in the list, so it wll be added to the list."
  echo "$game" >>"$game_list"
fi
