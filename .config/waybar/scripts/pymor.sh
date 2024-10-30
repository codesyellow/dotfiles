#!/bin/bash
pymor_icon=
pymor_icon_half=
pymor_icon_empty=

pomodoro="/tmp/pomodoro_time"
if [[ -f "$pomodoro" ]]; then
  pomodoro_number=$(cat "$pomodoro")
  if [[ ! -f "/tmp/pomo_half" ]]; then
    let pomo_half=pomodoro_number/2
    touch "/tmp/pomo_half"
  fi

  output='<span rise="4650" size="12000" foreground="#EF5A6F">%s</span> <span size="14000" rise="4000" foreground="#EF5A6F">%s</span> <span size="x-large" foreground="#fff">|</span>' 
  output=""$pymor_icon" "$pomodoro_number"<span size='15000' foreground='#4c566a'> | </span>"
  state="warning"
else
  printf ''
  if [[ -f "/tmp/pomo_half" ]]; then
    rm "/tmp/pomo_half"
  fi
fi

echo "{\"text\": \"$output\", \"tooltip\": \"Pomodoro Timer\", \"class\": \"$state\"}"
