#!/bin/bash
# Save this file as /home/cie/.bin/memory_usage.sh

# Get the used memory percentage as an integer
freemen_per=$(free -m | awk 'NR==2{printf "%.0f", $3*100/$2}')
echo "$freemen_per" >/tmp/memory_usage
