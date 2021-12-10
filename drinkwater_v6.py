#very bad python code, don't use it
from pynput.keyboard import Key, Controller

import time

def water():

    keyboard = Controller()
    time.sleep(3)

    for char in "11223": #walking
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(.12) #emulate human like presses

        time.sleep(3)

    for char in "32211": #phrase 2
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(.15) #emulate human like presses

        time.sleep(9)

    for char in "112": #phrase 2
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(.17) #emulate human like presses

    time.sleep(18)

water()

#x = 1
#while True:
#    water()
#    x += 1
