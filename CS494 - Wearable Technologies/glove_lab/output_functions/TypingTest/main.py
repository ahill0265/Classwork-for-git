capsLock = False

from pynput.keyboard import Key, Controller, Listener
import serial
import time  # We will probably use this library in the future

# change COM port your arduino is in (Check Arduino app)
ser = serial.Serial('COM3', 115200)
# Enables us to output to computer
keyboard = Controller()
# Cleans up input from serial
ser.flushInput()


#
# while True:
#     try:
#         serialData = ser.readline()
#         serialSplit = serialData.split(" ")
#
#         userInput = int(serialSplit[0])
#         print(userInput)
#         flex = float(serialData[1])
#         print(flex)
#
#         base = 96
#
#         if capsLock:
#             caps = -32
#         else:
#             caps = 0
#
#         #debugging
#
#
#         print(chr(base + caps + userInput))
#
#     except:
#         print("Some Error!?!?!")

def switchTest(flex):
    if flex <= -20:
        return 0
    elif -20 < flex <= 20:
        return 9
    elif 20 < flex:
        return 18


def getLetter(userInput, flex):
    base = 96

    if capsLock:
        caps = -32
    else:
        caps = 0

    floor = switchTest(flex)
    userInput += 1

    return chr(base + caps + floor + userInput)


def setCaps():
    global capsLock

    if capsLock:
        capsLock = False
    else:
        capsLock = True


def main():
    testInput = 0
    testFlex = 0
    #
    # print(getLetter(testInput, testFlex))

    while True:
        try:
            serialData = ser.readline()
            serialData = serialData.decode('utf-8')
            print(serialData)
            serialSplit = serialData.split(' , ')

            userInput = int(serialSplit[0])
            flex = float(serialSplit[1])

            print(getLetter(userInput, flex))

        except:
            print('error')


if __name__ == "__main__":
    main()
