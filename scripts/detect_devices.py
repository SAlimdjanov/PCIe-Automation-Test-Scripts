"""
detect_devices.py

NOTE: For debugging purposes

"""

import pyudev


def detect_pci_devices(devices: pyudev.Enumerator) -> None:
    """
    Prints information about all devices currently connected to the computer

    Args:
        devices (pyudev.Enumerator): Filtered iterable containing devices
    """
    for device in devices:
        device_info = {
            "manufacturer": device.get("ID_VENDOR_FROM_DATABASE"),
            "model": device.get("ID_MODEL_FROM_DATABASE"),
            "driver": device.driver,
            "path": device.device_path,
        }
        print("#" * 50)
        print("Device Information:")
        print("-" * 50)
        print("Manufacturer: ", device_info["manufacturer"])
        print("Model: ", device_info["model"])
        print("Path: ", device_info["path"])


if __name__ == "__main__":
    context = pyudev.Context()
    all_devices = context.list_devices()
    detect_pci_devices(all_devices)
