#include "Wire.h"
#include <MPU6050_light.h>

MPU6050 mpu(Wire);

//values to remember what acceleration was in the previous loop
//might just be unused honestly
float lastX;
float lastY;
float lastZ;

//value to remember total steps
int numSteps;

int cadence = 0;

//alias FSR pins and initialize values to 0
int medialForeFootPin = 0;
int medialFootPin = 1;
int heelPin = 2;
int lateralMidFootPin = 3;

int medialForeFoot = 0;
int medialFoot = 0;
int heel = 0;
int lateralMidFoot = 0;

//flags to be used to detect a step 
bool toeOff = false;
bool heelStrike = false;

//keeps track of time
long timer = 0;

void setup()
{
    Wire.begin();
    mpu.calcOffsets(true,true);

    //initializing acceleration values
    // lastX = mpu.getAccX();
    // lastY = mpu.getAccY();
    // lastZ = mpu.getAccZ();

    numSteps = 0;

    //initialize FSR pins
    medialForeFoot = analogRead(medialForeFootPin);
    medialFoot = analogRead(medialFootPin);
    heel = analogRead(heelPin);
    lateralMidFoot = analogRead(lateralMidFootPin);
}

void loop()
{

}

//return a boolean based on if the user is currently in motion or not
bool ifAccelerating()
{
    mpu.update();
    if(mpu.getAccX() != 0 || mpu.getAccY() != 0 || mpu.getAccZ() != 0) //non-zero acceleration means change in position
        return true;
    else
        return false;
}

//adds to the step counter after a step is detected
void incrementSteps()
{
    if(_detectStep())
        //increment steps by 2 since there's only one sole but a cycle would be 2 steps
        //unfortunate innate problem is that if you step off with the FSR foot, the counter will always be off by 1
        numSteps = numSteps + 2;
}

//detects steps based on a toe off into heel strike cycle
bool _detectStep()
{
    if(!toeOff && !heelStrike)
        medicalForeFoot = analogRead(medialForeFootPin);
        heel = analogRead(heelPin);
        
        if(!toeOff)
            if(medicalForeFoot > 10 && heel < 10)
                toeOff = true;
        
        if(!heelStrike)
            if(medicalForeFoot < 10 && heel > 10)
                heelStrike = true;

        return false;
    else
        //reset flags and return that a step has been completed
        toeOff = false;
        heelStrike = false;
        return true; 
}

//stores how many steps taken in a 2 minute period to cadence 
//takes difference of current time found from millis() and timer to tell when 2 minutes is up
//startTime and startStepCount should be initialized by an event
void findCadence(const long& startTime, const int& startStepCount)
{
    if((millis() - startTime) >= 120000)
        cadence = (numSteps - startStepCount);
}