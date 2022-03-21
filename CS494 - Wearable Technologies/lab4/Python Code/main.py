# BIOE/CS494 LAB 4 Group 11 Code

# Imports
from pynput.keyboard import Key, Controller, Listener
import serial
import time  # We will probably use this library in the future
from tkinter import *
import threading

# change COM port your arduino is in (Check Arduino app)
# ser = serial.Serial('COM3', 115200)
# Enables us to output to computer
keyboard = Controller()
# Cleans up input from serial
# ser.flushInput()

# Python program to implement Morse Code Translator

''' 
VARIABLE KEY 
'cipher' -> 'stores the morse translated form of the english string' 
'decipher' -> 'stores the english translated form of the morse string' 
'citext' -> 'stores morse code of a single character' 
'i' -> 'keeps count of the spaces between morse characters' 
'message' -> 'stores the string to be encoded or decoded' 
'''

# Dictionary representing the morse code chart
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':

            # Looks up the dictionary and adds the
            # correspponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '

    return cipher


def decrypt(message):
    # extra space added at the end to access the
    # last morse code
    message += ' '

    decipher = ''
    citext = ''
    for letter in message:

        # checks for space
        if (letter != ' '):

            # counter to keep track of space
            i = 0

            # storing morse code of a single character
            citext += letter

            # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1

            # if i = 2 that indicates a new word
            if i == 2:

                # adding space to separate words
                decipher += ' '
            else:

                # accessing the keys using their values (reverse of encryption)
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                                                              .values()).index(citext)]
                citext = ''

    return decipher


###################################

root = Tk()
canvas = Canvas(root, width=700, height=700)
canvas.pack()
img = PhotoImage(file="lab4_morsecode.png")
canvas.create_image(20, 20, anchor=NW, image=img)


def inputCode():
    message = input("Type some morse code: ")
    result = decrypt(message)
    print(result)


####################################

def tkLoop():
    root.mainloop()


# Hard-coded driver function to run the program
def main():
    t1 = threading.Thread(target=tkLoop)
    t2 = threading.Thread(target=inputCode)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


# Executes the main function
if __name__ == '__main__':
    main()

# while True:
#
#     try:
#         #Reads output of arduino
#         ser_bytes = ser.readline()
#         #Converts bytes to values we can use
#         decoded_bytes = float(ser_bytes[0:len(ser_bytes) - 2].decode("utf-8"))
#         print(decoded_bytes)
#
#         # Serial to Key Mappings
#         # 0 - up
#         # 1 - down
#         # 2 - left
#         # 3 - right
#
#         #Conditionals, Probably better to use switch statements in the future
#         if decoded_bytes == 0:
#             keyboard.press(Key.up)
#             keyboard.release(Key.up)
#             print("Up Key was Pressed")
#         elif decoded_bytes == 1:
#             keyboard.press(Key.down)
#             keyboard.release(Key.down)
#             print("Down Key was Pressed")
#         elif decoded_bytes == 2:
#             keyboard.press(Key.left)
#             keyboard.release(Key.left)
#             print("Left Key was Pressed")
#         elif decoded_bytes == 3:
#             keyboard.press(Key.right)
#             keyboard.release(Key.right)
#             print("Right Key was Pressed")
#
#     except:
#         print("Some Error!?!?!")
