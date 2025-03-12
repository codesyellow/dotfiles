#!/usr/bin/env bash

classes='["normal", "root"]'
day=$(date +%d)
weekday=$(date +%a)
hour=$(date +%H:%M)

text="<span font_family='VictorMono Nerd Font Mono' font_weight='ultralight'>DAY:</span>$hour $day $weekday"
output="{\"text\": \"$text\", \"tooltip\": \"Updates: $day\", \"class\": $classes}"
echo $output
