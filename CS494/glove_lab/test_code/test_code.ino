/**************

MPR global code

***************/

#include <Wire.h>
#include "Adafruit_MPR121.h"

#ifndef _BV
#define _BV(bit) (1 << (bit)) 
#endif

// You can have up to 4 on one i2c bus but one is enough for testing!
Adafruit_MPR121 cap = Adafruit_MPR121();

// Keeps track of the last pins touched
// so we know when buttons are 'released'
uint16_t lasttouched = 0;
uint16_t currtouched = 0;

/**************

Flex sensor global code

***************/

const int FLEX_PIN = A0; // Pin connected to voltage divider output

// Measure the voltage at 5V and the actual resistance of your
// 47k resistor, and enter them below:
const float VCC = 3.28; // Measured voltage of Ardunio 5V line
const float R_DIV = 143939.39; // Measured resistance of 10k resistor

// Upload the code, then try to adjust these values to more
// accurately calculate bend degree.
const float STRAIGHT_RESISTANCE = 328015.72; // resistance when straight
const float BEND_RESISTANCE = 90000.0; // resistance at 90 deg

void setup() {
  Serial.begin(115200);

  /***
  MPR set up 
  ***/
  while (!Serial) { // needed to keep leonardo/micro from starting too fast!
    delay(10);
  }
  
//  Serial.println("Adafruit MPR121 Capacitive Touch sensor test"); 
  
  // Default address is 0x5A, if tied to 3.3V its 0x5B
  // If tied to SDA its 0x5C and if SCL then 0x5D
  if (!cap.begin(0x5A)) {
//    Serial.println("MPR121 not found, check wiring?");
    while (1);
  }
//  Serial.println("MPR121 found!");

  /***
  Flex sensor set up 
  ***/
  pinMode(FLEX_PIN, INPUT);
}

void loop() {
  /***
  MPR loop code
  ***/
  
  // Get the currently touched pads
  currtouched = cap.touched();
  
  for (uint8_t i=0; i<12; i++) {
    // it if *is* touched and *wasnt* touched before, alert!
    if ((currtouched & _BV(i)) && !(lasttouched & _BV(i)) ) {
      Serial.print(i); Serial.print((" "));

      /***
      Flex sensor loop code
      ***/
      
      // Read the ADC, and calculate voltage and resistance from it
      int flexADC = analogRead(FLEX_PIN);
      float flexV = flexADC * VCC / 1023.0;
      float flexR = R_DIV * (VCC / flexV - 1.0);
      //Serial.println("Resistance: " + String(flexR) + " ohms");
    
      // Use the calculated resistance to estimate the sensor's
      // bend angle:
      float angle = map(flexR, STRAIGHT_RESISTANCE, BEND_RESISTANCE,
                       0, 90.0);
      //Serial.println("Bend: " + String(angle) + " degrees");
      Serial.println(String(angle));
    }
    // if it *was* touched and now *isnt*, alert!
    // if (!(currtouched & _BV(i)) && (lasttouched & _BV(i)) ) {
    //   Serial.print(i); Serial.println(" released");
    // }
  }

  // reset our state
  lasttouched = currtouched;

  // comment out this line for detailed data from the sensor!
  return;
  
//  // debugging info, what
//  Serial.print("\t\t\t\t\t\t\t\t\t\t\t\t\t 0x"); Serial.println(cap.touched(), HEX);
//  Serial.print("Filt: ");
//  for (uint8_t i=0; i<12; i++) {
//    Serial.print(cap.filteredData(i)); Serial.print("\t");
//  }
//  Serial.println();
//  Serial.print("Base: ");
//  for (uint8_t i=0; i<12; i++) {
//    Serial.print(cap.baselineData(i)); Serial.print("\t");
//  }
//  Serial.println();


  

}
