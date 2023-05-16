import serial
import serial.tools.list_ports as sp

# lists all ports in use
ports = sp.comports()
serialInst = serial.Serial()

# empty list of ports (strings)
portList = []

for port in ports:
    portList.append(str(port))
    print(str(port.manufacturer))

val = input("Select Port: COM")

for x in range(0, len(portList)):
    if portList[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(portList[x])

# transmission rate that we should sample the incoming data
serialInst.baudrate = 9600

# defines the port we will communicate over
serialInst.port = portVar

# opens port and listen for any incoming data
serialInst.open()

# we want to listen for incoming data until user stops flow of data in the terminal

while True:
    # if our serial instance has data in the buffer
    if serialInst.in_waiting:
        # extract the packet of data
        # reads incoming bytes of information from serial device
        packet = serialInst.readline()  # must decode

        # packet is coming in as unicode UTF-8 encoding. We must decode this to get this
        # in ASCII char representation
        print(packet.decode('utf'))
# okay, I can receive data from the arduino (the one being printed over buffer
# now I want to send things to it to have bidirectional communication

