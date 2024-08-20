#!/bin/bash
nm="^c#d8dee9^"
wn="^c#ebcb8b^"
al="^c#bf616a^"

ram_icon=
server_icon=$(cat /tmp/map_display-icon)
cpu_icon=
root_icon=
home_icon=
date_icon=
cpu_temp_low=
cpu_temp_mid=
cpu_temp_high=
controller=
sleep_time=2

to_late="21:00"

while true; do

  volume=$(</tmp/volume)
  checkupdates=$(</tmp/updates)
  is_muted=$(pamixer --get-mute)
  is_easy_active=$(pgrep 'easyeffects')
  server=$(</tmp/map_display)
  santos=$(</tmp/santosmatch)
  server_status=$(</tmp/server_status)
  ds4_bat=$(</tmp/ds4_battery)
  ds4_status=$(</tmp/ds4_status)
  climate=$(</tmp/climate)
  day=$(date +"%a" | tr '[:lower:]' '[:upper:]')
  easy=$(/home/cie/.bin/easy_preset.sh)
  cputemp=$(</tmp/cpu_temp)
  root=$(df -h | awk '{ if ($6 == "/") print $4 }')
  root_int=${root::-1}
  freemen_per=$(free -m | awk 'NR==2{print $3*100/$2 }')
  freemen_per_int=$(printf "%.0f\n" "$freemen_per")
  date=$(date +"%m")
  day_month=$(date +"%d")
  hour=$(echo "$hour" | sed 's/^0*//') # Remove leading zeros
  houre=$(date +"%H:%M")
  cpu=$(awk '{u=$2+$4; t=$2+$4+$5; if (NR==1){u1=u; t1=t;} else print ($2+$4-u1) * 100 / (t-t1) "%"; }' \
    <(grep 'cpu ' /proc/stat) <(
      sleep 1
      grep 'cpu ' /proc/stat
    ))
  cpu=$(echo "$cpu" | tr -d '%') # Remove the '%' sign if present
  cpu_per_int=$(printf "%.0f\n" "$cpu")

  status=""

  if [[ -n $is_easy_active ]]; then
    if [[ $easy = "eq" ]]; then
      status+="$nm"
    else
      status+="$wn"
    fi
  else
    status+="$wn !"
  fi

  if [[ -f "/tmp/santosmatch" ]]; then
    if [[ -f "/tmp/matchup" ]] && [[ $santos == *"x"* ]]; then
      status+=" $nm|$wn $santos"
    else
      status+=" $nm|$nm $santos"
    fi
  fi

  if [[ "$climate" -ge 30 ]]; then
    status+=" $nm|  $climate"
  elif [[ "$climate" -le 20 ]]; then
    status+=" $nm|  $climate"
  else
    status+=" $nm|  $climate"
  fi

  if [[ $server_status == 'true' ]]; then
    status+=" $nm| $server_icon $server"
  fi

  if [[ $checkupdates -le 20 ]]; then
    status+=" $nm|  $checkupdates"
  elif [[ $checkupdates -ge 21 ]] && [[ $checkupdates -le 40 ]]; then
    status+=" $wn|  $checkupdates"
  else
    status+=" $al|  $checkupdates"
  fi

  if [[ -f /tmp/ds4_status ]]; then
    if [[ $ds4_status == 'false' ]]; then
      status+=" $nm| $nm$controller "
    elif [[ -f /tmp/ds4_charging ]]; then
      status+=" $nm| $wn$controller  "
    elif [[ $ds4_bat -ge 51 && $ds4_bat -le 70 ]]; then
      status+=" $nm| $nm$controller  "
    elif [[ $ds4_bat -le 50 && $ds4_bat -ge 30 ]]; then
      status+=" $nm| $wn$controller  "
    elif [[ $ds4_bat -le 29 ]]; then
      status+=" $nm| $al$controller  "
    else
      status+=" $nm| $nm$controller  "
    fi
  else
    status+=" $nm| $nm$controller "
  fi

  if [[ $is_muted == 'false' ]]; then
    if [[ $volume -ge 60 ]]; then
      status+=" $nm| $al $volume%"
    elif [[ $volume -le 59 ]] && [[ $volume -ge 1 ]]; then
      status+=" $nm| $nm $volume%"
    elif [[ $volume -eq 0 ]]; then
      status+=" $nm| $wm $volume%"
    fi
  else
    status+=" $nm| $al $volume%"
  fi

  if [[ $cputemp -le 60 ]]; then
    status+=" $nm| $nm $cpu_temp_low $cputemp°"
  elif [[ $cputemp -ge 61 && $cputemp -le 70 ]]; then
    status+=" $nm| $wn$cpu_temp_mid $cputemp°"
  else
    status+=" $nm| $al$cpu_temp_high $cputemp°"
  fi

  if [[ $cpu_per_int -ge 80 ]]; then
    status+=" $nm| $al$cpu_icon $cpu_per_int%"
  elif [[ $cpu_per_int -ge 60 ]] && [[ $cpu_per_int -le 79 ]]; then
    status+=" $nm| $wn$cpu_icon $cpu_per_int%"
  else
    status+=" $nm| $nm$cpu_icon $cpu_per_int%"
  fi

  if [[ $freemen_per_int -ge 70 ]]; then
    status+=" $nm| $wm$ram_icon $freemen_per_int%"
  elif [[ $freemen_per_int -ge 50 ]] && [[ $freemen_per_int -le 60 ]]; then
    status+=" $nm| $al$ram_icon $freemen_per_int%"
  else
    status+=" $nm| $nm$ram_icon $freemen_per_int%"
  fi

  if [[ $(echo "$root_int < 20" | bc) -ne 0 ]]; then
    status+=" $nm| $wm$root_icon $root_int""g"
  elif [[ $(echo "$root_int < 10" | bc) -ne 0 ]]; then
    status+=" $nm| $al$root_icon $root_int""g"
  else
    status+=" $nm| $nm$root_icon $root_int""g"
  fi

  seconds1=$(date -d "$houre" +%s)
  seconds2=$(date -d "$to_late" +%s)

  if ((seconds1 >= seconds2)); then
    status+=" $nm| $al$date_icon $al$houre $nm$day_month $day "
  else
    status+=" $nm| $nm$date_icon $nm$houre $day_month $day "
  fi

  xprop -root -set WM_NAME "$status "
  sleep $sleep_time
done
