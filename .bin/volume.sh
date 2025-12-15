#!/bin/bash
function check_dependencies() {
  local ret=0
  for cmd in "$@"; do
    if ! command -v "$cmd" >/dev/null 2>&1; then
      echo "Missing dependency: $cmd."
      ret=1
    fi
  done
  return $ret
}

(check_dependencies "pamixer" "dunst") || exit 1

user_input="$1"

case "$user_input" in 
  up)        
    pamixer -i 5
    ;;          
  down)
    pamixer -d 5
    ;;
  mute)
    pamixer -m
    ;;
  small_up)
    pamixer -i 1
    ;;
  small_down)
    pamixer -d 1
    ;;
  *) 
    pamixer --get-volume
    ;;
esac            

current_volume=$(pamixer --get-volume)
dunstify -r 32 "$current_volume"

