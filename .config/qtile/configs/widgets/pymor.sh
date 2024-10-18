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

  if [[ "$pomodoro_number" -le "$pomo_half" ]] && [[ "$pomodoro_number" -ge 6 ]]; then
    output="$pymor_icon_half $pomodoro_number"
    printf '<span foreground="#36C2CE">%s</span>' "$output"
  else
    output="$pymor_icon $pomodoro_number"
    printf '<span foreground="#36C2CE">%s</span>' "$output"
  fi

  if [[ "$pomodoro_number" -le 5 ]]; then
    output="$pymor_icon_empty $pomodoro_number"
    printf '<span foreground="#EF5A6F">%s</span>' "$output"
  fi
else
  if [[ -f "/tmp/pomo_half" ]]; then
    rm "/tmp/pomo_half"
  fi
fi
