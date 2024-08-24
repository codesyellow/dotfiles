#!/usr/bin/env bash

player_count() {
  count=$(curl -s -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36" "$1" | pup 'span.srvPage-countCur text{}')
  echo "$count"
}

display_server_info() {
  echo "$1" >"/tmp/tf2_badwater_count"
  echo "$2" >"/tmp/map_display"
}

cicle_maps_to_display() {
  badwater_icon=''
  dustbowl_icon=''

  sleep_time=2
  current_time=$(date "+%H")
  current_hour=$((10#$current_time))
  if [[ $current_hour -ge 22 ]]; then
    echo "Increasing the sleep time of the maps_to_display"
    touch "/tmp/disable_server_info"
    main_sleep_time=25600
  else
    if [[ $sleep_time != 2 ]]; then
      sleep_time=2
    fi
    if [[ -f "/tmp/disable_server_info" ]]; then
      rm "/tmp/disable_server_info"
    fi
  fi

  while true; do
    if [[ -f "/tmp/dustbowl_count" ]]; then
      dustbowl=$(</tmp/dustbowl_count)
      echo "$dustbowl_icon $dustbowl" >"/tmp/map_display"
      sleep 30
    fi
    if [[ -f "/tmp/badwater_count" ]]; then
      badwater=$(</tmp/badwater_count)
      echo "$badwater_icon $badwater" >"/tmp/map_display"
      sleep 30
    fi
    sleep $sleep_time
  done &
}

cicle_maps_to_display

main_sleep_time=600

while true; do
  dustbowl_count=$(player_count "https://tsarvar.com/en/servers/team-fortress-2/205.178.182.182:27060")
  badwater_count=$(player_count "https://tsarvar.com/en/servers/team-fortress-2/95.214.180.108:27015")
  echo $dustbowl_count
  echo $badwater_count

  current_time=$(date "+%H")
  current_hour=$((10#$current_time))
  if [[ $current_hour -ge 22 ]]; then
    echo "Increasing the sleep time"
    main_sleep_time=25600
  else
    if [[ $main_sleep_time != 600 ]]; then
      main_sleep_time=600
    fi
    if [[ -f "/tmp/disable_server_info" ]]; then
      rm "/tmp/disable_server_info"
    fi
  fi

  if [[ $dustbowl_count -ge 5 ]]; then
    if [[ -f "/tmp/disable_server_info" ]]; then
      rm "/tmp/disable_server_info"
    fi
    echo "$dustbowl_count" >"/tmp/dustbowl_count"
  else
    echo "Dustbowl server don't have enough players"
    if [[ -f "/tmp/badwater_count" ]]; then
      rm "/tmp/dustbowl_count"
    fi
    if ! [[ -f "/tmp/disable_server_info" ]] && [[ $badwater_count -le 4 ]]; then
      touch "/tmp/disable_server_info"
    fi

  fi

  if [[ $badwater_count -ge 5 ]]; then
    if [[ -f "/tmp/disable_server_info" ]]; then
      rm "/tmp/disable_server_info"
    fi
    echo "$badwater_count" >"/tmp/badwater_count"
  else
    echo "Badwater server don't have enough players"
    if [[ -f "/tmp/badwater_count" ]]; then
      rm "/tmp/badwater_count"
    fi
    if ! [[ -f "/tmp/disable_server_info" ]] && [[ $dustbowl_count -le 4 ]]; then
      touch "/tmp/disable_server_info"
    fi

  fi
  sleep $main_sleep_time
done
