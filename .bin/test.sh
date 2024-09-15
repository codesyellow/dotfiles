#!/bin/sh
exec 2>&1
printf "$$" >~/.cache/pidofbar
tick=0
ticktime=1
nm="^c#d8dee9^"
wn="^c#ebcb8b^"
al="^c#bf616a^"

pacman=
ram_icon=
cpu_icon=
root_icon=
home_icon=
date_icon=
pymor_icon=
pymor_icon_half=
pymor_icon_empty=
cpu_temp_low=
cpu_temp_mid=
cpu_temp_high=
controller=

update() {
  [ $((tick % 2)) -eq 0 ] && {
      is_easy_active=$(pgrep 'easyeffects')
      easy=$(</home/cie/.config/.easy_preset)
      if [[ -n $is_easy_active ]]; then
	if [[ $easy = "LoudnessEqualizer" ]]; then
	  easyeffects="$nm"
	else
	  easyeffects="$wn"
	fi
      else
	easyeffects="$wn !"
      fi
  }
  [ $((tick % 1)) -eq 0 ] && {
    if [[ -f "/tmp/stretch" ]]; then
      if [[ -f "/tmp/stretch_start" ]]; then
	stretch=" $nm|$wn  GET READY!"
      fi
      if [[ -f "/tmp/stop" ]]; then
	stretch=" $nm|$al  STOP!"
      else
	stretch=" $nm|$wn  DO IT!!"
      fi 
    else
      stretch=""
    fi
  }

  [ $((tick % 1)) -eq 0 ] && {
    pomodoro="/tmp/pomodoro_time"
    if [[ -f "$pomodoro" ]]; then
      pomodoro_number=$(cat "$pomodoro")
      if [[ ! -f "/tmp/pomo_half" ]]; then
	let pomo_half=pomodoro_number/2
	touch "/tmp/pomo_half"
      fi

      if [[ "$pomodoro_number" -le "$pomo_half" ]] && [[ "$pomodoro_number" -ge 6 ]]; then
	pymor=" $nm| $nm$pymor_icon_half $pomodoro_number"
      else
	pymor=" $nm| $nm$pymor_icon $pomodoro_number"
      fi

      if [[ "$pomodoro_number" -le 5 ]]; then
	pymor=" $nm| $wn$pymor_icon_empty $pomodoro_number"
      fi
    else
      pymor=""
      if [[ -f "/tmp/pomo_half" ]]; then
	rm "/tmp/pomo_half"
      fi
    fi
  }
  [ $((tick % 15)) -eq 0 ] && {
    if [[ -f "/tmp/santosmatch" ]]; then
      santos=$(</tmp/santosmatch)
      if [[ -f "/tmp/matchup" ]] && [[ $santos == *"x"* ]]; then
	smatch=" $nm|$wn  $santos"
      else
	smatch=" $nm|$nm  $santos"
      fi
    else
      smatch=""
    fi
  }
  [ $((tick % 3)) -eq 0 ] && {
    key_variant=$(xkb-switch -p)
    if [[ "$key_variant" == "us(intl)" ]]; then
      variant=" $nn|$wn  INTL" 
    else
      variant=" $nm|$nm  US"
    fi
  }
  [ $((tick % 3600)) -eq 0 ] && {
    climate_num=$(curl -s "http://api.openweathermap.org/data/2.5/weather?lat=-23.963&lon=-46.3918&appid=2d6602a071d92529af1939b0152f5aba&units=metric" | jq '.main.temp | round')
    climate=''
    if [[ -n $climate_num ]]; then
      if [[ "$climate_num" -ge 30 ]]; then
	climate=" $nm|  $climate_num"
      elif [[ "$climate_num" -le 20 ]]; then
	climate=" $nm|  $climate_num"
      else
	climate=" $nm|  $climate_num"
      fi
    else
      climate=" $nm|  X"
    fi
  }
  [ $((tick % 10)) -eq 0 ] && {
    server_status="/tmp/disable_server_info"
    if [[ -f "/tmp/dustbowl_count" ]] || [[ -f "/tmp/turbine_count" ]] || [[ -f "/tmp/badwater_count" ]]; then
      server_info=$(</tmp/map_display)
      if [[ ! -f $server_status ]]; then
	server=" $nm| $server_info"
      else
	server=""
      fi
    else
      server=""
    fi
  }
  [ $((tick % 300)) -eq 0 ] && {
    updates_num=$(checkupdates | wc -l)
    if [[ $updates_num -le 20 ]]; then
     updates=" $nm|  $updates_num"
    elif [[ $updates_num -ge 21 ]] && [[ $updates_num -le 40 ]]; then
      updates=" $wn|  $updates_num"
    else
      updates=" $al|  $updates_num"
    fi
  }
  [ $((tick % 10)) -eq 0 ] && {
    ds4=$(dsbattery)
    if [[ -n "$ds4" ]]; then
      ds4_charging="false"
      ds4_status=""
      if [[ "$ds4" == *"↑"* ]]; then
	ds4_charging="true"
	ds4_status=" $nm| $wn$controller  "
      else
	ds4_bat=$(echo "$ds4" | grep -o '[0-9]*')
	ds4_charging="false"
	if [[ $ds4_bat -ge 51 && $ds4_bat -le 70 ]]; then
	  ds4_status=" $nm| $nm$controller  "
	elif [[ $ds4_bat -le 50 && $ds4_bat -ge 30 ]]; then
	  ds4_status=" $nm| $wn$controller  "
	elif [[ $ds4_bat -le 29 ]]; then
	  ds4_status=" $nm| $al$controller  "
	else
	  ds4_status=" $nm| $nm$controller  "
	fi
      fi
    else
      ds4_status=""
    fi
  }
  [ $((tick % 10)) -eq 30 ] && {
    is_it_muted=$(pamixer --get-mute)
    vol_num=$(pamixer --get-volume) >"/tmp/volume"

    if ! [[ -f "$is_it_muted" ]]; then
      if [[ $vol_num -ge 60 ]]; then
	vol=" $nm| $al $vol_num%"
      elif [[ $vol_num -le 59 ]] && [[ $vol_num -ge 1 ]]; then
	vol=" $nm| $nm $vol_num%"
      elif [[ $volume -eq 0 ]]; then
	vol=" $nm| $wm $vol_num%"
      fi
    else
      vol=" $nm| $al $vol_num%"
    fi
  }
  [ $((tick % 5)) -eq 0 ] && {
    cpu_temp_num=$(cut -c 1-2 </sys/class/thermal/thermal_zone2/temp)

    if [[ $cpu_temp_num -le 60 ]]; then
      cpu_temp=" $nm| $nm $cpu_temp_low $cpu_temp_num°"
    elif [[ $cpu_temp_num -ge 61 && $cpu_temp_num -le 70 ]]; then
      cpu_temp=" $nm| $wn$cpu_temp_mid $cpu_temp_num°"
    else
      cpu_temp=" $nm| $al$cpu_temp_high $cpu_temp_num°"
    fi
  }
  [ $((tick % 60)) -eq 0 ] && {
    disk_usage=$(df -h | awk '{ if ($6 == "/") print $4 }')
    disk_num=${disk_usage::-1}

    if [[ $(echo "$disk_num < 20" | bc) -ne 0 ]]; then
      disk=" $nm| $wm$root_icon $disk_num""g"
    elif [[ $(echo "$disk_num < 10" | bc) -ne 0 ]]; then
      disk=" $nm| $al$root_icon $disk_num""g"
    else
      disk=" $nm| $nm$root_icon $disk_num""g"
    fi
  }
  [ $((tick % 60)) -eq 0 ] && {
    current_time="$(date "+%H:%M | %d | %a")"
    time=" $nm| $nm$date_icon $nm$current_time"
  }
  [ $((tick % 1)) -eq 0 ] && {
      cpu_usage=$(top -bn2 | grep "Cpu(s)" | awk 'NR==2 {print 100 - $8}')
      cpu_usage_int=$(printf "%.0f" "$cpu_usage")

      if [[ $cpu_usage_int -ge 80 ]]; then
	cpu=" $nm| $al$cpu_icon $cpu_usage_int%"
      elif [[ $cpu_usage_int -ge 60 ]] && [[ $cpu_usage_int -le 79 ]]; then
	cpu=" $nm| $wn$cpu_icon $cpu_usage_int%"
      else
	cpu=" $nm| $nm$cpu_icon $cpu_usage_int%"
      fi

    }
  [ $((tick % 10)) -eq 0 ] && {
      freemen_per=$(free -m | awk 'NR==2{print $3*100/$2 }')
      memory_num=$(printf "%.0f\n" "$freemen_per")
      if [[ $memory_num -ge 70 ]]; then
	memory=" $nm| $wm$ram_icon $memory_num%"
      elif [[ $memory_num -ge 50 ]] && [[ $memory_num -le 60 ]]; then
	memory=" $nm| $al$ram_icon $memory_num%"
      else
	memory=" $nm| $nm$ram_icon $memory_num%"
      fi
    }
    #...update code...
    xsetroot -name "$easyeffects$stretch$pymor$smatch$variant$climate$server$updates$ds4_status$vol$cpu_temp$cpu$memory$disk$time "
  }

trap "update;" 30
#trap "update_updates;" 31
trap "exit" SIGTERM

while true; do
  update
  tick=$((tick + 1))
  sleep $ticktime
done
