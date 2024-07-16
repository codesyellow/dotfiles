#!/bin/sh
ds4=$(dsbattery)
if [[ -z $ds4 ]]; then
  false
else
  true
fi
