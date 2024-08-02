#!/usr/bin/env bash
touch /tmp/on_off
echo '0' >/tmp/on_off
badwater_icon=''
dustbowl_icon=''

while true; do
  on_off=$(cat /tmp/on_off)
  map_dustbowl=$(cat /tmp/tf2_dustbowl_count)
  map_badwater=$(cat /tmp/tf2_badwater_count)
  dustbowl_status=$(cat /tmp/dustbowl_status)
  badwater_status=$(cat /tmp/badwater_status)

  if [[ $dustbowl_status == 'false' ]] && [[ $badwater_status == 'false' ]]; then
    echo 'false' >/tmp/server_status
    echo 'yep'
  fi

  if [[ $dustbowl_status == 'true' ]] && [[ $on_off == 0 ]]; then
    echo $map_dustbowl >"/tmp/map_display"
    echo $dustbowl_icon >"/tmp/map_display-icon"
    echo $dustbowl_icon 'dust'
    echo 'true' >/tmp/server_status
    echo '1' >/tmp/on_off
  elif [[ $on_off == 0 ]]; then
    echo '1' >/tmp/on_off
  fi
  if [[ $badwater_status == 'true' ]] && [[ $on_off == 1 ]]; then
    echo $badwater_icon 'bad'
    echo $map_badwater >"/tmp/map_display"
    echo $badwater_icon >"/tmp/map_display-icon"
    echo 'true' >/tmp/server_status
    echo '0' >/tmp/on_off
  elif [[ $on_off == 1 ]]; then
    echo '0' >/tmp/on_off
  fi

  sleep 60
done
