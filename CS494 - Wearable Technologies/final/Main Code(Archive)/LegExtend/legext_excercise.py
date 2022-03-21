#Leg Extensions

import time

repcount = 0
isBent = False #False is extended default, True is bent

#it's really just reading if you have bent or not
def extRep(currentBend, startingBend, targetBend):
    global isBent

    if isBent:
        if currentBend >= targetBend:
            switchState()
    else:
        if currentBend <= startingBend:
            switchState()

#switches if you're considered bending or extending and then increments reps if you've completed a cycle
def switchState():
    global isBent

    if isBent:
        incrementReps()

    isBent = not isBent

def incrementReps():
    global repcount
    repcount += 1