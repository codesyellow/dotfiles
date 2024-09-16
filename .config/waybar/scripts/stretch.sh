#!/bin/bash
if [[ -f "/tmp/stretch" ]]; then
  if [[ -f "/tmp/stretch_start" ]]; then
    output=" $nm|$wn  GET READY!"
  fi
  if [[ -f "/tmp/stop" ]]; then
    state="critical"
    output=" STOP!"
  else
    state="warning"
    output=" DO IT!!"
  fi 
else
  output=""
fi

echo "{\"text\": \"$output\", \"tooltip\": \"DS4 Battery Status\", \"class\": \"$state\"}"
