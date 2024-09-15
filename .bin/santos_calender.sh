#!/usr/bin/env bash

show_teams=600
show_hour=3600
current_month=$(date +"%m")
current_day=$(date +"%d")
santoss_match="/tmp/santosmatch"

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

match_hour=$(echo "$hour" | sed 's/"//g')
match_teams=$(echo "$match" | sed 's/"//g')
if [[ -n $match_hour ]] && [[ -n $match_teams ]]; then

  while true; do
    game_hour=$(date -d "$match_hour" +"%H:%M")
    actual_time=$(date +"%H:%M")
    game_hour_sec=$(date -d "$game_hour today" +"%s")
    actual_time_sec=$(date -d "$actual_time today" +"%s")
    if [[ -f "/tmp/santos_pregame_hour" ]]; then
      echo "$match_hour" > "/tmp/santos_pregame_hour"
    fi

    if [[ $actual_time_sec -ge $game_hour_sec ]]; then
      echo "The game is about to start or has started already!"
      if [[ -f "$santosmatch" ]]; then
        rm "$santoss_match"
      fi
      break
    fi

    if [[ -f "/tmp/matchup" ]]; then
      rm "/tmp/matchup"
    fi

    echo "$match_hour" >"$santoss_match"
    echo "Displaying hour"
    sleep $show_hour
    echo "$match_teams" >"$santoss_match"
    echo "Displaying matchup"
    touch "/tmp/matchup"
    sleep $show_teams
  done
else
  echo "No matchs for Santos for now."
  if [[ -f "$santoss_match" ]]; then
    rm "$santoss_match"
  fi
fi
