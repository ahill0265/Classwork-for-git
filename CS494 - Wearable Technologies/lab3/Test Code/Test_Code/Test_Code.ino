/******************************************************************************
Team 11 Lab 2 Arduino Sample Code
3/2/2021
******************************************************************************/

#include "Wire.h"
#include <MPU6050_light.h>

MPU6050 mpu(Wire);

//Global Variables
int serialOutInterval = 100;

int redPin = 3;
int yellowPin = 5;
int greenPin = 6;
int bluePin = 9;

int mFFPin = 0;
int mFPin = 1;
int heelPin = 2;
int lMFPin = 3;

int mFF = 0;
int mF = 0;
int heel = 0;
int lMF = 0;
int mFFOffset = 0;
int mFOffset = 0;
int heelOffset = 0;
int lMFOffset = 0;

long timer = 0;

void setup() {
  //prinModes
  pinMode(redPin, OUTPUT);
  pinMode(yellowPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);

  //Startup Sequence
  digitalWrite(bluePin, HIGH); 
  delay(250);            
  digitalWrite(greenPin, HIGH);
  digitalWrite(bluePin, LOW);  
  delay(250); 
  digitalWrite(yellowPin, HIGH);
  digitalWrite(greenPin, LOW);  
  delay(250); 
  digitalWrite(redPin, HIGH);
  digitalWrite(yellowPin, LOW);  
  delay(250); 
  
  digitalWrite(redPin, LOW);

  Serial.begin(115200);
  Wire.begin();
  
  byte status = mpu.begin();
//<<<<<<< Updated upstream
  Serial.print(F("MPU6050 status: "));
  Serial.println(status);
  //while(status!=0){ } // stop everything if could not connect to MPU6050
  
  Serial.println(F("Calculating offsets, do not move MPU6050"));
//=======
//  while(status!=0){ } // stop everything if could not connect to MPU6050
////>>>>>>> Stashed changes
  delay(2000);
  mpu.calcOffsets(true,true); // gyro and accelero
  

  mFFOffset = analogRead(mFFPin);
  mFOffset = analogRead(mFPin);
  heelOffset = analogRead(heelPin);
  lMFOffset = analogRead(lMFPin);
  
}

void loop() {
  mpu.update();
  mFF = analogRead(mFFPin) - mFFOffset; 
  mF = analogRead(mFPin) - mFOffset;
  heel = analogRead(heelPin) - heelOffset;
  lMF = analogRead(lMFPin) - lMFOffset;

  lightUp(mFF, bluePin);
  lightUp(mF, greenPin);
  lightUp(heel, yellowPin);
  lightUp(lMF, redPin);
  
  if(millis() - timer > serialOutInterval){ // print data every second
    Serial.print(mpu.getAccX());
    Serial.print(",");
    Serial.print(mpu.getAccY());
    Serial.print(",");    
    Serial.print(mpu.getAccZ());
    Serial.print(",");
    
    Serial.print(mFF, DEC);
    Serial.print(",");
    Serial.print(mF, DEC);
    Serial.print(",");
    Serial.print(heel, DEC);
    Serial.print(",");
    Serial.println(lMF, DEC);
    
    timer = millis();
  }

}

void lightUp(int FSR, int LED){
  analogWrite(LED, FSR/4);
}
