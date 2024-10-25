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

  output="$pymor_icon_empty $pomodoro_number"
  printf '<span rise="4500" size="12500" foreground="#EF5A6F">%s</span> <span size="x-large" foreground="#fff">|</span>' "$output"
else
  if [[ -f "/tmp/pomo_half" ]]; then
    rm "/tmp/pomo_half"
  fi
fi
