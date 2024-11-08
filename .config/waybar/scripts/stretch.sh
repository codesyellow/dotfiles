#!/bin/bash
if [[ -f "/tmp/stretch" ]]; then
  if [[ -f "/tmp/stretch_start" ]]; then
    output="<span size='15000' foreground='#4c566a'> | </span> GET READY!"
  fi
  if [[ -f "/tmp/stop" ]]; then
    output="<span size='15000' foreground='#4c566a'> | </span> STOP!"
  else
    state="warning"
    output="<span size='15000' foreground='#4c566a'> | </span> DO IT!!"
  fi
else
  output=""
fi

echo "{\"text\": \"$output\", \"tooltip\": \"stretch\", \"class\": \"$state\"}"
