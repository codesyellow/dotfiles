#!/bin/bash
hdd_icon=
disk_usage=$(df -h | awk '{ if ($6 == "/") print $4 }')
disk_num=$(printf "%.0f" "$(echo "${disk_usage::-1}" | bc)")

if [[ $disk_num -le 10 ]]; then
  printf '<span size="x-large" foreground="#fff">|</span> <span size="12000" foreground="#EF5A6F" rise="4000">%s</span> <span foreground="#EF5A6F" rise="3500"> %sG</span>' "$hdd_icon" "$disk_num"
fi
