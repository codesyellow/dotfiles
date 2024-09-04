#!/bin/bash

if [[ -f "/tmp/santosmatch" ]]; then
  santos=$(</tmp/santosmatch)
  if [[ -f "/tmp/matchup" ]] && [[ $santos == *"x"* ]]; then
    output=" $santos"
  else
    output=" $santos"
  fi
else
  output=""
fi

# Properly escape any double quotes in the output
output=$(echo "$output" | sed 's/"/\\"/g')

# Print the JSON output
echo "{\"text\": \"$output\", \"tooltip\": \"Santos Game\" }"
