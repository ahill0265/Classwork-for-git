#BIOE/CS494 LAB 4 Group 11 Code

#Imports
from pynput.keyboard import Key, Controller, Listener
import serial
import time #We will probably use this library in the future

#change COM port your arduino is in (Check Arduino app)
ser = serial.Serial('COM3', 115200)
#Enables us to output to computer
keyboard = Controller()
#Cleans up input from serial
ser.flushInput()

while True:

    try:
        #Reads output of arduino
        ser_bytes = ser.readline()
        #Converts bytes to values we can use
        decoded_bytes = float(ser_bytes[0:len(ser_bytes) - 2].decode("utf-8"))
        print(decoded_bytes)

        # Serial to Key Mappings
        # 0 - up
        # 1 - down
        # 2 - left
        # 3 - right

        #Conditionals, Probably better to use switch statements in the future
        if decoded_bytes == 0:
            keyboard.press(Key.up)
            keyboard.release(Key.up)
            print("Up Key was Pressed")
        elif decoded_bytes == 1:
            keyboard.press(Key.down)
            keyboard.release(Key.down)
            print("Down Key was Pressed")
        elif decoded_bytes == 2:
            keyboard.press(Key.left)
            keyboard.release(Key.left)
            print("Left Key was Pressed")
        elif decoded_bytes == 3:
            keyboard.press(Key.right)
            keyboard.release(Key.right)
            print("Right Key was Pressed")

    except:
        print("Some Error!?!?!")