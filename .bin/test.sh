#!/bin/bash

log_file="/tmp/ds4_logger"
idle_crit=15
idle_warn=10

if [[ -f "$log_file" ]]; then
  # Read the last logged time from the file
  last_time=$(cat "$log_file")

  # Convert last time to seconds since the epoch
  last_time_epoch=$(date -d "$last_time" +"%s")
  current_time_epoch=$(date +"%s")

  # Calculate the difference in minutes
  time_diff=$(((current_time_epoch - last_time_epoch) / 60))

  if ((time_diff >= idle_warn)); then
    notify-send.sh "inac" "has ben for warn"
  elif ((time_diff >= idle_crit)); then
    notify-send.sh "inac" "ggg over"
  fi
else
  echo "Log file not found!"
fi
