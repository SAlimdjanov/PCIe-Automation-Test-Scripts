"""
traverse_connection_tree.py

"""

import pyudev


class DeviceConnectionTree:
    """A utility class for gathering and displaying parent and child
    connections of PCI/PCIe devices.

    Attributes:
        pci_devices (pyudev.Enumerator): An enumerator containing PCI/PCIe
        devices.
    """

    def __init__(self, devices: pyudev.Enumerator) -> None:
        self.pci_devices = devices

    def _get_model_id(self, device: pyudev.Device) -> str:
        """Get the model ID of a given device

        Args:
            device (pyudev.Device): Device object

        Returns:
            str: Model ID string
        """
        return device.get("ID_MODEL_FROM_DATABASE")

    def _obtain_nodes(
        self, device: pyudev.Device, nodes: pyudev.Enumerator
    ) -> list[str]:
        """Traverses down the connection list and obtains a list of connected
        nodes

        Args:
            device (pyudev.Device): The main device whose connections are being
            obtained
            nodes (pyudev.Enumerator): Enumerator object containing all
            parent/child nodes

        Returns:
            list[str]: List of model IDs for all parent/child nodes of a given
             device
        """
        result = []
        visited = set()
        device_id = self._get_model_id(device)
        device_path = device.device_path
        for node in nodes:
            node_id = self._get_model_id(node)
            node_path = node.device_path
            if (
                node_id != device_id
                and node_path != device_path
                and ((node_id not in visited) and (node_path not in visited))
            ):
                if node_id is None:
                    result.append(node_path)
                    visited.add(node_path)
                else:
                    result.append(node_id)
                    visited.add(node_id)
        return result

    def _print_nodes(self, name: str, nodes: list[str]) -> None:
        """Print the parent/child nodes

        Args:
            name (str): "Parents" or "Children"
            nodes (list[str]): list containing parent/children nodes
        """
        print(name + ":")
        if nodes:
            for device in nodes:
                print(device)
        else:
            print("NONE")

    def print_connections(self, device_connections: dict) -> None:
        """Prints each PCI/PCIe related device, all parent/children nodes to
        the terminal"""
        for key, value in device_connections.items():
            print("#" * 50)
            print("Component:", key)
            print("-" * 50)
            self._print_nodes("Parents", value["parents"])
            print("-" * 50)
            self._print_nodes("Children", value["children"])
            print()

    def display_connection_tree(self) -> None:
        """Gathers and groups parent and child connections of all PCI/PCIe
        devices intalled on the system"""
        device_links = {}
        for device in self.pci_devices:
            device_id = self._get_model_id(device)
            device_links[device_id] = {
                "parents": self._obtain_nodes(device, device.ancestors),
                "children": self._obtain_nodes(device, device.children),
            }
        self.print_connections(device_links)


if __name__ == "__main__":
    context = pyudev.Context()
    pci_devices = context.list_devices(subsystem="pci")
    connections = DeviceConnectionTree(pci_devices)
    connections.display_connection_tree()
