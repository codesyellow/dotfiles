#!/bin/bash
normal="^c#f8f8f2^"
normal_men="^c#e39400^"
normal_cpu="^c#b3a1e6^"
normal_root="^c#5ccc96^"
normal_home="^c#00a3cc^"
normal_date="^c#ce6f8f^"
urgent="^c#ff5555^"
alarming="^c#f1fa8c^"

ram_icon=
cpu_icon=
root_icon=
home_icon=
date_icon=

volume=$(pamixer --get-volume)
root=$(df -h | awk '{ if ($6 == "/") print $4 }')
root_int=${root::-1}
home=$(df -h | awk '{ if ($6 == "/home") print $4 }')
freemen_per=$(free -m | awk 'NR==2{print $3*100/$2 }')
freemen_per_int=$(printf "%.0f\n" "$freemen_per")
date=$(date +"%m/%d %H:%M")
cpu=$(awk '{u=$2+$4; t=$2+$4+$5; if (NR==1){u1=u; t1=t;} else print ($2+$4-u1) * 100 / (t-t1) "%"; }' \
<(grep 'cpu ' /proc/stat) <(sleep 1;grep 'cpu ' /proc/stat))
cpu_per_int=$(printf "%.0f\n" "$cpu")

status=""

if [[ $volume -ge 110 ]]; then
  status+="   $urgent|$volume% "
elif [[ $volume -le 15 && $volume -gt 0 ]]; then
  status+="   $urgent $volume% "
elif [[ $volume -eq 0 ]]; then
  status+="   $urgent|$volume% "
elif [[ $volume -ge 95 ]]; then
  status+="   $alarming|$volume% "
else
  status+="   $normal|$volume% " 
fi

if [[ $cpu_per_int -ge 80 ]]; then
  status+="$urgent$cpu_icon|$cpu_per_int% "
else
  status+="$normal_cpu$cpu_icon|$cpu_per_int% "
fi

if [[ $freemen_per_int -ge 70 ]]; then
  status+=" $urgent$ram_icon|$freemen_per_int% "
elif [[ $freemen_per_int -ge 60 ]]; then
  status+=" $alarming$ram_icon|$freemen_per_int% "
else
  status+=" $normal_men$ram_icon|$freemen_per_int% "
fi

if [[ $(echo "$root_int < 5" | bc) -ne 0 ]]; then
  echo E
  status+=" $alarming$root_icon|$root_int""g " 
elif [[ $(echo "$root_int < 2" | bc) -ne 0 ]]; then 
  status+=" $urgent$root_icon|$root_int""g " 
else
  status+=" $normal_root$root_icon|$root_int""g " 
fi

status+=" $normal_home$home_icon|$home "
status+=" $normal_date$date_icon|$date"
xprop -root -set WM_NAME "$status "
