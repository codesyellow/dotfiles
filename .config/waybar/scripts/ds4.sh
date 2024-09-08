#!/bin/bash

controller=""
ds4=$(dsbattery)

if [[ -n "$ds4" ]]; then
  if ! [[ -f "/tmp/ds4_active" ]]; then
    touch "/tmp/ds4_active"
  fi

  if [[ "$ds4" == *"↑"* ]]; then
    if ! [[ -f "/tmp/ds4_charging" ]]; then
      touch "/tmp/ds4_charging"
    fi
    state="charging"
    output="$controller "
  else
    if [[ -f "/tmp/ds4_charging" ]]; then
      rm "/tmp/ds4_charging"
    fi
    ds4_bat=$(echo "$ds4" | grep -o '[0-9]*')
    if [[ $ds4_bat -ge 51 && $ds4_bat -le 70 ]]; then
      state="normal"
      output="$controller "
    elif [[ $ds4_bat -le 50 && $ds4_bat -ge 30 ]]; then
      state="warning"
      output=" $controller "
    elif [[ $ds4_bat -le 29 ]]; then
      state="alert"
      output="$controller "
    else
      state="normal"
      output="$controller "
    fi
  fi
else
  if [[ -f "/tmp/ds4_active" ]]; then
    rm "/tmp/ds4_active"
  fi
  state="normal"
  output="$controller "
fi

echo "{\"text\": \"$output\", \"tooltip\": \"DS4 Battery Status\", \"class\": \"$state\"}"
