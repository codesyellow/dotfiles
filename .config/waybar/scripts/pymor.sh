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
    state="normal"
    output="$pymor_icon_half $pomodoro_number"
  else
    state="normal"
    output="$pymor_icon $pomodoro_number"
  fi

  if [[ "$pomodoro_number" -le 5 ]]; then
    state="warning"
    output="$pymor_icon_empty $pomodoro_number"
  fi
else
  state="normal"
  output=""
  if [[ -f "/tmp/pomo_half" ]]; then
    rm "/tmp/pomo_half"
  fi
fi

echo "{\"text\": \"$output\", \"tooltip\": \"Pomodoro Timer\", \"class\": \"$state\"}"
