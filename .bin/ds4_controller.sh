#!/usr/bin/env bash

# Function to write content to a temp file
update_temp_file() {
  local file="$1"
  local content="$2"
  echo "$content" >"/tmp/$file"
}

# Function to determine if the battery is charging
is_it_charging() {
  battery_status=$(dsbattery)
  # Check if the status contains the charging indicator, e.g., "↑"
  if [[ "$battery_status" == *"↑"* ]]; then
    'yes'
    return 0
  else
    'no'
    return 1
  fi
}

# Main function to update status and battery information
ds4() {
  echo "oi"
  local battery_level="$1"
  local charging_status

  if [[ -z "$battery_level" ]]; then
    update_temp_file "ds4_status" "false"
    rm -f "/tmp/ds4_first_connect"
  else
    update_temp_file "ds4_status" "true"
    update_temp_file "ds4_battery" "$battery_level"

    if is_it_charging; then
      charging_status="charging"
    else
      charging_status="not charging"
    fi

    update_temp_file "ds4_charging_status" "$charging_status"
  fi
}

while sleep 2; do
  ds=$(dsbattery)
  if [[ -z $ds ]] && [[ -f "/tmp/ds4_logger" ]]; then
    rm -f "/tmp/ds4_logger"
  fi
  bat=$(echo "$ds" | grep -o '[0-9]*')
  ds4 "$bat"
done
