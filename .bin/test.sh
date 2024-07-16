#!/bin/bash

# The input string
input=$(curl curl -s -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36" https://teamwork.tf/community/quickplay/class-wars | grep -A 5 "PG | CLASS WARS US | D")

# Extract numbers using grep and sed
numbers=$(echo "$input" | grep -o '[0-9]\+ / [0-9]\+' | sed 's/ /\\n/g' | grep -o '[0-9]\+')

# Print the numbers
echo "$numbers"
