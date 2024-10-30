#!/bin/bash
root_icon=
disk_usage=$(df -h | awk '{ if ($6 == "/") print $4 }')
disk_num=$(printf "%.0f" "$(echo "${disk_usage::-1}" | bc)")

if [[ $disk_num -le 15 ]]; then
  state="warning"
  output="<span size='15000' foreground='#4c566a'>| </span>$root_icon $disk_num""g "
else
  state="normal"
  output=""
fi

echo "{\"text\": \"$output\", \"tooltip\": \"Pomodoro Timer\", \"class\": \"$state\"}"
