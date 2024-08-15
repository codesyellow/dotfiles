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

    for event in dev.read_loop():
        if event.type == ecodes.EV_KEY:
            timestamp = time.strftime("%H:%M:%S", time.localtime())
            with open(log_file, "w") as f:  # Open file in write mode to overwrite
                f.write(timestamp)
else:
    print(f"Device with name '{CONTROLLER_NAME}' not found.")
