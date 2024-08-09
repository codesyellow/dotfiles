#!/usr/bin/env bash

get_count() {
  count=$(curl -s -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36" $1 | pup 'dt:contains("Player count") + dd text{}')
  echo $count
}

store_status() {
  count=$1
  map=$2
  if [[ "$count" -le 5 ]]; then
    echo 'false' >"/tmp/${map}_status"
    echo "$count" >"/tmp/tf2_${map}_count"
  else
    echo 'true' >"/tmp/${map}_status"
    echo "$count" >"/tmp/tf2_${map}_count"
  fi
}

while true; do
  dustbowl_count=$(get_count "https://www.battlemetrics.com/servers/tf2/16583539" | cut -d'/' -f1)
  badwater_count=$(get_count "https://www.battlemetrics.com/servers/tf2/22316887" | cut -d'/' -f1)
  echo $dustbowl_count
  echo $badwater_count
  store_status $badwater_count "badwater"
  store_status $dustbowl_count "dustbowl"

  current_hour=$(date +%H)
  if [[ $current_hour -ge 22 ]] || [[ $current_hour -lt 6 ]]; then
    echo 'false' >/tmp/server_status
    sleep_duration=$((8 * 3600)) # 8 hours in seconds
  else
    sleep_duration=1200 # 20 minutes in seconds
  fi

  sleep $sleep_duration
done
