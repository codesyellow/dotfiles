#!/bin/bash
hdd_icon=
disk_usage=$(df -h | awk '{ if ($6 == "/home") print $4 }')
disk_num=${disk_usage::-1}

if [[ $disk_num -le 30 ]]; then
  printf '<span size="12000" foreground="#36C2CE" rise="3000">%s</span> <span foreground="#36C2CE" rise="2000">%sG</span>' "$hdd_icon" "$disk_num"
fi