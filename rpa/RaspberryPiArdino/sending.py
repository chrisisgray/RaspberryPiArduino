import serial
import serial.tools.list_ports as sp

# lists all ports in use
ports = sp.comports()
serialInst = serial.Serial()

# I do not need to store ALL ports. I am just looking for Arduino's

name = "Arduino"
for port in ports:
    if name in str(port.manufacturer):
        serialInst.port = port.device

serialInst.baudrate = 9600
serialInst.open()

# any function that reads information via serial assumes data is in utf-8, so
# you will have to convert it
while True:

    try:
        if serialInst.in_waiting:
            packet = serialInst.readline()
            print(packet.decode())

            item = int(packet.decode('utf-8').strip('\r\n'))

            if item < 50:
                command = "on".encode('utf-8')
                # print(command)
                serialInst.write(command)
            else:
                command = "off".encode('utf-8')
                # print(command)
                serialInst.write(command)
    except:
        print("failed to read value")
        continue
