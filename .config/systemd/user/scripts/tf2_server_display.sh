#!/usr/bin/env bash

current_hour=$(date +%H)
if [[ $current_hour -lt 6 || $current_hour -ge 22 ]]; then
  systemctl --user stop tf2_server_display.timer
  exit 0
fi

badwater_icon=''
dustbowl_icon=''
turbine_icon=''
displayed="/tmp/did_showed"
dustbowl_path="/tmp/dustbowl_count"
badwater_path="/tmp/badwater_count"
turbine_path="/tmp/turbine_count"

# Ensure the displayed file exists
if [[ ! -f "$displayed" ]]; then
  touch "$displayed"
  echo "badwater" >"$displayed"
fi

did_showed=$(cat "$displayed")

to_display() {
  map_count=$(cat "/tmp/${1}_count")
  echo "$2 $map_count" >"/tmp/map_display"
  echo "displaying $1 count"
  echo "$1" >"$displayed"
}

# Determine which maps are active
dustbowl_active=false
badwater_active=false
turbine_active=false

if [[ -f "$dustbowl_path" ]]; then
  dustbowl_active=true
fi

if [[ -f "$badwater_path" ]]; then
  badwater_active=true
fi

if [[ -f "$turbine_path" ]]; then
  turbine_active=true
fi

# Logic to alternate or display based on active maps
if $dustbowl_active && $badwater_active && $turbine_active; then
  if [[ "$did_showed" == "badwater" ]]; then
    to_display "dustbowl" "$dustbowl_icon"
  elif [[ "$did_showed" == "dustbowl" ]]; then
    to_display "turbine" "$turbine_icon"
  else
    to_display "badwater" "$badwater_icon"
  fi
elif $dustbowl_active && $badwater_active; then
  if [[ "$did_showed" == "badwater" ]]; then
    to_display "dustbowl" "$dustbowl_icon"
  else
    to_display "badwater" "$badwater_icon"
  fi
elif $dustbowl_active && $turbine_active; then
  if [[ "$did_showed" == "dustbowl" ]]; then
    to_display "turbine" "$turbine_icon"
  else
    to_display "dustbowl" "$dustbowl_icon"
  fi
elif $badwater_active && $turbine_active; then
  if [[ "$did_showed" == "badwater" ]]; then
    to_display "turbine" "$turbine_icon"
  else
    to_display "badwater" "$badwater_icon"
  fi
elif $dustbowl_active; then
  to_display "dustbowl" "$dustbowl_icon"
elif $turbine_active; then
  to_display "turbine" "$turbine_icon"
elif $badwater_active; then
  to_display "badwater" "$badwater_icon"
else
  echo "All the servers are empty!"
fi
