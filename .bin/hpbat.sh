#!/bin/bash

# Get the list of Bluetooth devices
bluetoothctl devices | cut -f2 -d' ' | while read uuid; do
  # Get the device info
  info=$(bluetoothctl info "$uuid")

  # Check if the device name is KTP-100
  if echo "$info" | grep -q "Name: KTP-100"; then
    # Extract the connection status
    connected=$(echo "$info" | grep "Connected" | awk '{print $2}')

    # Check if the device is connected
    if [ "$connected" = "yes" ]; then
      echo "KTP-100 is connected."
    else
      echo "KTP-100 is not connected."
    fi
  fi
done
