#!/usr/bin/env python
import subprocess
import time

MY_DEVICE = "RX8M804971Y"


class Phone():
    def __init__(self) -> None:
        self.state = False

    def share_android(self) -> None:
        """Share the android screen"""
        subprocess.run([
            "scrcpy"
        ])

    def get_device(self) -> str:
        """Get the device and return it"""
        device = subprocess.check_output([
            "adb", "devices",
        ]).decode("utf-8")

        return device

    def is_device_connected(self) -> bool:
        """Get the devices and return they ID"""
        device = subprocess.check_output([
            "adb", "devices",
        ]).decode("utf-8")
        if MY_DEVICE in device:
            return True
        else:
            return False

    def is_authorized(self) -> bool:
        """Check if the device is is_authorized and return true or false"""
        if "unauthorized" in self.get_device():
            return False
        else:
            return True

    def run(self) -> None:
        """Run a loop"""
        while True:
            if self.is_device_connected() and self.is_authorized() and self.state == False:
                self.state = True
                self.share_android()
            else:
                self.state = False

            time.sleep(2)


if __name__ == "__main__":
    phone = Phone()
    phone.run()
