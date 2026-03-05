#!/usr/bin/env bash

while true; do
  focused_win=$(niri msg focused-window)
  focused_win_lines=$(wc -l <<< "$focused_win")
  is_floating=$(awk '/Is floating:/ {print $3}' <<< "$focused_win")
  is_which_key_open=$(pgrep -x wlr-which-key)
  eww_windows=$(eww active-windows)

  clock_is_open=$(grep -q "clock_bg" <<< "$eww_windows" && echo yes)

  # should hide widget
  if [[ $focused_win_lines -eq 1 && -z "$is_which_key_open" && -n "$clock_is_open" ]]; then
    eww close clock_bg
    echo "clock_bg was closed"
  fi

  # should show widget
  if [[ $focused_win_lines -gt 1 && "$is_floating" != "yes" && -z "$is_which_key_open" && -z "$clock_is_open" ]]; then
    eww open clock_bg
    echo "clock_bg was opened"
  fi

  sleep 2
done
