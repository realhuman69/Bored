from scapy.all import ARP, Ether, srp
import ipaddress

def scan_network(network):
    # Create an ARP request packet
    arp = ARP(pdst=network)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    # Send the packet and receive the response
    result = srp(packet, timeout=2, verbose=False)[0]

    # Create a list to hold discovered devices
    devices = []

    for sent, received in result:
        # Append each discovered device to the list
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

def main():
    # Get the network address from user input
    network_input = input("Enter the network address (e.g., 192.168.1.0/24): ")

    try:
        # Validate and create an IP network object
        network = ipaddress.ip_network(network_input, strict=False)
    except ValueError:
        print("Invalid network address. Please try again.")
        return

    print(f"Scanning network: {network}")
    devices = scan_network(str(network))

    # Print the discovered devices
    print("\nDiscovered Devices:")
    print("IP Address\t\tMAC Address")
    print("------------------------------------------")
    for device in devices:
        print(f"{device['ip']}\t\t{device['mac']}")

if __name__ == "__main__":
    main()
