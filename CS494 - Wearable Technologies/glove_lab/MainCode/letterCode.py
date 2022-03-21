capsLock = False

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

def switchTest(flex, tuckCal, restCal, extendedCal):
    # print(str(flex))
    # print(str(tuckCal))
    # print(str(extendedCal))
    # print(type(flex))
    # print(type(tuckCal))
    # print(type(extendedCal))
    if flex <= tuckCal + 5:
        return 0
    elif flex <= extendedCal - 5:
        return 9
    else:
        return 18

def getLetter(userInput, flex, tuckCal, restCal, extendedCal):
    base = 96

    if capsLock:
        caps = -32
    else:
        caps = 0
    print("getting letter")
    floor = switchTest(flex, tuckCal, restCal, extendedCal)
    print(str(floor))
    # userInput += 1

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

    print(getLetter(testInput, testFlex))


if __name__ == "__main__":
    main()
