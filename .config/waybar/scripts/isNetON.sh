#!/bin/bash
wired_icon=
isConnected=$(nm-online | grep 'online')

if [[ -n "$isConnected" ]]; then
  output="<span size='15000' foreground='#4c566a'> | </span><span rise='1500'>$wired_icon</span>"
else
  state="warning"
  output="<span size='15000' foreground='#4c566a'> | </span>$wired_icon"
fi

echo "{\"text\": \"$output\", \"tooltip\": \"Pomodoro Timer\", \"class\": \"$state\"}"
