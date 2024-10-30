#!/bin/bash
home_icon=
disk_usage=$(df -h | awk '{ if ($6 == "/home") print $4 }')
disk_num=$(printf "%.0f" "$(echo "${disk_usage::-1}" | bc)")

if [[ $disk_num -le 20 ]]; then
  state="warning"
  output="<span size='15000' foreground='#4c566a'>|</span> $home_icon $disk_num""g "

else
  state="normal"
  output=""
fi

echo "{\"text\": \"$output\", \"tooltip\": \"Pomodoro Timer\", \"class\": \"$state\"}"
