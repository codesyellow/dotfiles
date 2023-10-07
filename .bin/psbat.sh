#!/bin/bash

text=$(dsbattery)
result=$(echo "$text" | grep -o '[0-9]*%')
printf '%s' "$result"

