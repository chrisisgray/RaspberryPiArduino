import serial
import serial.tools.list_ports as sp

# lists all ports in use
ports = sp.comports()
serialInst = serial.Serial()

# I do not need to store ALL ports. I am just looking for Arduino's

name = "Arduino"
for port in ports:
    if name in port.description:
        serialInst.port = port.device
        serialInst.baudrate = 9600
        serialInst.open()


while True:
    # if our serial instance has data in the buffer
    if serialInst.in_waiting:
        # extract the packet of data
        # reads incoming bytes of information from serial device
        packet = serialInst.readline()  # must decode

        # packet is coming in as unicode UTF-8 encoding. We must decode this to get this
        # in ASCII char representation
        print(packet.decode('utf'))