import serial
ser = serial.Serial('/dev/ttyAMA0',115200)
print(ser.isOpen())
ser.write(b"a")