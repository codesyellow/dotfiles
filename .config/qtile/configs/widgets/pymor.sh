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

  printf '<span size="x-large" foreground="#4c566a">|</span> <span rise="4650" size="12000" foreground="#EF5A6F">%s</span> <span size="14000" rise="3600" foreground="#EF5A6F">%s</span>' "$pymor_icon" "$pomodoro_number"
else
  printf ''
  if [[ -f "/tmp/pomo_half" ]]; then
    rm "/tmp/pomo_half"
  fi
fi
