# PCIe Automation Test Scripts

This repository contains various Python test scripts that one can run to test their PCIe hardware components. Currently, the scripts only work on Linux-based systems, due to current dependencies (i.e., `pyudev` libray which operates using `udev`, the Linux kernal's device manager).

## Scripts

-   **PCIe Device Detection** (`detect_devices.py`): Outputs component information of PCIe devices connected to the computer