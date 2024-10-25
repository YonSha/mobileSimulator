from base_classes.device import Device


class DevicesHandler:

    def __init__(self):
        self.devices = []
        self.base_ip = "192.168.1."

    def add_device(self, device_name, ip_address) -> Device:
        self.devices.append(Device(device_name, ip_address))
        print(f"Added: {device_name}")
        return Device(device_name, ip_address)

    def build_devices(self, num_devices) -> None:
        for i in range(1, num_devices + 1):
            ip_address = f"{self.base_ip}{i}"
            device_name = f"Device{i}"
            self.add_device(device_name, ip_address)

    def get_all_devices_status(self) -> None:
        for device in self.devices:
            print(device)

    @property
    def return_all_devices(self):
        return self.devices

    def auto_build_devices(self, device_configs):
        devices = []
        for name, ip in device_configs.items():
            devices.append(Device(name, ip))
        return devices
