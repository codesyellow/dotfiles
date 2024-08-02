#!/bin/sh
ds4=$(cat /tmp/ds4_status)
if [[ -z $ds4 ]]; then
  false
elif [[ $ds4 == 'false' ]]; then
  false
else
  true
fi
