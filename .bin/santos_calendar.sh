#!/bin/bash
santoss_match="/tmp/santosmatch"
current_month=$(date +"%m")
current_day=$(date +"%d")

todays_match=$(jq --arg cm "$current_month" --arg cd "$current_day" '
  .matchs 
  | to_entries[] 
  | select(.value.month == $cm and .value.day == $cd) 
  | "\(.value.hour) \(.value.match)"
' /home/cie/.config/santosfc/santos.json)

while IFS= read -r line; do
  hour=$(echo "$line" | awk '{print $1}')
  match=$(echo "$line" | awk '{$1=""; print $0}' | sed 's/^ //')

  eval "hour=\$hour"
  eval "match=\$match"

done <<<"$todays_match"
