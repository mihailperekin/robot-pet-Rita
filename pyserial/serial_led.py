# Робот славик лента Pyserial на малинке


import time

import serial

cam='COM3'
ser = serial.Serial(cam, 9600)
time.sleep(2)
ser.reset_input_buffer()
while True:
        text = input("Ваш настрой(злюсь бешенный норма вп нз вправо лев): ")
        if text == "норма":
            ser.write(b'N')
        if text == "злюсь":
            ser.write(b'Z')
        if text == "бешенный":
            ser.write(b'B')
        if text == "влево":
            ser.write(b'C')
        if text == "вправо":
            ser.write(b'D')
        if text == "назад":
            ser.write(b'E')
        if text == "вперед":
            ser.write(b'F')

        if text == "стоп":
            ser.write(b'S')

        if text == "хватит":
            ser.write(b'S')
            break
        if text == "да":
            ser.write(b'R')
