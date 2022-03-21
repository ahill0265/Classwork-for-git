/* Team 11
* Template Code for easy UI testing
* Processing Reference: https://processing.org/reference/
* References:
*        * Background Image: https://processing.org/examples/backgroundimage.html
*/

import processing.serial.*;
Serial myPort;        // The serial port


PImage f_map;
PImage i_map;
float a = 0.0;
float s = 0.0;

//UI Stuff
int state = 0;

//Input Variables
float accX = 0;
float accY = 0;
float accZ = 0;
boolean moveX = false;
boolean moveY = false;
boolean moveZ = false;
float lastAccX = 0.0;
float lastAccY = 0.0;
float lastAccZ = 0.0;

boolean movedRight   = false;
boolean movedLeft    = false;
boolean movedForward = false;
boolean movedBack    = false;

int mFF = 0;
int mF = 0;
int heel = 0;
int lMF = 0;

float MFSum = 0;
float MFFSum = 0;
float LMFSum = 0;
float HeelSum = 0;

String stepLength = "";
boolean lengthLock = false;
char lastKey;

// Buttons
boolean homeButton = false;
String homeText = "Home";
int hBSP[] = {898, 2, 100, 58}; //home button position and size

boolean stepRecordButton = false;
String stepText = "Record Steps";
int sRSP[] = {80, 500, 300, 80};

boolean stepResetButton = false;
int sRRSTSP[] = {390, 500, 80, 80};

boolean motionDetectionButton = false;
String motionDetectionText = "Detect Motion";
int mDSP[] = {0, 920, 333, 80};

boolean gaitRecordButton = false;
String gaitText = "Gait Analysis";
int gRSP[] = {333, 920, 333, 80};

boolean normalGait = false;
String normalGaitText = "Normal Gait";
int nGSP[] = {20, 100, 200, 80};

boolean inToeingButton = false;
String inToeingText = "In-Toeing";
int iTSP[] = {20, 190, 200, 80};

boolean outToeingButton = false;
String outToeingText = "Out-Toeing";
int oTSP[] = {20, 280, 200, 80};

boolean tipToeingButton = false;
String tipToeingText = "Tiptoeing";
int tTSP[] = {20, 370, 200, 80};

boolean heelButton = false;
String heelText = "Heel Walk";
int hSP[] = {20, 460, 200, 80};

//Timers
int timeInt = 100; //interval to counting time
timerC stepRecord = new timerC(120000);
timerC normalGaitRecord = new timerC(30000);
timerC inToeingRecord = new timerC(30000);
timerC outToeingRecord = new timerC(30000);
timerC tipToeingRecord = new timerC(30000);
timerC heelRecord = new timerC(30000);

// Section 3
String motion = "No Motion";

// Section 4
boolean intrBtn = false;
String intrText = "Let's move!";
int iRSP[] = {666, 920, 333, 80};
    // section 4 movement commands
String iRText = "MOVE RIGHT";
int iRRec[] = {500, 500, 400, 100};


// Gait Variables
String gaitType = "Normal";
int pThresh = 3;
int stepCount = 0;
float cadenceC = 0.0;
int lastMil = 0;
int lastState = 0;
int stepState = 0;
String lastProfile = "Nothing";

//During Midstance
float normalGaitMFP = 71.4;
float inToeingMFP = 70.05;
float outToeingMFP = 73.7;
float tipToeingMFP = 69.4;
float heelMFP = 67.8;

//float normalGaitMFP = 51.9;
//float inToeingMFP = 48.8;
//float outToeingMFP = 55.6;
//float tipToeingMFP = 57.9;
//float heelMFP = 0.8;


float lastDirection = 0;

//value to remember total steps
int numSteps = 0;
float cadence = 0;

//flags to be used to detect a step
boolean toeOff = false;
boolean heelStrike = false;

//keeps track of time
long timer = 0;
/******/

// Heat Map Variables
int mFFR = 0;
int mFR = 0;
int heelR = 0;
int lMFR = 0;


/**************************/
/********* Set up *********/

void setup() {
  size(1000, 1000);
  f_map = loadImage("foot-1000.jpg");
  i_map = loadImage("intrStage.jpeg");

  myPort = new Serial(this, "COM3", 115200); // Open whatever port is the one you're using.
  myPort.bufferUntil('\n'); // don't generate a serialEvent() unless you get a newline character:
}

/***** End of Set up *****/
/*************************/


/*************************/
/********* Draw **********/

