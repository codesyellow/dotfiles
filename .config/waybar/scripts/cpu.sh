#!/bin/bash
cpu_icon=
cpu_usage=$(top -bn2 | grep "Cpu(s)" | awk 'NR==2 {print 100 - $8}')

# Round to nearest integer
cpu_usage_int=$(printf "%.0f" "$cpu_usage")
if [[ $cpu_usage_int -ge 80 ]]; then
  state="warning"
  output="<span size='15000' foreground='#4c566a'> | </span>$cpu_icon $cpu_usage_int%"
else
  output=""
fi

echo "{\"text\": \"$output\", \"tooltip\": \"Pomodoro Timer\", \"class\": \"$state\"}"
