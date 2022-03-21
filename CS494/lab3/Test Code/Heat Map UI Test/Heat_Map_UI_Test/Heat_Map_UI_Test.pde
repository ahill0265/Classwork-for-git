/* Team 11
* Template Code for easy UI testing 
* Processing Reference: https://processing.org/reference/
* References: 
*        * Background Image: https://processing.org/examples/backgroundimage.html
*/

import processing.serial.*;

PImage f_map;
float a = 0.0;
float s = 0.0;

// Buttons
boolean stepRecordButton = false;
String stepText = "Record Steps";
int sRSP[] = {50, 50, 225, 80};

boolean gaitRecordButton = false;
String gaitText = "Walk (30 Sec)";
int gRSP[] = {50, 320, 225, 80};

boolean interestingRecBtn = false;
String intrText = "Cool stuff ahead";
int iRSP[] = {50, 700, 300, 80};

// Gait Variables
String gaitType = "Normal";
int stepCount = 0;
float cadenceC = 0.0;
int lastMil = 0;


/**************************/
/********* Set up *********/

void setup() {
  size(1000, 1000);
  f_map = loadImage("foot-1000.jpg");
}

/***** End of Set up *****/
/*************************/


/*************************/
/********* Draw **********/

void draw() {
  
  update(mouseX, mouseY);
  
  background(f_map);
  btnPlacement();
  
  /* just here to change the size 
     a is used for the sizing
     TODO: replace with FSR values
           - depending on how large the values are, 
             divide the values by something to make 
             them fit on the foot */
  if (stepRecordButton){
    if (a >= 80.0) {
      while (a >= 0.0)
        a = a - 1.5;
    }
    else if (a <= 0.0) a = a + 1.5;
    else               a = a + 1.5;
    
    if (millis() - lastMil >= 1000){
      stepCount++;
      lastMil = millis();
    }
  }
  
  if (gaitRecordButton){
    println("gait button active");
    
  }
    
  cadenceStep();
  heatMap();
}

/****** End of Draw ******/
/*************************/



/********************************/
/******** Step/Gait Info ********/

void cadenceStep(){
  
  // Cadence/Step Count Info
  fill(0, 102, 153);
  textSize(30);
  text("Cadence: " + (cadenceC/(random(1,3))), 50, 200);
  text("Step Count: " + stepCount, 50, 250);
  
  // Gait Info
  text("Gait Type: ", 50, 450);
  fill(255,0,0);
  text(gaitType, 230, 450);
  
}

/**** End of Step/Gait Info *****/
/********************************/




/*******************/
/**** Heat Map *****/

void heatMap(){
  
  // toe
  fill(255, 0, 0);
  ellipse(635, 370, a, a);
  
  // inner portion of the foot 
  fill(0, 255, 0);
  ellipse(690, 470, a, a);
  
  // outer portion of the foot
  fill (0, 0, 255);
  ellipse(800, 470, a, a);
  
  // heel
  fill(200, 0, 200);
  ellipse(740, 720, a, a);
  
}

/* End of Heat Map */
/*******************/
  
  

/********************/
/* Button Functions */
  
// sets the button
void button(int SP[], String buttonText, int textSize, int textColor, boolean isSelected, int highlightColor, int baseColor) {
  //Creates a rectangle shaped button
  //SP are arrays of size and position of the button

  if(isSelected){ //highlights if selected or not
    fill(highlightColor);
  } else {
    fill(baseColor);
  }
  rect(SP[0], SP[1], SP[2], SP[3]);

  //button text
  textSize(textSize);
  //textAlign(CENTER);
  fill(textColor);
  text(buttonText,75,SP[1]+3*SP[3]/4);
}


// Places buttons in the UI
void btnPlacement(){
  
  button(sRSP, stepText, 30, 255, stepRecordButton, #808080, #006699);
  button(gRSP, gaitText, 30, 255, gaitRecordButton, #808080, #006699);
  button(iRSP, intrText, 30, 255, interestingRecBtn, #808080, #006699);
}


//Button Finder
void update(int x, int y) {
  
  // Record Steps button detection
  if ( overRect(sRSP[0],sRSP[1],sRSP[2],sRSP[3]) && stepRecordButton == false) {
    stepRecordButton = true;
    gaitRecordButton = false;
    interestingRecBtn = false;
  }
  else if ( overRect(sRSP[0],sRSP[1],sRSP[2],sRSP[3]) && stepRecordButton == true) {
    stepRecordButton = false;
    gaitRecordButton = false;
    interestingRecBtn = false;
  }
  
  // Walk Cycle & Gait button detection
  else if ( overRect(gRSP[0],gRSP[1],gRSP[2],gRSP[3]) && gaitRecordButton == false) {
    stepRecordButton = false;
    gaitRecordButton = true;
    interestingRecBtn = false;
  }
  else if ( overRect(gRSP[0],gRSP[1],gRSP[2],gRSP[3]) && gaitRecordButton == true) {
    stepRecordButton = false;
    gaitRecordButton = false;
    interestingRecBtn = false;
  }
}

/***** Action when button is pressed *****/
void mousePressed() {
  
  if (stepRecordButton)
    println("step pressed");
    
  else if (gaitRecordButton) 
    println("gait pressed");
  
}

// Get Mouse location
boolean overRect(int x, int y, int width, int height)  {
  if (mouseX >= x && mouseX <= x+width &&
      mouseY >= y && mouseY <= y+height) {
    return true;
  } else {
    return false;
  }
}

/* End of Button Functions */
/**************************/
