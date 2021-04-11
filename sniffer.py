from scapy.all import * # Sniffing functions
import sys              # Safely terminating the program

# ------------------------------------------------------

# ---------------------
#  SNIFFING FUNCTIONS -
# ---------------------

# Print ALL information about a packet
def detailedPacket(packetNumber):
    a = sniff(count = packetNumber, iface = 'enp0s3', prn = lambda x: x.show())
    print(a)
    return

# Print summarized packet information
def summarizedPacket(packetNumber):
    a = sniff(count = packetNumber, iface = 'enp0s3', prn = lambda x: x.summary())
    print(a)
    return

# Print packet of a specific layer
def layerPacket(layer):
    pass

# ------------------------------------------------------

# -----------------
#  MENU FUNCTIONS -
# -----------------

# Show main menu
def showMenu():
    print('''Welcome to the Python Sniffer program. These are the available options:
    1. Show all packets
    2. Show packets of a specific layer (data link, transportation, application)
    3. 
    4. Exit
    ''')
    return

# Handling positive integer input
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

# ------------------------------------------------------

# Main
if __name__ == '__main__':
    # Main Menu
    while True:
        # Show menu options
        showMenu()

        choice = int(input('Please write the number of your desired option: \n'))

        # All sniffed packets
        if choice == 1:
            while True:
                choice = input('Do you want to see all the information about each packet? (y,n) \n')
                # All the information
                if choice in {'y', 'Y', 'yes', 'Yes'}:
                    choice = input('The current default packet number is 100, would you like to change it? (y,n) \n')
                    if choice in {'y', 'Y', 'yes', 'Yes'}:
                        packetNumber = integerInput('Enter the amount of packets to be sniffed \n') 
                        detailedPacket(packetNumber)
                    else:
                        packetNumber = 100
                        detailedPacket(packetNumber)
                    break
                # Summarized information
                elif choice in {'n', 'N', 'no', 'No'}:
                    summarizedPacket(100)
                    break
                # Invalid option handling
                else:
                    print('Invalid option\n')

        # Packets of a specific layer
        elif choice == 2:
            print("Hello")

        # Finalize program
        elif choice == 4:
            sys.exit()

        else:
            print('Not a valid option \n')