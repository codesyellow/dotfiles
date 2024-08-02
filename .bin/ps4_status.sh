#!/bin/bash

# dsbat string
dsbat=$(dsbattery)
icon=''

if [[ $1 == "icon" ]]; then
  echo "$icon"
  exit 0
fi

if [[ $1 == "perc" ]]; then
  perc=$(echo "$dsbat" | grep -oE '[0-9]+%' | sed 's/%//')
  echo "$perc%"
else
  echo "Usage: $0 [icon|perc]"
fi
