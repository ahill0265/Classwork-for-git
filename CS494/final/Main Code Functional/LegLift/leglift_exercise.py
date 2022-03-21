# This is code for the leg lift exercise backend
# it will be called after the gui code.

# in this exercise the user must do a 30 second hold
# a timer will count down the 30 seconds

# if the user bends their knee too much, the count down will stop
# they must straighten their knee to continue the countdown

import time

#Variables
duration = 0
holdDuration = 0 #[Seconds]
lastTime = 0
repCount = 0

# bend - current bend of the flex sensor
# minBend - min value of bend from calibration ~ value knee can be most bended
# tolerance - how far from min and max will we count a rep.
def lift(bend, minBend, tolerance, cap, state):
    global lastTime, holdDuration, duration, repCount

    if state == 0 : #Press button to start
        if cap == "0": #requirement to complete state
            setLast() #sets time that
            return 1 #Returns value of next state
        else:
            return state
    elif state == 1: #Hold leg position
        if bend <= minBend + tolerance:  # if the leg is straight, continue counting down
            duration = duration + (time.perf_counter() - lastTime)  # from the squatexercise
            setLast()
            # print(30 - duration) # display the countdown
        if duration >= holdDuration:
            duration = 0
            return 2 #Returns value of next state
        else:
            return state
    elif state == 2: #Squat up
        if cap == "0": #requirement to complete state
            setLast() #sets time that
            return 3 #Returns value of next state
        else:
            return state
    elif state == 3: #Hold up stance
        if minBend + tolerance >= bend:
            duration = duration + (time.perf_counter() - lastTime)
            setLast()
        if duration >= holdDuration:
            duration = 0
            repCount = repCount + 1
            return 0 #Returns value of next state
        else:
            return state

#Function to set last time to current time (reused a lot)
def setLast():
    global lastTime
    lastTime = time.perf_counter()

def getReps():
    return repCount

def zeroReps():
    global repCount
    repCount = 0
    # print(repCount)

def getDuration():
    return holdDuration - duration

def setDuration(dur):
    global holdDuration
    holdDuration = dur