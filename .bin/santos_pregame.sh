#!/usr/bin/env bash
pregame_path="/tmp/santos_pregame_hour"

notify_prior() {
  game_time="$1"
  game_hour="${game_time%:*}"
  game_minutes="${game_time#*:}"
  game_offset=-2

  current_time=$(date +"%H:%M")
  current_hour="${current_time%:*}"
  current_minutes="${current_time#*:}"

  # Remove leading zeros to avoid octal interpretation
  game_hour=$((10#$game_hour))
  game_minutes=$((10#$game_minutes))
  current_hour=$((10#$current_hour))
  current_minutes=$((10#$current_minutes))

  new_hours=$(((game_hour + game_offset + 24) % 24))

  if [[ "$current_hour" -ge "$new_hours" ]] && [[ "$current_minutes" -ge "$game_minutes" ]]; then
    notify-send -u critical -i $HOME/.local/share/icons/football.png "Pregame is about to start!!!"
    exit 1
  fi
}

if [[ -f "$pregame_path" ]]; then
  while true; do
    pregame_hour=$(cat $pregame_path)
    notify_prior "$pregame_hour"

    sleep 10
  done
else
  echo "No games for today!"
fi
