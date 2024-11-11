#!/bin/bash
cpu_icon=
cpu_usage=$(top -bn2 | grep "Cpu(s)" | awk 'NR==2 {print 100 - $8}')

# Round to nearest integer
cpu_usage_int=$(printf "%.0f" "$cpu_usage")
if [[ $cpu_usage_int -ge 70 ]]; then
  printf '<span size="x-large" foreground="#4c566a">| </span><span rise="4800" foreground="#EF5A6F">%s</span> <span rise="3800" foreground="#EF5A6F">%s</span>' "$cpu_icon" "$cpu_usage_int%"
fi
