#!/bin/bash
if [[ -f "/tmp/stretch" ]]; then
  if [[ -f "/tmp/stretch_start" ]]; then
    output=" GET READY!<span size='15000' foreground='#4c566a'> | </span>"
  fi
  if [[ -f "/tmp/stop" ]]; then
    output=" STOP!<span size='15000' foreground='#4c566a'> | </span>"
  else
    state="warning"
    output=" DO IT!!<span size='15000' foreground='#4c566a'> | </span>"
  fi
else
  output=""
fi

echo "{\"text\": \"$output\", \"tooltip\": \"DS4 Battery Status\", \"class\": \"$state\"}"
