# This is code for the squat exercise backend, will be called/alter the gui code.

import time

#Variables
lastTime = 0
duration = 0
repCount = 0
#Paramaters (Variables that you want to tweak)
holdDuration = 0 #[Seconds]

# bend - current bend of the flex sensor
# maxBend - max value of bend from calibration ~ max value knee is straightened
# minBend - min value of bend from calibration ~ value knee can be most bended
# tolerance - how far from min and max will we count a rep.
# state - what part of the exercise is being done
#TODO: Same as squat lol
def stepUpRep(bend, maxBend, minBend, tolerance, state):
    global lastTime, holdDuration, duration, repCount
    # print(bend)
    # print(maxBend)
    # print(minBend)
    # print(tolerance)
    # print(state)
    if state == 0: #Step down
        if maxBend - tolerance <= bend: #requirement to complete state
            setLast() #sets time that
            return 1 #Returns value of next state
        else:
            return state
    elif state == 1: #Hold squat position
        if maxBend - tolerance <= bend:
            duration = duration + (time.perf_counter() - lastTime) #Counts how long you are in the hold position
            setLast()
        if duration >= holdDuration:
            duration = 0
            return 2 #Returns value of next state
        else:
            return state
    elif state == 2: #Squat up
        if minBend + tolerance >= bend:
            setLast()
            return 3
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

#Function to grab # of reps for the GUI
def getReps():
    return repCount

def getDuration():
    return holdDuration - duration

def zeroReps():
    global repCount
    repCount = 0
    # print(repCount)

def setDuration(dur):
    global holdDuration
    holdDuration = dur
