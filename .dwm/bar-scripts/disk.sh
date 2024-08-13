#!/usr/bin/env bash
while true; do
  root=$(df -h | awk '{ if ($6 == "/") print $4 }')
  root_int=${root::-1}

  echo "$root_int" >/tmp/disk
  sleep 30
done
