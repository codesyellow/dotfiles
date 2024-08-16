#!/bin/bash
nm="^c#d8dee9^"
wn="^c#F6E96B^"
al="^c#FF4E88^"

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

to_late="21:00"
volume=$(pamixer --get-volume)
checkupdates=$(cat /tmp/updates)
is_muted=$(pamixer --get-mute)
is_easy_active=$(pgrep 'easyeffects')
server=$(cat /tmp/map_display)
santos=$(cat /tmp/santosmatch)
server_status=$(cat /tmp/server_status)
ds4_bat=$(cat /tmp/ds4_battery)
ds4_status=$(cat /tmp/ds4_status)
#climate=$(curl 'wttr.in/Santos?format="%t"' | sed 's/[^0-9]*//g')
day=$(date +"%a" | tr '[:lower:]' '[:upper:]')
easy=$(easy_preset.sh)
cputemp=$(cat /sys/class/thermal/thermal_zone2/temp | cut -c 1-2)
root=$(df -h | awk '{ if ($6 == "/") print $4 }')
root_int=${root::-1}
#home=$(df -h | awk '{ if ($6 == "/home") print $4 }')
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

if [[ -n $santos ]]; then
  status+=" $nm|$nm $santos"
fi

# if [[ $climate -le 25 ]]; then
#   status+="   $cold $climate°"
# else
#   status+="   $hot $climate°"
# fi
#

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
  status+=" $nm| $al$cpu_temp_mid $cputemp°"
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
elif [[ $(echo "$root_int < 5" | bc) -ne 0 ]]; then
  status+=" $nm| $al$root_icon $root_int""g"
else
  status+=" $nm| $nm$root_icon $root_int""g"
fi

echo "$houre"

seconds1=$(date -d "$houre" +%s)
seconds2=$(date -d "$to_late" +%s)

if ((seconds1 >= seconds2)); then
  status+=" $nm| $al$date_icon $al$houre $nm$day_month $day "
else
  status+=" $nm| $nm$date_icon $nm$houre $day_month $day "
fi

xprop -root -set WM_NAME "$status "
