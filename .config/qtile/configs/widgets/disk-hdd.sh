#!/bin/bash
hdd_icon=
disk_usage=$(df -h | awk '{ if ($6 == "/home/digo/.HDD") print $4 }')
disk_num=${disk_usage::-1}

if [[ $disk_num -le 20 ]]; then
  output="$hdd_icon  $disk_num""G"
  printf '<span foreground="#fff">|</span> <span size="12000" foreground="#EF5A6F" rise="3000">%s</span> <span foreground="#EF5A6F" rise="2000"> %sG</span>' "$hdd_icon" "$disk_num"
fi
