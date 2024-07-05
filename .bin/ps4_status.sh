#!/bin/bash

# Input string
input=$(dsbattery)

if [[ $1 == "icon" ]]; then
	echo ""
elif [[ $1 == "perc" ]]; then
	perc=$(echo "$input" | grep -oE '[0-9]+%')
	echo "$perc"
else
	echo "Usage: $0 [icon|perc]"
fi
