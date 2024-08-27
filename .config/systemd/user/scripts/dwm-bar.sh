#!/bin/bash
nm="^c#d8dee9^"
wn="^c#ebcb8b^"
al="^c#bf616a^"

ram_icon=
cpu_icon=
root_icon=
home_icon=
date_icon=
cpu_temp_low=
cpu_temp_mid=
cpu_temp_high=
controller=
sleep_time=2
ds4_status_sleep=10
ssd_space_sleep=60
ram_usage_sleep=10
check_updates_sleep=60
get_volume_sleep=10
get_hour=5
day_week_sleep=7200

to_late="21:00"

ds4_status() {
  while true; do
    ds4=$(dsbattery)
    if [[ -n "$ds4" ]]; then
      if ! [[ -f "/tmp/ds4_active" ]]; then
        touch "/tmp/ds4_active"
      fi

      if [[ "$ds4" == *"↑"* ]]; then
        if ! [[ -f "/tmp/ds4_charging" ]]; then
          touch "/tmp/ds4_charging"
        fi
      else
        if [[ -f "/tmp/ds4_charging" ]]; then
          rm "/tmp/ds4_charging"
        fi
        echo $(echo "$ds4" | grep -o '[0-9]*') >"/tmp/ds4_battery"
      fi
    else
      if [[ -f "/tmp/ds4_active" ]]; then
        rm "/tmp/ds4_active"
      fi
    fi
    sleep $ds4_status_sleep
  done &
}

ssd_space() {
  while true; do
    root=$(df -h | awk '{ if ($6 == "/") print $4 }')
    root_int=${root::-1}
    echo "$root_int" >"/tmp/ssd_space"

    sleep $ssd_space_sleep
  done &
}

ram_usage() {
  while true; do
    freemen_per=$(free -m | awk 'NR==2{print $3*100/$2 }')
    freemen_per_int=$(printf "%.0f\n" "$freemen_per")
    echo "$freemen_per_int" >"/tmp/ram_usage"

    sleep $ram_usage_sleep
  done &
}

check_updates() {
  while true; do
    echo $(checkupdates | wc -l) >"/tmp/checkupdates"
    sleep $check_updates_sleep
  done &
}

get_volume() {
  while true; do
    is_it_muted=$(pamixer --get-mute)
    if [[ "$is_it_muted" == "true" ]]; then
      touch "/tmp/volume_muted"
    else
      if [[ -f "/tmp/volume_muted" ]]; then
        rm "/tmp/volume_muted"
      fi
    fi
    echo $(pamixer --get-volume) >"/tmp/volume"
    sleep $get_volume_sleep
  done &
}

get_day_month() {
  while true; do
    echo $(date +"%d") >"/tmp/day_month"
    sleep $day_week_sleep
  done &
}

get_hour() {
  while true; do
    echo $(date +"%H:%M") >"/tmp/hours"
    sleep 5
  done &
}

get_week() {
  while true; do
    echo $(date +"%a" | tr '[:lower:]' '[:upper:]') >"/tmp/week_day"
    sleep $day_week_sleep
  done &
}

is_easyeffects_active() {
  while true; do
    echo $(pgrep 'easyeffects') >"/tmp/easy_active"
    sleep 10
  done &
}

get_cpu_usage() {
  while true; do
    # Read the first line from /proc/stat
    read cpu user nice system idle iowait irq softirq steal guest guest_nice </proc/stat

    # Calculate the total and idle time
    total=$((user + nice + system + idle + iowait + irq + softirq + steal))
    idle_time=$((idle + iowait))

    # Sleep for 1 second to calculate the difference
    sleep 1

    # Read the updated values after 1 second
    read cpu user nice system idle iowait irq softirq steal guest guest_nice </proc/stat

    # Calculate the new total and idle time
    total_new=$((user + nice + system + idle + iowait + irq + softirq + steal))
    idle_new=$((idle + iowait))

    # Calculate the difference
    total_diff=$((total_new - total))
    idle_diff=$((idle_new - idle_time))

    # Calculate the CPU usage percentage
    cpu_usage=$((100 * (total_diff - idle_diff) / total_diff))

    echo "$cpu_usage" >"/tmp/cpu_usage"
    sleep 2
  done &
}

ds4_status
ssd_space
ram_usage
check_updates
get_volume
get_week
get_day_month
get_hour
is_easyeffects_active
get_cpu_usage

while true; do
  volume=$(</tmp/volume)
  checkupdates=$(</tmp/checkupdates)
  is_easy_active=$(</tmp/easy_active)
  server=$(</tmp/map_display)
  server_status="/tmp/disable_server_info"
  server_icon=$(</tmp/map_display-icon)
  ds4_bat=$(cat /tmp/ds4_battery)
  climate=$(</tmp/climate)
  day=$(</tmp/week_day)
  easy=$(</home/cie/.config/.easy_preset)
  cputemp=$(</tmp/cpu_temp)
  freemen_per_int=$(</tmp/ram_usage)
  root_int=$(</tmp/ssd_space)
  day_month=$(</tmp/day_month)
  houre=$(</tmp/hours)
  cpu_per_int=$(</tmp/cpu_usage)

  status=""

  if [[ -n $is_easy_active ]]; then
    if [[ $easy = "LoudnessEqualizer" ]]; then
      status+="$nm"
    else
      status+="$wn"
    fi
  else
    status+="$wn !"
  fi

  if [[ -f "/tmp/santosmatch" ]]; then
    santos=$(</tmp/santosmatch)
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

  if ! [[ -f $server_status ]]; then
    status+=" $nm| $server"
  fi

  if [[ $checkupdates -le 20 ]]; then
    status+=" $nm|  $checkupdates"
  elif [[ $checkupdates -ge 21 ]] && [[ $checkupdates -le 40 ]]; then
    status+=" $wn|  $checkupdates"
  else
    status+=" $al|  $checkupdates"
  fi

  if ! [[ -f /tmp/ds4_active ]]; then
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

  if ! [[ -f "/tmp/volume_muted" ]]; then
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
    status+=" $nm| $wn$date_icon $wn$houre $nm$day_month $day "
  else
    status+=" $nm| $nm$date_icon $nm$houre $day_month $day "
  fi

  xsetroot -name "$status "
  sleep $sleep_time
done
