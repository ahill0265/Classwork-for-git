# This is code for the leg lift exercise backend
# it will be called after the gui code.

# in this exercise the user must do a 30 second hold
# a timer will count down the 30 seconds

# if the user bends their knee too much, the count down will stop
# they must straighten their knee to continue the countdown

import time

#Variables
duration = 0
holdDuration = 30 #[Seconds]
lastTime = 0

# bend - current bend of the flex sensor
# minBend - min value of bend from calibration ~ value knee can be most bended
# tolerance - how far from min and max will we count a rep.
def lift(bend, minBend, tolerance):
    global lastTime, holdDuration, duration

    while duration <= 30: # while there is still time left
        if bend <= minBend + tolerance: # if the leg is straight, continue counting down
            duration = duration + (time.perf_counter() - lastTime) # from the squatexercise
            setLast()
            
        print(30 - duration) # display the countdown

#Function to set last time to current time (reused a lot)
def setLast():
    global lastTime
    lastTime = time.perf_counter()


lift(5, 10, 5)
