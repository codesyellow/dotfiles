#!/usr/bin/env bash
ds4_bat=$(dsbattery | awk '{print $2}')

if [[ -z "$ds4_bat" ]]; then
    classes='["normal", "ds4"]' # Use JSON array syntax
    text=""
    output="{\"text\": \"$text\", \"tooltip\": \"Updates: $ds4_bat\", \"class\": $classes}"
else
    classes='["normal", "ds4"]' # Use JSON array syntax
    text="<span>$ds4_bat</span>"
    output="{\"text\": \"$text\", \"tooltip\": \"Updates: $ds4_bat\", \"class\": $classes}"
fi

echo $output
