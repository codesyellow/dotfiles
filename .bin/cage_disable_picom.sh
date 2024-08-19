#!/usr/bin/env bash

while true; do
  picom=$(pidof picom)
  cage=$(pidof cage)

  if [[ -n "$picom" ]] && [[ -n "$cage" ]]; then
    echo "picom killed"
    killall picom &
  elif ! [[ -n "$picom" ]] && ! [[ -n "$cage" ]]; then
    echo "picom started"
    picom &
  fi

  sleep 4
done
