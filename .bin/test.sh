#!/bin/bash

dbus-monitor --system "type='signal',interface='org.freedesktop.login1.Session'" |
  while read -r line; do
    if echo "$line" | grep -q "Unlock"; then
      # Run your command here
      echo "Unlocked at $(date)" >>~/.unlock.log
      echo "oi"
    fi
  done
