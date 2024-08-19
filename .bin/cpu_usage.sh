#!/bin/bash

# Paths
CPU_FILE="/tmp/cpu_usage"

# Function to calculate CPU usage
get_cpu_usage() {
  # Read the first line from /proc/stat
  local cpu_line=$(head -n 1 /proc/stat)
  local cpu_vals=(${cpu_line#cpu})

  # Sum the values
  local total=0
  for val in "${cpu_vals[@]}"; do
    total=$((total + val))
  done

  # Calculate idle time
  local idle=${cpu_vals[3]}

  echo "$total $idle"
}

# Initial read
read -r prev_total prev_idle < <(get_cpu_usage)
sleep 1

# Second read
read -r total idle < <(get_cpu_usage)

# Calculate usage
total_diff=$((total - prev_total))
idle_diff=$((idle - prev_idle))
cpu_usage=$(((100 * (total_diff - idle_diff)) / total_diff))

# Write to file
echo "$cpu_usage%" >"$CPU_FILE"
