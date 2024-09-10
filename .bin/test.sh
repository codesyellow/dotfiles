#!/bin/bash

active_counter=0
inactive_counter=60
break_counter=20
no_activity=false
no_activity_rounds=0

notify() {
  notify-send -i ~/.local/share/icons/eye_${1}.png "$2"
}

while true; do
  idle_time=$(xprintidle)
  if [[ "$idle_time" -le 1000 ]]; then
    if [[ "$inactive_counter" != 60 ]]; then
      inactive_counter=60
    fi
    if [[ "$active_counter" == 300 ]]; then
      notify "break" "breaking time"
      sleep $break_counter
      active_counter=0
      notify "good" "Break ended!"
    fi
    ((active_counter++))

    if [[ "$no_activity" == true ]]; then
      no_activity=false
      echo "actitivy was detected, so inactive counter will start again"
    fi
    if [[ "$no_activity_rounds" != 0 ]]; then
      no_activity_rounds=0
    fi
  else
    if [[ "$no_activity" == "false" ]]; then
      ((inactive_counter--))
      if [[ "$inactive_counter" -le 0 ]]; then
        inactive_counter=60
        active_counter=0
        ((no_activity_rounds++))
        echo "$no_activity_rounds"
        echo "$no_activity"
        if [[ "$no_activity_rounds" -ge 2 ]]; then
          no_activity=true
          echo "stopping inactivity counter until activity is detected"
        fi
      fi
    fi
  fi
  sleep 1
done

