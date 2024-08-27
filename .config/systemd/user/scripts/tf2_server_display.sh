#!/usr/bin/env bash

badwater_icon=''
dustbowl_icon=''

if [[ -f "/tmp/dustbowl_count" ]]; then
  dustbowl=$(</tmp/dustbowl_count)
  echo "$dustbowl_icon $dustbowl" >"/tmp/map_display"
  echo "displaying dustbowl count"
fi

if [[ -f "/tmp/badwater_count" ]]; then
  badwater=$(</tmp/badwater_count)
  echo "$badwater_icon $badwater" >"/tmp/map_display"
  echo "displaying badwater count"
fi
