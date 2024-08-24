#!/bin/bash

while true; do
  echo $(dsbattery) >/tmp/ds4
  sleep 10
done
