# Group 11: Step 1
# Reference:
#   Edureka.co "How to Implement Snake Game in Python?": https://www.edureka.co/blog/snake-game-with-pygame/

import pygame
import random
from pynput.keyboard import Key, Controller, Listener
import serial
import threading

keyboard = Controller()
ser = serial.Serial('COM3', 115200)

# Initialize the game and background
pygame.init()
bg = pygame.image.load("jb-50.jpg")
bg_1 = pygame.image.load("CHILL!.jpg")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 50)

# Display Info
displayWidth = 600
displayHeight = 600
display = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('Group 11 Lab 4 Snake Game')

# Changes in x and y coordinates
_x = 0
_y = 0

# Miscellaneous variables
timer = pygame.time.Clock()
font = pygame.font.SysFont("bahnschrift", 25)
hotSnakeBod = 10
speed = 10


# Increase the snake size
def grow(hotSnakeBod, snakeBody):
    for i in snakeBody:
        pygame.draw.rect(display, black, [i[0], i[1], hotSnakeBod, hotSnakeBod])


# Randomize the food's location
def randomize(x_coor, y_coor):
    x_coor = round(random.randrange(0, displayWidth - hotSnakeBod) / 10.0) * 10.0
    y_coor = round(random.randrange(0, displayHeight - hotSnakeBod) / 10.0) * 10.0
    return x_coor, y_coor


# Display a given message
def message(msg, color, x1, y1):
    msg = font.render(msg, True, color)
    display.blit(msg, [x1, y1])

def runSerial():
    print("SerialRUNNING")
    while True:
        try:
            ser_bytes = ser.readline()
            decoded_bytes = float(ser_bytes[0:len(ser_bytes) - 2].decode("utf-8"))
            print(decoded_bytes)

            # Serial to Key Mappings
            # 0 - up
            # 1 - down
            # 2 - left
            # 3 - right

            # Conditionals, Probably better to use switch statements in the future
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
            print("Keyboard Interrupt")
            # break

# Check what type of input the user provides
def key_check(_input):
    if   _input.key == pygame.K_UP:
        _x = 0
        _y = -hotSnakeBod
    elif _input.key == pygame.K_DOWN:
        _x = 0
        _y = hotSnakeBod
    elif _input.key == pygame.K_LEFT:
        _x = -hotSnakeBod
        _y = 0
    elif _input.key == pygame.K_RIGHT:
        _x = hotSnakeBod
        _y = 0
    return _x, _y

sOn = False

# Main Game Loop
def snake():
    global sOn
    if not(sOn):
        t = threading.Thread(target=runSerial)
        t.start()
        sOn = True

    end = False
    close = False
    x = displayWidth/2
    y = displayHeight/2
    _x = 0
    _y = 0

    # define the initial snake
    snakeBody = []
    snakeSize = 1

    # food location
    comeda_x = round(random.randrange(0, displayWidth - hotSnakeBod) / 10.0) * 10.0
    comeda_y = round(random.randrange(0, displayHeight - hotSnakeBod) / 10.0) * 10.0


    while not end:
        while close:

            display.blit(bg_1, (0, 0))
            # message("Loser. For further embarrassment, press any key to continue. "
            #         "Press X to save yourself the humiliation.", black)
            message("Loser!", black, 430, 200)
            message("Press UP to Continue", red, 350, 250)
            message("DOWN to Quit", black, 425, 300)
            pygame.display.update()

            # Check if the user will continue or end
            for touch in pygame.event.get():
                if touch.type == pygame.KEYDOWN:
                    if touch.key == pygame.K_DOWN:
                        end = True
                        close = False

                    else:
                        snake()

        # Determine the direction
        for touch in pygame.event.get():
            if touch.type == pygame.QUIT:
                end = True
            elif touch.type == pygame.KEYDOWN:
                _x, _y = key_check(touch)

        # Snake hits the boundaries
        if x >= displayWidth or x < 0 or y >= displayHeight or y < 0:
            close = True

        x += _x
        y += _y
        display.blit(bg, (0, 0))
        pygame.draw.rect(display, (0, 255, 0), [comeda_x, comeda_y, hotSnakeBod, hotSnakeBod])
        s_head = [x, y]
        snakeBody.append(s_head)
        if len(snakeBody) > snakeSize:
            del snakeBody[0]
        for i in snakeBody[:-1]:
            if i == s_head:
                close = True

        grow(hotSnakeBod, snakeBody)
        pygame.display.update()

        if x == comeda_x and y == comeda_y:
            comeda_x, comeda_y = randomize(comeda_x, comeda_y)
            snakeSize += 1

        timer.tick(speed)

    t.raise_exception()
    pygame.quit()


snake()
