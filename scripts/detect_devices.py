"""
detect_devices.py

"""

import pyudev


def detect_pcie_devices() -> None:
    """
    Detect PCIe devices currently connected to the computer
    """
    context = pyudev.Context()
    devices = context.list_devices(subsystem="pci")

    for device in devices:
        device_info = {
            "id": device.get("PCI_ID"),
            "type": device.device_type,
            "manufacturer": device.get("ID_VENDOR_FROM_DATABASE"),
            "model": device.get("ID_MODEL_FROM_DATABASE"),
            "driver": device.driver,
            "path": device.device_path,
            "node": device.device_node,
            "links": device.device_links,
        }
        print("#" * 50)
        print("PCI/PCIe Device Info:")
        print("-" * 50)
        print("ID: ", device_info["id"])
        print("Type:", device_info["type"])
        print("Manufacturer: ", device_info["manufacturer"])
        print("Model: ", device_info["model"])
        print("Path: ", device_info["path"])
        print("Node: ", device_info["node"])
        print("Links:", device_info["links"])
        print("-" * 50)


if __name__ == "__main__":
    detect_pcie_devices()
