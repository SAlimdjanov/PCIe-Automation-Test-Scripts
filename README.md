# PCI/PCIe Automation Test Scripts

This repository contains various Python test scripts that one can run to test their PCIe hardware components. Currently, the scripts only work on Linux-based systems, due to current dependencies (i.e., `pyudev` libray which operates using `udev`, the Linux kernal's device manager).

## Scripts

**Device Detector** (`detect_devices.py`): Outputs information about all hardware components in the system. This was mainly written to debug other scripts.

**PCI/PCIe Device Detection** (`detect_pci_devices.py`): Outputs component information of PCI and PCIe devices connected to the computer. For example, here's information about my GPU and my CPU's host bridge:

![detected-devices-sample](/screenshots/detected_devices_sample.png)

**PCI/PCIe Device Connection Tree Traverser** (`pci_device_tree.py`): For each PCI/PCIe device, the script first traverses up until it reaches its root component. Then, it traverses down all connected devices. These are outputted as parent and children nodes, respectively. Here's my GPU for example:

![gpu-connections](/screenshots/gpu_connections.png)

It shows that the GPU is connected to PCIe controller, then to the root PCI bridge (root complex). It's children nodes are rendering devices and I2C communication devices.