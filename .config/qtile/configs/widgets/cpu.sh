#!/bin/bash
cpu_icon=
cpu_usage=$(top -bn2 | grep "Cpu(s)" | awk 'NR==2 {print 100 - $8}')

# Round to nearest integer
cpu_usage_int=$(printf "%.0f" "$cpu_usage")
if [[ $cpu_usage_int -ge 80 ]]; then
  output="$cpu_icon  $cpu_usage_int%"
  printf '<span size="x-large" foreground="#fff">| </span><span rise="3700" foreground="#EF5A6F">%s</span>' "$output"
fi
