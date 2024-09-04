#!/bin/bash

if [[ "$1" == "server" ]]; then
  if [[ -f "/tmp/dustbowl_count" ]] || [[ -f "/tmp/badwater_count" ]] || [[ -f "/tmp/turbine_count" ]]; then
    exit 0
  else
    exit 1
  fi
fi

echo " | "
