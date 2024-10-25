from handlers.devices_handler import DevicesHandler


class Controller( DevicesHandler):

    def __init__(self):
        super().__init__()



    def return_active_device(self, identifier):
        for device in self.return_all_devices:
            if device.device_name == identifier or device.ip_address == identifier:
                print(device)
                return device
        print(f"Device with identifier '{identifier}' not found.")
        return None
