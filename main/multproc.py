import time
from threading import *
from tkinter import *

import pygame
import pyttsx3
import serial

#параметры окна для музыки
pygame.init()


#параметры pyserial
cam='COM11'
ser = serial.Serial(cam, 9600)
time.sleep(2)
ser.reset_input_buffer()
def first():
    # параметры окна в tkinter
    root = Tk()
    root.title("   ")
    frameCnt = 12
    frames = [PhotoImage(file='kot.gif', format='gif -index %i' % (i)) for i in range(frameCnt)]
    def update(ind):
        frame = frames[ind]
        ind += 1
        if ind == frameCnt:
            ind = 0
        label.configure(image=frame)
        root.after(100, update, ind)
    # запуск эмоции
    label = Label(root)
    label.pack()
    root.after(0, update, 0)
    root.mainloop()

def second():
    # запуск дефолт подсветки
    ser.write(b'N')
    # time.sleep(20)

    voise = pyttsx3.init()
    pygame.mixer.music.load('meaow.mp3')
    pygame.mixer.music.play()
    time.sleep(2)
    pygame.mixer.music.stop()
    voise.say("Может включить музыку?")
    voise.runAndWait()
    time.sleep(6)

    # включается музыка
    pygame.mixer.music.load('REPEAT.mp3')
    pygame.mixer.music.play()
    time.sleep(20)
    pygame.mixer.music.stop()

    pygame.mixer.music.stop()
    voise.say("Может закажем пиццу?")
    voise.runAndWait()
th1 = Thread(target=first)
th2 = Thread(target=second)

th1.start()
th2.start()

