"""
detect_pci_devices.py

"""

import pyudev


def detect_pci_devices(devices: pyudev.Enumerator) -> None:
    """
    Prints information about PCI/PCIe devices currently connected to the
    computer

    Args:
        devices (pyudev.Enumerator): Filtered iterable containing devices
    """
    for device in devices:
        device_info = {
            "id": device.get("PCI_ID"),
            "manufacturer": device.get("ID_VENDOR_FROM_DATABASE"),
            "model": device.get("ID_MODEL_FROM_DATABASE"),
            "driver": device.driver,
            "path": device.device_path,
        }
        print("#" * 50)
        print("PCI/PCIe Device Info:")
        print("-" * 50)
        print("ID: ", device_info["id"])
        print("Manufacturer: ", device_info["manufacturer"])
        print("Model: ", device_info["model"])
        print("Path: ", device_info["path"])


if __name__ == "__main__":
    context = pyudev.Context()
    pci_devices = context.list_devices(subsystem="pci")
    detect_pci_devices(pci_devices)
