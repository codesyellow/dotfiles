#!/bin/bash

# Input string
input=$(dsbattery)

# Check if the input contains 'icon' or 'perc'
if [[ $1 == "icon" ]]; then
    # Extract and print the icon
    icon=$(echo "$input" | grep -oE '^.+? ')
    echo "$icon"
elif [[ $1 == "perc" ]]; then
    # Extract and print the percentage
    perc=$(echo "$input" | grep -oE '[0-9]+%')
    echo "$perc"
else
    # Invalid argument
    echo "Usage: $0 [icon|perc]"
fi
