from base_classes.device import Device
from handlers.controller import Controller
from handlers.network_handler import NetworkHandler


# TODO
# 1. Add Multiprocess/Multi threaded with asyncio?
# 2. Add docker implementation
# 3. Test with fiddler/wireshark over the lan
# 4. Test with high volume
# 5. Add comments
# 6. Add config file
# 7. Add utils (read from conf..etc..)
# 8. Add results validation - What do we expect from the test?
# 9. remove redundant sniffing (the routing through the local computer) to see cleaner results.


if __name__ == "__main__":
    # Define devices
    device1 = Device("Device1", "192.168.1.5")
    device2 = Device("Device2", "192.168.1.10")

    co = Controller()
    co.build_devices(5)

    dev = co.return_all_devices

    sender = NetworkHandler()

    #UDP
    #sender.run(sender_devices=dev, target_devices=[device1], target_port=12345, payload="Hello UDP", protocol='UDP')

    # Sending TCP
    sender.run(sender_devices=dev, target_devices=[device1], target_port=80, payload="Hello TCP", protocol='TCP')

    # Sending ICMP
    #sender.run(sender_devices=[device1], target_devices=[device1], target_port=None, payload="Hello ICMP", protocol='ICMP')
