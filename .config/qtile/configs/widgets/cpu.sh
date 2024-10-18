#!/bin/bash
cpu_icon=
cpu_usage=$(top -bn2 | grep "Cpu(s)" | awk 'NR==2 {print 100 - $8}')

# Round to nearest integer
cpu_usage_int=$(printf "%.0f" "$cpu_usage")
if [[ $cpu_usage_int -ge 80 ]]; then
  output="$cpu_icon  $cpu_usage_int%"
  printf '<span foreground="#d8dee9">%s</span>' "$output"
fi
