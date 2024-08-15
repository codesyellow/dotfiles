#!/usr/bin/env bash

ramdon_notify() {
  messages_file="/home/cie/.config/joyley/$1"
  # Set IFS to handle line endings correctly
  IFS=$'\n'
  # Select a random line from the file
  random_message=$(shuf -n 1 "$messages_file")

  notify-send.sh -i ~/.local/share/icons/joystick.png "Joyley" $random_message
}

temp() {
  if [[ "$1" == "t" ]]; then
    touch "/tmp/$2"
  else
    rm "/tmp/$1"
  fi
}

is_idle() {
  log_file="/tmp/ds4_logger"
  idle_crit=15
  idle_warn=10

  if [[ -f "$log_file" ]]; then
    last_time=$(cat "$log_file")

    last_time_epoch=$(date -d "$last_time" +"%s")
    current_time_epoch=$(date +"%s")
    time_diff=$(((current_time_epoch - last_time_epoch) / 60))

    if ((time_diff >= idle_warn)); then
      if ! [[ -f "/tmp/ds4_idle_warn" ]]; then
        ramdon_notify "joyley_idle_warn"
        touch "/tmp/ds4_idle_warn"
      fi
    else
      if [[ -f "/tmp/ds4_idle_warn" ]]; then
        rm "/tmp/ds4_idle_warn"
      fi
    fi

    if ((time_diff >= idle_crit)); then
      if ! [[ -f "/tmp/ds4_idle_crit" ]]; then
        ramdon_notify "joyley_idle_crit"
        touch "/tmp/ds4_idle_crit"
        rm "/tmp/ds4_idle_warn"
        rm "/tmp/ds4_idle_crit"
        echo "$(cat /tmp/ds4_logger)"
        rm "/tmp/ds4_logger"
        dsbattery -d &
      fi
    else
      if [[ -f "/tmp/ds4_idle_crit" ]]; then
        rm "/tmp/ds4_idle_crit"
      fi
    fi
  else
    echo "Log file not found!"
  fi
}

ds4_bat_warnings_50() {
  if [[ $1 -le 50 ]]; then
    if ! [[ -f "/tmp/fwarning_50" ]]; then
      ramdon_notify "joyley_bat_warn"
      temp "t" "fwarning_50"
    fi
  else
    if [[ -f "/tmp/fwarning_50" ]]; then
      temp "fwarning_50"
    fi
  fi
}

ds4_bat_warnings_30() {
  if [[ $1 -le 30 ]]; then
    if ! [[ -f "/tmp/fwarning_30" ]]; then
      ramdon_notify "joyley_bat_crit"
      temp "t" "fwarning_30"
    fi
  else
    if [[ -f "/tmp/fwarning_30" ]]; then
      temp "fwarning_30"
    fi
  fi
}

ds4_first_connected() {
  if ! [[ -f "/tmp/ds4_first_connect" ]]; then
    ramdon_notify "joyley_wokeup"
    temp "t" "ds4_first_connect"
    echo "$(date +%H:%M:%S)" >>/tmp/ds4_logger
  fi
}

ds4() {
  if [[ -z "$1" ]]; then
    echo "false" >/tmp/ds4_status
    if [[ -f /tmp/ds4_first_connect ]]; then
      temp "ds4_first_connect"
    fi
  else
    battery_status=$(dsbattery)
    echo "true" >/tmp/ds4_status
    echo "$1" >/tmp/ds4_battery
    if [[ "$battery_status" == *"↑"* ]]; then
      if ! [[ -f /tmp/ds4_charging ]]; then
        if [[ -f /tmp/ds4_notcharging ]]; then
          temp "ds4_notcharging"
        fi
        temp "t" "ds4_charging"
        ramdon_notify "joyley_juiceon"
      fi
    else
      if [[ -f /tmp/ds4_charging ]]; then
        if ! [[ -f /tmp/ds4_notcharging ]]; then
          ramdon_notify "joyley_juiceoff"
          temp "ds4_charging"
        fi
        temp "t" "ds4_notcharging"
      fi
    fi
    ds4_first_connected
    if [[ -z $idle ]]; then
      echo oi
      nohup idle_joy.py &
    fi
    ds4_bat_warnings_50 $1
    ds4_bat_warnings_30 $1
  fi
}

while true; do
  idle=$(pgrep -fl 'idle_joy.py')
  ds=$(dsbattery)
  bat=$(echo "$ds" | grep -o '[0-9]*')
  ds4 $bat $idle
  is_idle
  sleep 2
done
