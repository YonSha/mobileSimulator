class Device:
    def __init__(self, device_name, ip_address):
        self.device_name = device_name
        self.ip_address = ip_address
        self.online = True  # Simulating online status

    def __str__(self):
        return f"Device: {self.device_name}, IP: {self.ip_address}, Online: {self.online}"

    def set_status(self, status) -> None:
        self.online = status



