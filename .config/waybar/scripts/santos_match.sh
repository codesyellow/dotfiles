#!/bin/bash

if [[ -f "/tmp/santosmatch" ]]; then
  if [[ ! -f "/tmp/stop_santos_widget" ]]; then
    santos=$(</tmp/santosmatch)
    output=" $santos<span size='15000' foreground='#4c566a'> | </span>"
    state="warning"
  fi
else
  if [[ -f "/tmp/stop_santos_widget" ]]; then
    rm "/tmp/stop_santos_widget"
  fi
fi

echo "{\"text\": \"$output\", \"tooltip\": \"Pomodoro Timer\", \"class\": \"$state\"}"
