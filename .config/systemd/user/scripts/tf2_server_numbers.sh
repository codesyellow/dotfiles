#!/usr/bin/env bash
player_count() {
  count=$(curl -s -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36" "$1" | pup 'span.srvPage-countCur text{}')
  echo "$count"
}

dustbowl_count=$(player_count "https://tsarvar.com/en/servers/team-fortress-2/205.178.182.182:27060")
badwater_count=$(player_count "https://tsarvar.com/en/servers/team-fortress-2/95.214.180.108:27015")
turbine_count=$(player_count "https://tsarvar.com/en/servers/team-fortress-2/131.196.196.197:27610")

if [[ $dustbowl_count -ge 5 ]]; then
  if [[ -f "/tmp/disable_server_info" ]]; then
    rm "/tmp/disable_server_info"
  fi
  echo "$dustbowl_count" >"/tmp/dustbowl_count"
else
  echo "Dustbowl server don't have enough players"
fi

if [[ "$turbine_count" -ge 30 ]]; then
  if [[ -f "/tmp/disable_server_info" ]]; then
    rm "/tmp/disable_server_info"
  fi
  echo "$turbine_count" >"/tmp/turbine_count"
else
  echo "Turbine server don't have enough players"
fi

if [[ $badwater_count -ge 5 ]]; then
  if [[ -f "/tmp/disable_server_info" ]]; then
    rm "/tmp/disable_server_info"
  fi
  echo "$badwater_count" >"/tmp/badwater_count"
else
  echo "Badwater server don't have enough players"
fi

if [[ $badwater_count -le 4 ]] && [[ $dustbowl_count -le 4 ]] && [[ $turbine_count -le 29 ]]; then
  touch "/tmp/disable_server_info"
fi
