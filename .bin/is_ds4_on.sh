#!/bin/sh
ds4=$(cat /tmp/ds4_status)
if [[ -z $ds4 ]]; then
  exit 0
elif [[ $ds4 == 'false' ]]; then
  exit 1
else
  exit 0
fi
