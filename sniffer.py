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
        print('{} packets sniffed successfully.'.format(packetNumber))
        return
    except:
        sys.exit('No interface found, make sure you typed the name correctly.\n')

# Print summarized packet information
def summarizedPacket(interface, packetNumber):
    try:
        a = sniff(count = packetNumber, iface = interfaceName, prn = lambda x: x.summary())
        print(a)
        print('{} packets sniffed successfully.'.format(packetNumber))
        return
    except:
        sys.exit('No interface found, make sure you typed the name correctly.\n')

# Print packet of a specific layer
def layerPacket(interface, packetNumber, layer):
    pass

# -------------------------------------------------------------------------------------

# -----------------
#  MENU FUNCTIONS -
# -----------------

# Show main menu
def showMenu():
    print('''\nThese are the available options:
    1. Sniff all packets
    2. Sniff packets of a specific layer (data link, transportation, application)
    3. 
    4. Exit
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

# Main
if __name__ == '__main__':
    print('---Welcome to the Python Sniffer program---\n')
    
    # Ask for the interface name
    interfaceName = inputInterfaceName()

    # Main Menu
    while True:
        # Show menu options
        showMenu()

        choice = int(input('Please write the number of your desired option: '))

        # All sniffed packets
        if choice == 1:
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

        # Packets of a specific layer
        elif choice == 2:
            print("Hello")

        # Finalize program
        elif choice == 4:
            print('Thanks for using the program! Have a good day/night (^-^)')
            sys.exit()

        else:
            print('Not a valid option \n')