#!/bin/bash

# Search for the controller's name in the /proc/bus/input/devices file
CONTROLLER_NAME="Wireless Controller"
EVENT_HANDLE=$(grep -A 5 "$CONTROLLER_NAME" /proc/bus/input/devices | grep -Eo 'event[0-9]+' | head -n 1)

echo $EVENT_HANDLE