void draw() {
  update(mouseX, mouseY); //important for mouse usability



  currentWindow();

  if (millis() - lastMil >= 1000){
    stepCount++;
    lastMil = millis();
  }
  topBar();

}
/**** End of Draw *****/
/********************************/


/*******************/
/* Current Window */
void currentWindow(){
  switch(state){
    case 0: // Main Window
      heatMap();
      home();
    break;

    case 1: // Motion Detection
      heatMap();
      motionDetection();
      break;

    case 2: // Gait Analysis
      heatMap();
      gaitAnalysis();
      break;

    case 3: // Interesting Impl
      intrStage();
      break;
  }
}
/**** End of Current Window *****/
/********************************/

/*******************/
/* Top Bar */
// Display the top bar of the UI
void topBar() {
  fill(0, 102, 153); //change color depending on if age and baseline are good ready (ADD)
  rect(0, 0, width, height/16);
  button(hBSP, homeText, 32, #006699, homeButton, #808080, 255);

  fill(255);
  textSize(40);
  textAlign(LEFT);

  //Display which mode you're on.
  String mode = "";
  switch(state){
    case 0: //Main Window
      mode = "HOME";
      break;
    case 1: //Step Recording
      mode = "MOTION DETECTION";
      break;
    case 2: //Gait Analysis
      mode = "GAIT ANALYSIS";
      break;
    case 3: //Interesting Mode
      mode = "GUIDED WORKOUT";
      break;
  }

  text(mode, 5, height/20);

}
/* End of Top Bar */
/**************************/

/*******************/
/* Step Analysis */

//adds to the step counter after a step is detected
void incrementSteps()
{
      //increment steps by 2 since there's only one sole but a cycle would be 2 steps
      //unfortunate innate problem is that if you step off with the FSR foot, the counter will always be off by 1

      if(stepRecord.on){
        numSteps = numSteps + 2;
        //println(numSteps);
      }

}

//detects steps based on a toe off into heel strike cycle
void detectStep()
{
    if(mFF > pThresh && heel < pThresh && stepState == 0){
      stepState = 1;
      //println("Toe Off");
    } else if((mF > pThresh || lMF > pThresh) && stepState == 1) {
      stepState = 2;
      //println("Mid Stance");
    } else if(mFF < pThresh && heel > pThresh && stepState == 2) {
      stepState = 0;
      incrementSteps();
      //println("Heel Strike");

    }
}

//stores how many steps taken in a 2 minute period to cadence
//takes difference of current time found from millis() and timer to tell when 2 minutes is up
//startTime and startStepCount should be initialized by an event
//void findCadence(constant long startTime, const int& startStepCount)
//{
//    if((millis() - startTime) >= 120000)
//        cadence = (numSteps - startStepCount);
//}

/**** End of Step Analysis *****/
/********************************/

/*******************/
/* Home Page*/
void home() {

  // Buttons to display in stages 0-2
  button(sRSP, stepText, 30, 255, stepRecordButton, #808080, #006699);
  button(gRSP, gaitText, 30, 255, gaitRecordButton, #808080, #006699);
  button(iRSP, intrText, 30, 255, intrBtn,          #808080, #006699);
  button(mDSP, motionDetectionText, 30, 255, motionDetectionButton,          #808080, #006699);
  button(sRRSTSP, "■", 45, 255, stepResetButton, #ff4d4d, #ff0000);

  //Record steps
  timer(stepRecord);
  if(stepRecord.on || stepRecord.totTime > 0){
    stepText = nfc(stepRecord.totTime/1000, 1);
  } else {
    stepText = "Record Steps";
  }
  //Cadence Calculations
  if(stepRecord.totTime >= 1000){
    cadence = numSteps/(stepRecord.totTime/60000);
  }

  fill(0, 102, 153);
  textAlign(LEFT);
  textSize(35);
  text("Please enter your Step Length (ft): " + stepLength, 25, height/10 + 5);

  if(lengthLock){
    float sL = Float.valueOf(stepLength);
    text("Your Stride Length: " + nfc(sL*2,0) + " ft", 25, height/10 + 55);
  }

  textSize(50);
  text("Cadence: "+ cadence, 80, height/2 - 20);
  text("Step Count: " + nfc(numSteps,1), 80, height/2 - 90);
  text("Cadence: "+ cadence, 80, height/2 - 20);




}

/* End of Home*/
/*******************/


/*******************/
/*Motion Detection*/
int motionTimer = 0;
void motionDetection() {
  println(moveX);
  if(moveX || moveY){
    motionTimer++;
  }
  
  if(movedLeft){
    motion = "MOVED LEFT";
  } else if (movedRight) {
    motion = "MOVED RIGHT";
  } else if (movedForward) {
    motion = "MOVED FORWARD";
  } else if (movedBack) {
    motion = "MOVED BACK";    
  } else {
    motion = "Standing Still";
  }
  
  text("You've been moving for: " + nfc(float(motionTimer)/1000,2) + " sec" , 20, 100);
  textSize(80);
  text(motion + " Detected!", 20, 950);
}

/* End of Home*/
/*******************/

/*******************/
/* Heat Map */
void heatMap() {

  background(f_map);


  // toe
  fill(255, 0, 0);
  ellipse(635, 370, mFFR, mFFR);

  // green
  fill(0, 255, 0);
  ellipse(690, 470, mFR, mFR);

  // blue
  fill (0, 0, 255);
  ellipse(800, 470, lMFR, lMFR);

  // heel
  fill(200, 0, 200);
  ellipse(740, 720, heelR, heelR);

}

/* End of Heat Map */
/*******************/

/*******************/
/* Gait Analysis */
void gaitAnalysis() {

  //Record Times
  timer(normalGaitRecord);
  timer(inToeingRecord);
  timer(outToeingRecord);
  timer(tipToeingRecord);
  timer(heelRecord);

  if(normalGaitRecord.on || normalGaitRecord.totTime > 0){
    normalGaitText = nfc(normalGaitRecord.totTime/1000, 1);
  } else {
    normalGaitText = "Normal Gait";
  }
  if(inToeingRecord.on || inToeingRecord.totTime > 0){
    inToeingText = nfc(inToeingRecord.totTime/1000, 1);
  } else {
    inToeingText = "In-Toeing";
  }
  if(outToeingRecord.on || outToeingRecord.totTime > 0){
    outToeingText = nfc(outToeingRecord.totTime/1000, 1);
  } else {
    outToeingText = "Out-Toeing";
  }
  if(tipToeingRecord.on || tipToeingRecord.totTime > 0){
    tipToeingText = nfc(tipToeingRecord.totTime/1000, 1);
  } else {
    tipToeingText = "TipToeing";
  }
  if(heelRecord.on || heelRecord.totTime > 0){
    heelText = nfc(heelRecord.totTime/1000, 1);
  } else {
    heelText = "Heel Walk";
  }

  button(nGSP, normalGaitText, 30, 255, normalGait, #808080, #006699);
  button(iTSP, inToeingText, 30, 255, inToeingButton, #808080, #006699);
  button(oTSP, outToeingText, 30, 255,  outToeingButton,          #808080, #006699);
  button(tTSP, tipToeingText, 30, 255, tipToeingButton,          #808080, #006699);
  button(hSP, heelText, 30, 255, heelButton, #808080, #006699);

  if(normalGaitRecord.on){
    normalGaitMFP = calcMFPavg();
  } else if (inToeingRecord.on){
    inToeingMFP = calcMFPavg();
  } else if (outToeingRecord.on){
    outToeingMFP = calcMFPavg();
  } else if (tipToeingRecord.on){
    tipToeingMFP = calcMFPavg();
  } else if (heelRecord.on){
    heelMFP = calcMFPavg();
  }

  fill(0, 102, 153);
  textAlign(LEFT);
  if(stepState == 1 ){
    float tempMFP = calcMFP(mF, mFF, lMF, heel);


    if(tempMFP >= outToeingMFP){
      lastProfile = "Out-Toeing";
    } else if (tempMFP >= normalGaitMFP) {
      lastProfile = "Normal Gait";
    } else if (tempMFP >= inToeingMFP) {
      lastProfile = "In-Toeing";
    } else if (tempMFP >= tipToeingMFP) {
      lastProfile = "Tip-Toeing";
    } else if (tempMFP < tipToeingMFP) {
      lastProfile = "Heel Walking";
    }

  }

  textSize(45);
  text("Average MFP's", 20, 600);
  textSize(30);
  text("Normal Gait MFP: " + normalGaitMFP, 20, 640);
  text("In-Toeing MFP: " + inToeingMFP, 20, 680);
  text("Out-Toeing MFP: " + outToeingMFP, 20, 720);
  text("Tip Toeing MFP: " + tipToeingMFP, 20, 760);
  text("Heel Walk MFP: " + heelMFP, 20, 800);
  textSize(80);
  text(lastProfile + " Detected!", 20, 950);
}

float calcMFPavg(){
  if(stepState == 1){
    MFSum = MFSum + mF;
    MFFSum = MFFSum + mFF;
    LMFSum = LMFSum + lMF;
    HeelSum = HeelSum + heel;
  }

  return calcMFP(MFSum, MFFSum, LMFSum, HeelSum);
  //println(Profile);
}

float calcMFP(float MF, float MFF, float LMF, float HEEL){
  return  (( MF + MFF ) * 100) / ( MF + MFF + LMF + HEEL + 0.001 );
}

/* End of Gait Analysis */
/*******************/

/****************************/
/* Section 4 Implementation */
int intrState = 0;
int lastTime = 0;
void intrStage(){
  background(i_map);
  println(intrState);
  // Order of movements to take right, left, forward, backward
  if        (intrState == 0){
    directionList("MOVE RIGHT");
    if(movedRight){
      intrState = 1;
      lastTime = millis();
    }
  } else if ( intrState == 1 && millis() - lastTime > 2000){
    directionList("MOVE LEFT");
    if(movedRight){
      intrState = 2;
      lastTime = millis();
    }
  } else if ( intrState == 2 && millis() - lastTime > 2000){
    directionList("MOVE FORWARD");
    if(movedRight){
      intrState = 3;
      lastTime = millis();
    }
  } else if ( intrState == 3 && millis() - lastTime > 2000){
    directionList("MOVE BACK");
    if(movedRight){
      intrState = 4;
      lastTime = millis();
    }
  } else if ( intrState == 4 && millis() - lastTime > 2000){
    background(255);
    fill(0);
    textSize(50);
  }
}

/* Movement directions and which flag to flip
    - accX > 0 : right      -> movedRight:   true
    - accX < 0 : left       -> movedLeft:    true
    - accY > 0 : forward    -> movedForward: true
    - accY < 0 : backward   -> movedBack:    true
*/

// Display the current desired direction for the user to move in
void directionList(String cmd){
  button(iRRec, cmd, 40, 255, false, #808080, #006699);
  //text(cmd, 230, 280);
}

// Check if the user moved
// Check which direction they moved in
void checkDirection(){
  
  if(checkMove(accX, lastAccX)){
    moveX = true;
      if(lastAccX - accX > 0.05){
        movedRight = true;
        movedLeft = false;
        println("RIGHT");
      } else if (lastAccX - accX < 0.05) {
        movedRight = false;
        movedLeft = true;
        println("RIGHT");
      }
    
  } else {
    moveX = false;
    movedRight = false;
    movedLeft = false;
  }
  
  if(checkMove(accY, lastAccY)){
    moveY = true;
    if(lastAccY - accY > 0.05){
      movedForward = true;
      movedBack = false;
    } else if (lastAccY - accY < 0.05) {
      movedForward = false;
      movedBack = true;
    }
  } else {
    moveY = false;
    movedForward = false;
    movedBack = false;
  }
  if(checkMove(accZ, lastAccZ)){
    moveZ = true;
  } else {
    moveZ = false;
  }
}

// Check if they moved
boolean checkMove(float acc, float lastAcc){
  if(abs(lastAcc - acc) > 0.05){
    return true;
  } else {
    return false;
  }
}

// check which direction they moved in
void direction(float acc, float lastAcc, boolean posDir, boolean negDir){
  if(lastAcc - acc > 0.05){
    posDir = true;
    negDir = false;
  } else if (lastAcc - acc < 0.05) {
    posDir = false;
    negDir = true;
  }
}

/* End of Section 4 Implementation */
/***********************************/

/****************************/
/* Timer */
void timer(timerC t){
  //starts a timer
  if(t.on){

    float tempTime = millis() - t.lastTime;
    if(t.lastTime == 0 ){
      t.lastTime = millis(); //sets
      //println(lastTime);
    } else if(tempTime >= timeInt) {
      t.totTime = t.totTime + tempTime;
      t.lastTime = millis();
      if(t.totTime >= t.autoStopDuration){
        t.reset = true;
      }
    }
  }

  if(t.reset){
    t.totTime = 0;
    t.lastTime = 0;
    t.reset = false;
    t.on = false;
  }
}

class timerC {
  boolean on = false;
  float lastTime = 0;
  float totTime = 0;
  float autoStopDuration = 0;
  boolean reset = false;

  timerC(float A) {
    autoStopDuration = A;
  }
}
/* End of Timer */
/***********************************/

/*******************/
/* Button Function */

void button(int SP[], String buttonText, int textSize, int textColor, boolean isSelected, int highlightColor, int baseColor) {
  //Creates a rectangle shaped button
  //SP are arrays of size and position of the button

  if(isSelected){ //highlights if selected or not
    fill(highlightColor);
  } else {
    fill(baseColor);
  }
  rect(SP[0], SP[1], SP[2], SP[3]);

  // TODO: need to align text properly
  if (buttonText == iRText){
    textAlign(CENTER);
  }

  //button text
  textSize(textSize);
  textAlign(CENTER);
  fill(textColor);
  text(buttonText,SP[0]+SP[2]/2,SP[1]+SP[3]/2+textSize/2);
}

boolean overRect(int x, int y, int width, int height)  {
  if (mouseX >= x && mouseX <= x+width &&
      mouseY >= y && mouseY <= y+height) {
    return true;
  } else {
    return false;
  }
}

void mousePressed() {
  if (homeButton) {
    state = 0;
    background(255);
  } else if(stepRecordButton) {
    if(stepRecord.on == false){
      stepRecord.on = true;
    } else if(stepRecord.on == true) {
      stepRecord.on = false;
      stepRecord.lastTime = 0;
    }
  } else if (motionDetectionButton) {   // for guided workout
    state = 1;
  } else if(stepResetButton) {
    stepRecord.reset = true;
    numSteps = 0;
  } else if (gaitRecordButton) {   // for guided workout
    state = 2;
  } else if(normalGait) {
    if(normalGaitRecord.on == false){
      normalGaitRecord.on = true;
      MFSum = 0;
      MFFSum = 0;
      LMFSum = 0;
      HeelSum = 0;
    } else if(normalGaitRecord.on == true) {
      normalGaitRecord.on = false;
      normalGaitRecord.lastTime = 0;
    }
  } else if(inToeingButton) {
    if(inToeingRecord.on == false){
      inToeingRecord.on = true;
      MFSum = 0;
      MFFSum = 0;
      LMFSum = 0;
      HeelSum = 0;
    } else if(inToeingRecord.on == true) {
      inToeingRecord.on = false;
      inToeingRecord.lastTime = 0;
    }
  } else if(outToeingButton) {
    if(outToeingRecord.on == false){
      outToeingRecord.on = true;
      MFSum = 0;
      MFFSum = 0;
      LMFSum = 0;
      HeelSum = 0;
    } else if(outToeingRecord.on == true) {
      outToeingRecord.on = false;
      outToeingRecord.lastTime = 0;
    }
  } else if(tipToeingButton) {
    if(tipToeingRecord.on == false){
      tipToeingRecord.on = true;
      MFSum = 0;
      MFFSum = 0;
      LMFSum = 0;
      HeelSum = 0;
    } else if(tipToeingRecord.on == true) {
      tipToeingRecord.on = false;
      tipToeingRecord.lastTime = 0;
    }
  } else if(heelButton) {
    if(heelRecord.on == false){
      heelRecord.on = true;
      MFSum = 0;
      MFFSum = 0;
      LMFSum = 0;
      HeelSum = 0;
    } else if(heelRecord.on == true) {
      heelRecord.on = false;
      heelRecord.lastTime = 0;
    }
  } else if (intrBtn) {
    state = 3;
  }

}

void update(int x, int y) {
  if ( overRect(hBSP[0],hBSP[1],hBSP[2],hBSP[3]) ) {
    homeButton = true;
    stepRecordButton = false;
    gaitRecordButton = false;
    motionDetectionButton = false;
    intrBtn = false;
    stepResetButton = false;
  } else if ( overRect(sRSP[0],sRSP[1],sRSP[2],sRSP[3])) {
    homeButton = false;
    stepRecordButton = true;
    gaitRecordButton = false;
    motionDetectionButton = false;
    intrBtn = false;
    stepResetButton = false;
  } else if ( overRect(gRSP[0],gRSP[1],gRSP[2],gRSP[3])) {
    homeButton = false;
    stepRecordButton = false;
    gaitRecordButton = true;
    motionDetectionButton = false;
    intrBtn = false;
    stepResetButton = false;
  } else if ( overRect(iRSP[0],iRSP[1],iRSP[2],iRSP[3])) {
    homeButton = false;
    stepRecordButton = false;
    gaitRecordButton = false;
    motionDetectionButton = false;
    intrBtn = true;
    stepResetButton = false;
  } else if ( overRect(mDSP[0],mDSP[1],mDSP[2],mDSP[3])) {
    homeButton = false;
    stepRecordButton = false;
    gaitRecordButton = false;
    motionDetectionButton = true;
    intrBtn = false;
    stepResetButton = false;
  } else if ( overRect(sRRSTSP[0],sRRSTSP[1],sRRSTSP[2],sRRSTSP[3])) {
    homeButton = false;
    stepRecordButton = false;
    gaitRecordButton = false;
    motionDetectionButton = false;
    intrBtn = false;
    stepResetButton = true;
  } else if ( overRect(nGSP[0],nGSP[1],nGSP[2],nGSP[3])) {
    homeButton = false;
    stepRecordButton = false;
    gaitRecordButton = false;
    motionDetectionButton = false;
    intrBtn = false;
    stepResetButton = false;
    normalGait = true;
    inToeingButton = false;
    outToeingButton = false;
    tipToeingButton = false;
    heelButton = false;
  } else if ( overRect(iTSP[0],iTSP[1],iTSP[2],iTSP[3])) {
    homeButton = false;
    stepRecordButton = false;
    gaitRecordButton = false;
    motionDetectionButton = false;
    intrBtn = false;
    stepResetButton = false;
    normalGait = false;
    inToeingButton = true;
    outToeingButton = false;
    tipToeingButton = false;
    heelButton = false;
  } else if ( overRect(oTSP[0],oTSP[1],oTSP[2],oTSP[3])) {
    homeButton = false;
    stepRecordButton = false;
    gaitRecordButton = false;
    motionDetectionButton = false;
    intrBtn = false;
    stepResetButton = false;
    normalGait = false;
    inToeingButton = false;
    outToeingButton = true;
    tipToeingButton = false;
    heelButton = false;
  } else if ( overRect(tTSP[0],tTSP[1],tTSP[2],tTSP[3])) {
    homeButton = false;
    stepRecordButton = false;
    gaitRecordButton = false;
    motionDetectionButton = false;
    intrBtn = false;
    stepResetButton = false;
    normalGait = false;
    inToeingButton = false;
    outToeingButton = false;
    tipToeingButton = true;
    heelButton = false;
  } else if ( overRect(hSP[0],hSP[1],hSP[2],hSP[3])) {
    homeButton = false;
    stepRecordButton = false;
    gaitRecordButton = false;
    motionDetectionButton = false;
    intrBtn = false;
    stepResetButton = false;
    normalGait = false;
    inToeingButton = false;
    outToeingButton = false;
    tipToeingButton = false;
    heelButton = true;
  } else {
    homeButton = false;
    stepRecordButton = false;
    gaitRecordButton = false;
    motionDetectionButton = false;
    intrBtn = false;
    stepResetButton = false;
    normalGait = false;
    inToeingButton = false;
    outToeingButton = false;
    tipToeingButton = false;
    heelButton = false;
  }
}

/* End of Button Function */
/**************************/

/*******************/
/* Serial Event */
void serialEvent (Serial myPort) {
  // get the ASCII string:
  String inString = myPort.readStringUntil('\n');
  //println(inString);

  if (inString != null ) {
    // trim off any whitespace:
    inString = trim(inString);
    String[] inStringList = split(inString, ',');  // split the pair of values

    accX = float(inStringList[0]);
    accY = float(inStringList[1]);
    accZ = float(inStringList[2]);
    mFF = int(inStringList[3]);
    mF = int(inStringList[4]);
    heel = int(inStringList[5]);
    lMF =  int(inStringList[6])*7/10;

    //Check if data is being read
    //println(accX, accY, accZ, mFF, mF, heel, lMF);


    //Map radius of Circles
    mFFR = int(map(mFF, 0, 1023, 0, 100));
    mFR = int(map(mF, 0, 1023, 0, 100));
    heelR = int(map(heel, 0, 1023, 0, 100));
    lMFR = int(map(lMF, 0, 1023, 0, 100));

    detectStep();
    if(millis() - lastDirection > 400){
      checkDirection();
      lastDirection = millis();
    }
    
    lastAccX = accX;
    lastAccY = accY;
    lastAccZ = accZ;

  }

}


/* End of Serial Even*/

void keyPressed() {

  if (key==BACKSPACE) {
    if(lengthLock == false){
      stepLength = "";
    }
  } else if (key==ENTER || key==RETURN) {
    if (lengthLock) {
      lengthLock = false;
    } else {
      lengthLock = true;
    }
  }
  else {
    if(state == 0 && stepLength.length() < 5 && lengthLock == false) { //prevents age to be greater than 3 digits
      lastKey = key;
      stepLength = stepLength + key;
    }
  }
}
/**************************/
