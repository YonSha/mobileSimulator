from scapy.all import sniff, send, IP, UDP, TCP, ICMP, RandShort
import threading



class NetworkHandler:
    def __init__(self):
        self.packet_count = 0
        self.sniff_thread = None
        self.stop_sniffing_event = threading.Event()  # Event to signal stopping

    def send_packet(self, sender_device, target_device, target_port, payload, protocol='UDP'):
        # Create an IP packet
        ip = IP(src=sender_device.ip_address, dst=target_device.ip_address)

        # Select protocol
        if protocol.upper() == 'UDP':
            packet = ip / UDP(sport=RandShort(), dport=target_port) / payload
        elif protocol.upper() == 'TCP':
            packet = ip / TCP(sport=RandShort(), dport=target_port) / payload
        elif protocol.upper() == 'ICMP':
            packet = ip / ICMP() / payload
        else:
            print("Unsupported protocol.")
            return

        # Send the packet
        send(packet, verbose=0)
        self.packet_count += 1
        print(
            f"Sent {protocol} packet from {sender_device.device_name} to {target_device.device_name} on port {target_port}. Total packets sent: {self.packet_count}.")

    def sniff_packets(self, sender_devices):
        def packet_handler(packet):
            # Print only the packets that originate from the sender devices
            if IP in packet and packet[IP].src in [device.ip_address for device in sender_devices]:
                print(f"Captured Outgoing Packet: {packet.summary()}")

        print("Starting packet sniffing...")
        sender_ips = [device.ip_address for device in sender_devices]
        filter_string = " or ".join([f"src host {ip}" for ip in sender_ips])

        # Sniff only outgoing packets
        sniff(prn=packet_handler, filter=filter_string, store=0,
              stop_filter=lambda x: self.stop_sniffing_event.is_set())

    def run(self, sender_devices, target_devices, target_port, payload, protocol='UDP'):
        # Start sniffing in a separate thread
        sniff_thread = threading.Thread(target=self.sniff_packets, args=(sender_devices,))
        sniff_thread.daemon = True
        sniff_thread.start()

        # Send packets from each sender device to each target device
        for target_device in target_devices:
            for sender_device in sender_devices:
                self.send_packet(sender_device, target_device, target_port, payload, protocol)


    def stop_sniffing(self):
        self.stop_sniffing_event.set()  # Signal the sniffing thread to stop
        if self.sniff_thread is not None:
            self.sniff_thread.join()  # Wait for the thread to finish
            print("Stopped packet sniffing.")

    def reset_sniffing(self, sender_devices):
        self.stop_sniffing()  # Stop current sniffing
        self.start_sniffing(sender_devices)  # Start a new sniffing thread

    def start_sniffing(self, sender_devices):
        # Start sniffing in a separate thread
        self.stop_sniffing_event.clear()  # Reset the event
        self.sniff_thread = threading.Thread(target=self.sniff_packets, args=(sender_devices,))
        self.sniff_thread.daemon = True
        self.sniff_thread.start()