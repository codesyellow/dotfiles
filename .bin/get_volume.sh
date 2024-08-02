#!/usr/bin/env bash

while true; do
  is_muted=$(pamixer --get-mute)
  volume=$(pamixer --get-volume)

  if [[ $is_muted == 'true' ]]; then
    echo  >/tmp/volume_status
  fi

  if [[ $volume -ge 45 ]]; then
    echo  >/tmp/volume_status
  elif [[ $volume -le 44 ]] && [[ $volume -ge 1 ]]; then
    echo  >/tmp/volume_status
  else
    echo  >/tmp/volume_status
  fi
  sleep 10
done
