#!/bin/bash
normal="^c#f8f8f2^"
normal_men="^c#e39400^"
normal_cpu="^c#b3a1e6^"
normal_root="^c#5ccc96^"
normal_home="^c#00a3cc^"
normal_date="^c#ce6f8f^"
low_temp="^c#4793AF^"
mid_temp="^c#FFC470^"
high_temp="^c#DD5746^"
urgent="^c#ff5555^"
early_hour="^c#FFF5E0^"
afternoon_hour="^c#8DECB4^"
night_hour="^c#41B06E^"
alarming="^c#f1fa8c^"
hour_colored=""

ram_icon=
cpu_icon=
root_icon=
home_icon=
date_icon=
cpu_temp_low= 
cpu_temp_mid= 
cpu_temp_high= 

volume=$(pamixer --get-volume)
cputemp=$(cat /sys/class/thermal/thermal_zone2/temp | cut -c 1-2)
root=$(df -h | awk '{ if ($6 == "/") print $4 }')
root_int=${root::-1}
#home=$(df -h | awk '{ if ($6 == "/home") print $4 }')
freemen_per=$(free -m | awk 'NR==2{print $3*100/$2 }')
freemen_per_int=$(printf "%.0f\n" "$freemen_per")
date=$(date +"%m[%d]")
hour=$(date +"%H:%M")
cpu=$(awk '{u=$2+$4; t=$2+$4+$5; if (NR==1){u1=u; t1=t;} else print ($2+$4-u1) * 100 / (t-t1) "%"; }' \
<(grep 'cpu ' /proc/stat) <(sleep 1;grep 'cpu ' /proc/stat))
cpu_per_int=$(printf "%.0f\n" "$cpu")

status=""

if [[ $volume -ge 55 ]]; then
  status+="   $urgent $volume %"
elif [[ $volume -le 20 && $volume -gt 0 ]]; then
  status+="   $urgent$volume % "
elif [[ $volume -eq 0 ]]; then
  status+="   $urgent$volume % "
elif [[ $volume -ge 50 ]]; then
  status+="   $alarming $volume % "
else
  status+="   $normal $volume % " 
fi

if [[ $cputemp -le 40 ]]; then
  status+=" $low_temp$cpu_temp_low $cputemp °"
elif [[ $cputemp -ge 41 && $cputemp -le 60 ]]; then
  status+=" $mid_temp$cpu_temp_mid $cputemp °"
else
  status+=" $high_temp$cpu_temp_high $cputemp b°"
fi

if [[ $cpu_per_int -ge 80 ]]; then
  status+=" $urgent$cpu_icon $cpu_per_int % "
else
  status+=" $normal_cpu$cpu_icon $cpu_per_int % "
fi

if [[ $freemen_per_int -ge 70 ]]; then
  status+=" $urgent$ram_icon $freemen_per_int % "
elif [[ $freemen_per_int -ge 60 ]]; then
  status+=" $alarming$ram_icon $freemen_per_int % "
else
  status+=" $normal_men$ram_icon $freemen_per_int % "
fi

if [[ $hour -le "12:00" ]]; then
    hour_colored+="$early_hour$hour"
elif [[ $hour -ge "12:01" && $hour -le "18:00" ]]; then
    hour_colored+="$afternoon_hour$hour"
else
    hour_colored+="$night_hour$hour"
fi

if [[ $(echo "$root_int < 5" | bc) -ne 0 ]]; then
  echo E
  status+=" $alarming$root_icon $root_int""g" 
elif [[ $(echo "$root_int < 2" | bc) -ne 0 ]]; then 
  status+=" $urgent$root_icon $root_int""g" 
else
  status+=" $normal_root$root_icon $root_int""g" 
fi

status+=" $normal_date$date_icon $date $hour_colored"
xprop -root -set WM_NAME "$status"
