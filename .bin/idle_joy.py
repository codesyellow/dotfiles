#!/usr/bin/env python3
import evdev
from evdev import InputDevice, categorize, ecodes, list_devices
import time
import subprocess

CONTROLLER_NAME = "Wireless Controller"
idle_time_limit = 900  # Total idle time limit (in seconds) before disconnecting
warning_idle_limit = 600  # Idle time limit (in seconds) before showing warning notification

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
    print(f'Device found: {device_path}')

    try:
        device = InputDevice(device_path)
        last_activity_time = time.time()
        warning_sent = False  # Flag to track if warning notification has been sent

        for event in device.read_loop():
            if event.type == ecodes.EV_KEY:
                last_activity_time = time.time()  # Update last activity time
                print(f'Key event detected: {categorize(event)}')
                warning_sent = False  # Reset the warning flag if activity is detected

            # Send warning notification if idle time exceeds warning_idle_limit
            if not warning_sent and time.time() - last_activity_time > warning_idle_limit:
                subprocess.run(["notify-send", "-i", "/home/cie/.local/share/icons/joystick.png","Joyley","Keep playing! I don’t want to disconnect!"])
                warning_sent = True  # Set the flag to prevent multiple notifications

            # Check if idle time has exceeded the total idle_time_limit
            if time.time() - last_activity_time > idle_time_limit:
                print("No activity for 15 minutes. Disconnecting controller...")
                subprocess.run(["notify-send", "-i", "/home/cie/.local/share/icons/joystick.png","Joyley", "Quick! Let’s play before I power d.."])
                subprocess.run(["dsbattery", "-d"])  # Run the command to disconnect
                break

    except FileNotFoundError:
        print(f'Error: Device not found at {device_path}. Please check the connection.')

    except OSError as e:
        print(f'OS error: {e.strerror}')

    except evdev.InputDeviceError:
        print(f'Error: Unable to access the input device at {device_path}.')

else:
    print(f'Error: No device found with name "{CONTROLLER_NAME}".')

