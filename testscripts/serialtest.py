
import serial


ser = serial.Serial('/dev/tty96B0', 9600)
shake = 0

while True:

    if shake == 0:
        if ser.in_waiting > 0:
            line = ser.readline()
            line2 = line.decode('ASCII')
            line2 = line2.strip('\n')
            line2 = line2.strip('\r')
            line2 = line2.split(",")
            print(line2)
            line2 = [float(i) for i in line2]
            print(line2)
            shake = 1

    if shake == 1:
        ser.write(2)
        shake = 0
        print("sent shake")
