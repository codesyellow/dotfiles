#!/usr/bin/env bash

ramdon_notify() {
  messages_file="/home/cie/.config/joyley/$1"
  # Set IFS to handle line endings correctly
  IFS=$'\n'
  # Select a random line from the file
  random_message=$(shuf -n 1 "$messages_file")

  notify-send.sh -i ~/.local/share/icons/joystick.png "Joyley" $random_message
}

# Notification for battery level below 50%
ds4_bat_warnings_50() {
  if [[ $1 -le 50 ]]; then
    if ! [[ -f /tmp/fwarning_50 ]]; then
      ramdon_notify "joyley_bat_warn"
      touch /tmp/fwarning_50
    fi
  else
    if [[ -f /tmp/fwarning_50 ]]; then
      rm /tmp/fwarning_50
    fi
  fi
}

# Notification for battery level below 30%
ds4_bat_warnings_30() {
  if [[ $1 -le 30 ]]; then
    if ! [[ -f /tmp/fwarning_30 ]]; then
      ramdon_notify "joyley_bat_crit"
      touch /tmp/fwarning_30
    fi
  else
    if [[ -f /tmp/fwarning_30 ]]; then
      rm /tmp/fwarning_30
    fi
  fi
}

# Notification for the first time the DS4 is connected
ds4_first_connected() {
  if ! [[ -f /tmp/ds4_first_connect ]]; then
    notify-send.sh -i ~/.local/share/icons/joystick.png "Joyley" "Power on! What’s the plan?"
    touch /tmp/ds4_first_connect
  fi
}

# Main function to check battery level and handle notifications
ds4() {
  if [[ -z "$1" ]]; then
    echo "false" >/tmp/ds4_status
    rm /tmp/ds4_first_connect
  else
    battery_status=$(dsbattery)
    echo "true" >/tmp/ds4_status
    echo "$1" >/tmp/ds4_battery
    # Check if the output contains the charging symbol "↑"
    if [[ "$battery_status" == *"↑"* ]]; then
      echo "charging"
      if ! [[ -f /tmp/ds4_charging ]]; then
        if [[ -f /tmp/ds4_notcharging ]]; then
          rm "/tmp/ds4_notcharging"
        fi
        touch "/tmp/ds4_charging"
        ramdon_notify "joyley_juiceon"
      fi
    else
      echo "not charging"
      if [[ -f /tmp/ds4_charging ]]; then
        if ! [[ -f /tmp/ds4_notcharging ]]; then
          ramdon_notify "joyley_juiceoff"
          rm "/tmp/ds4_charging"
        fi
        touch "/tmp/ds4_notcharging"
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

# Loop to continuously check the battery level
while true; do
  idle=$(pgrep -fl 'idle_joy.py')
  text=$(dsbattery)
  result=$(echo "$text" | grep -o '[0-9]*')
  ds4 $result $idle $text
  sleep 2
done
