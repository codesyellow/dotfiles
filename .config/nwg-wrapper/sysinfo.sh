#!/usr/bin/env bash

COLOR_TITLE="#88c0d0" 
COLOR_TEXT="#eceff4"  

TIME=$(date "+%a, %d %b - %H:%M")
CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')"%"
MEM_USED=$(free -h | awk '/Mem:/ { print $3 }')
MEM_TOTAL=$(free -h | awk '/Mem:/ { print $2 }')
ROOT_USE=$(df -h / | awk 'NR==2 {print $5}')
HOME_USE=$(df -h /home | awk 'NR==2 {print $5}')
HDD_PATH="$HOME/.HDD"

if [ -d "$HDD_PATH" ]; then
  HDD_USE=$(df -h "$HDD_PATH" | awk 'NR==2 {print $5}')
else
  HDD_USE="n/a"
fi

OUTPUT=$(cat <<EOF
<span font_family='Victor Mono' font_weight='bold' font_style='italic' size='large'>
<span foreground='$COLOR_TITLE'> time:</span> <span foreground='$COLOR_TEXT'>$TIME</span>

<span foreground='$COLOR_TITLE'> cpu:</span>  <span foreground='$COLOR_TEXT'>$CPU_USAGE</span>
<span foreground='$COLOR_TITLE'> ram:</span>  <span foreground='$COLOR_TEXT'>$MEM_USED / $MEM_TOTAL</span>

<span foreground='$COLOR_TITLE'> disk usage</span>
<span foreground='$COLOR_TEXT'>  root (/)  : $ROOT_USE</span>
<span foreground='$COLOR_TEXT'>  home (~)  : $HOME_USE</span>
<span foreground='$COLOR_TEXT'>  hdd (~/)  : $HDD_USE</span>
</span>
EOF
)

echo "$OUTPUT" | tr '[:upper:]' '[:lower:]'
