#!/usr/bin/env bash

keychord_active=$(cat /tmp/keychord_active)

if [[ -z $keychord_active ]]; then
  echo 0
else
  echo 1
fi
