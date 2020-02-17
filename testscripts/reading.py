import serial

ser = serial.Serial('/dev/tty96B0', 9600)
while 1:
    if(ser.in_waiting >0):
        line = ser.readline()
        line2 = line.decode('ASCII')
        line2 = line2.strip('\n')
        line2 = line2.strip('\r')
        line2 = line2.split(",")
        line2 = [float(i) for i in line2]

        print(line2)
