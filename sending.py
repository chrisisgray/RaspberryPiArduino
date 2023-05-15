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

# any function that reads information via serial assumes data is in utf-8, so
# you will have to convert it
while True:
    command = input("Arduino Command: ")
    serialInst.write(command.encode('utf-8'))

    if command == 'exit':
        exit()

    while not serialInst.in_waiting:
        pass

    if serialInst.in_waiting:
        packet = serialInst.readline()
        print(packet.decode('utf'))
