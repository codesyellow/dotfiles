#!/usr/bin/env bash

checkupdates=$(checkupdates | wc -l)

if [[ $checkupdates -le 20 ]]; then
  echo "$checkupdates" >/tmp/updates
elif [[ $checkupdates -ge 21 ]] && [[ $checkupdates -le 40 ]]; then
  echo "$checkupdates" >/tmp/updates
  echo "warning" >/tmp/updates_status
else
  echo "$checkupdates" >/tmp/updates
  echo "alert" >/tmp/updates_status
fi
