import serial
import time

arduino = serial.Serial(port='/dev/cu.wchusbserial1420', baudrate=9600)

while True:
    arduino.write(bytes("test", encoding='utf-8'))
    time.sleep(2)