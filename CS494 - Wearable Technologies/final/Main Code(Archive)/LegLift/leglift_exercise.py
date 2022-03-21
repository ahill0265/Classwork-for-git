# This is code for the leg lift exercise backend
# it will be called after the gui code.

# in this exercise the user must do a 30 second hold
# a timer will count down the 30 seconds

# if the user bends their knee too much, the count down will stop
# they must straighten their knee to continue the countdown

import time

#Variables
lastTime = 0
duration = 0
repCount = 0
#Paramaters (Variables that you want to tweak)
holdDuration = 30 #[Seconds]

# bend - current bend of the flex sensor
# maxBend - max value of bend from calibration ~ max value knee is straightened
# minBend - min value of bend from calibration ~ value knee can be most bended
# tolerance - how far from min and max will we count a rep.
# state - what part of the exercise is being done
def liftRep(bend, maxBend, minBend, tolerance, state):
    global lastTime, holdDuration, duration, repCount

    duration = duration + (time.perf_counter() - lastTime) # from the squatexercise

    while holdDuration >= 0: # while in the hold
        if bend <= minBend + tolerance:
            # if the leg is bent, the duration stays the same
            print("")
            ## this if statement can be removed i just have it for my thoughts
        else: # if the leg is straight, continue counting down
            holdDuration = holdDuration - 1

        print(holdDuration) # display the countdown
            

#Function to set last time to current time (reused a lot)
def setLast():
    global lastTime
    lastTime = time.perf_counter()

#Function to grab # of reps for the GUI
def getReps():
    global lastTime
    return repCount


