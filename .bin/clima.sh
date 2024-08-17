#!/usr/bin/env bash
climate=$(curl -s "wttr.in/SaoVicente?format=%t" | grep -oP '\d+')

if [[ -n $climate ]]; then
  echo $climate >"/tmp/climate"
else
  echo "climate not found"
fi
