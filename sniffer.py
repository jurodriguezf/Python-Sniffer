"""Code by Julio Rodriguez
"""

from scapy.all import * # Sniffing functions
import sys              # Safely terminating the program

# -------------------------------------------------------------------------------------

# ---------------------
#  SNIFFING FUNCTIONS -
# ---------------------

# Print ALL information about a packet
def detailedPacket(interface, packetNumber):
    try:
        a = sniff(count = packetNumber, iface = interfaceName, prn = lambda x: x.show())
        print(a)
        return
    except:
        sys.exit('No interface found, make sure you typed the name correctly.\n')

# Print summarized packet information
def summarizedPacket(interface, packetNumber):
    try:
        a = sniff(count = packetNumber, iface = interfaceName, prn = lambda x: x.summary())
        print(a)
        return
    except:
        sys.exit('No interface found, make sure you typed the name correctly.\n')

# Print ALL info of packet of a specific protocol
def detailedProtocolPacket(interface, packetNumber, protocol):
    try:
        a = sniff(filter = protocol, count = packetNumber, iface = interfaceName, prn = lambda x: x.show())
        print(a)
        return
    except:
        sys.exit('No interface found, make sure you typed the name correctly.\n')

# Print summarized info of packet of a specific protocol
def summarizedProtocolPacket(interface, packetNumber, protocol):
    try:
        a = sniff(filter = protocol, count = packetNumber, iface = interfaceName, prn = lambda x: x.summary())
        print(a)
        return
    except:
        sys.exit('Unexpected error. Make sure the protocol is compatible with your network interface.\n')

# -------------------------------------------------------------------------------------

# -----------------
#  MENU FUNCTIONS -
# -----------------

# Show main menu
def showMenu():
    print('''\nThese are the available options:
    1. Sniff all packets (any protocol)
    2. Sniff packets of a specific protocol
    3. Exit
    ''')
    return

# Ask for the network interface name
def inputInterfaceName():
    while True:
        interfaceName = input('Please type the network interface name (Linux command "ip link show"): ')
        choice = input('The network interface name is "{}", is that correct? (y/n): '.format(interfaceName))
        if choice in {'y', 'Y', 'yes', 'Yes'}:
            return interfaceName
        else:
            continue

# Handle positive integer input
def integerInput(message):
    while True:
        try:
            val = int(input(message))
            if val <= 0:
                print('Number MUST be positive')
            else:
                return val
        except ValueError:
            print('Not a valid option\n')

# -------------------------------------------------------------------------------------

# -----------------
#  MAIN FUNCTIONS -
# -----------------

def sniffedPackets():
    while True:
        choice = input('\nDo you want to see all the information about each packet? (y,n): ')
        # All the information
        if choice in {'y', 'Y', 'yes', 'Yes'}:
            choice = input('\nThe current default packet number is 100, would you like to change it? (y,n): ')
            if choice in {'y', 'Y', 'yes', 'Yes'}:
                packetNumber = integerInput('Enter the amount of packets to be sniffed: ')
                detailedPacket(interfaceName, packetNumber)
            else:
                packetNumber = 100
                detailedPacket(interfaceName, packetNumber)
            break
        # Summarized information
        elif choice in {'n', 'N', 'no', 'No'}:
            choice = input('\nThe current default packet number is 100, would you like to change it? (y,n): ')
            if choice in {'y', 'Y', 'yes', 'Yes'}:
                packetNumber = integerInput('Enter the amount of packets to be sniffed: ')
                summarizedPacket(interfaceName, packetNumber)
            else:
                packetNumber = 100
                summarizedPacket(interfaceName, packetNumber)
            break
        # Invalid option
        else:
            print('Invalid option\n')

def protocolPackets():
    while True:
        print('''\nSupported protocols:
        Ethernet (ether)
        Wireless LAN (wlan)
        Internet protocol (ip)
        IPv6 (ip6)
        Address Resolution Protocol (arp)
        Reverse ARP (rarp)
        Transmission Control Protocol (tcp)
        User Datagram Protocol (udp)
        Internet Control Message Protocol (icmp)
        ''')

        protocol = input('Enter the desired protocol to be filtered: ')

        if protocol not in {'ether', 'wlan', 'ip', 'ip6', 'arp', 'rarp', 'tcp', 'udp', 'icmp'}:
            print('Invalid protocol\n')
            continue
        else:
            choice = input('\nDo you want to see all the information about each packet? (y,n): ')
            # All the information
            if choice in {'y', 'Y', 'yes', 'Yes'}:
                choice = input('\nThe current default packet number is 100, would you like to change it? (y,n): ')
                if choice in {'y', 'Y', 'yes', 'Yes'}:
                    packetNumber = integerInput('Enter the amount of packets to be sniffed: ')
                    detailedProtocolPacket(interfaceName, packetNumber, protocol)
                else:
                    packetNumber = 100
                    detailedProtocolPacket(interfaceName, packetNumber, protocol)
                break
            # Summarized information
            elif choice in {'n', 'N', 'no', 'No'}:
                choice = input('\nThe current default packet number is 100, would you like to change it? (y,n): ')
                if choice in {'y', 'Y', 'yes', 'Yes'}:
                    packetNumber = integerInput('Enter the amount of packets to be sniffed: ')
                    summarizedProtocolPacket(interfaceName, packetNumber, protocol)
                else:
                    packetNumber = 100
                    summarizedProtocolPacket(interfaceName, packetNumber, protocol)
                break
            # Invalid option
            else:
                print('Invalid option\n')

def menuLoop():
    # Main Menu
    while True:
        # Show menu options
        showMenu()

        choice = int(input('Please write the number of your desired option: '))

        # All sniffed packets
        if choice == 1:
            sniffedPackets()

        # Packets of a specific protocol
        elif choice == 2:
            protocolPackets()

        # Finalize program
        elif choice == 3:
            print('Thanks for using the program! Have a good day/night (^-^)')
            sys.exit()

        else:
            print('Not a valid option \n')

# Main
if __name__ == '__main__':
    # Welcome happy message :)
    print('---Welcome to the Python Sniffer program---\n')
    
    # Ask for the interface name
    interfaceName = inputInterfaceName()

    # Loop through the menu
    menuLoop()