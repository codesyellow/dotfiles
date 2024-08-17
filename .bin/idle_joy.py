#!/usr/bin/env python3
import evdev
from evdev import InputDevice, ecodes, list_devices
import time

CONTROLLER_NAME = "Wireless Controller"

# Find the correct device path
def find_device_path(controller_name):
    devices = [InputDevice(path) for path in list_devices()]
    for device in devices:
        if controller_name in device.name:
            return device.path
    return None

# Get the device path for the controller
device_path = find_device_path(CONTROLLER_NAME)

if device_path:
    dev = InputDevice(device_path)
    log_file = "/tmp/ds4_logger"
    last_timestamp = None

    for event in dev.read_loop():
        if event.type == ecodes.EV_KEY:
            timestamp = time.strftime("%H:%M:%S", time.localtime())
            if timestamp != last_timestamp:  # Only write if the timestamp is different
                with open(log_file, "w") as f:
                    f.write(timestamp)
                last_timestamp = timestamp
        time.sleep(0.05)  # Add a small delay to reduce CPU usage
else:
    print(f"Device with name '{CONTROLLER_NAME}' not found.")
