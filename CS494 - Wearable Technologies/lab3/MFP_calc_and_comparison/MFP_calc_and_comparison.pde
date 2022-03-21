/******************************************************************************
Mary
calculate the MFP baseline using the following formula:
MFP = (( MMt + MFt ) * 100) / ( MMt + MFt + LFt + Heel + 0.001 )
then recalculate the current MFP occasionally and check if it's close to the MFP baseline
******************************************************************************/

//Variables
int halfWidth = 500;
int timeInt = 0; // "time" lapsed

float MFP = 0.0;
float MF = 0.0;
float LF = 0.0;
float MM = 0.0;
float HEEL = 0.0;
float MFPcurr = 0.0;

void setup () {

  size(1000, 500);          // set the window size    
  
  fill(0, 102, 153);
  rect(0, 0, width/2, height);
  rect(width/2, 0, width/2, height);
  
  // calculate a 10 "second" avgerage MFP
  for(int i = 0; i <= 10; i++){
    MF = random(0,150);
    LF = random(0,150);
    MM = random(0,150);
    HEEL = random(0,150);
    MFP = MFP + (( MM + MF ) * 100) / ( MM + MF + LF + HEEL + 0.001 );
  }
  MFP  = MFP / 10;
  
}

void draw () {
  
  textSize(30);
  fill(255,0,0); //change text color
  
  if (timeInt % 200 == 0) // check the current MFP value occasionally
  { 
    
    MF = random(0,150);
    LF = random(0,150);
    MM = random(0,150);
    HEEL = random(0,150);
    MFPcurr = (( MM + MF ) * 100) / ( MM + MF + LF + HEEL + 0.001 );
    
    if(MFPcurr > (1.1* MFP) || MFPcurr < (0.9* MFP)) // define upper and lower thesholds
    { 
      clear();
      fill(0, 102, 153);
      rect(0, 0, width/2, height);
      rect(width/2, 0, width/2, height);
      fill(255,0,0);
      text("no longer in midstance! " + nf(MFPcurr, 0, 2), 20, height/2);
      text("MFP: " + MFP, width/2 + 20, height/2);
    }
    else {
      clear();
      fill(0, 102, 153);
      rect(0, 0, width/2, height);
      rect(width/2, 0, width/2, height);
      fill(255,0,0);
      text("wow you're in midstance " + nf(MFPcurr, 0, 2), 20, height/2);
      text("MFP: " + MFP, width/2 + 20, height/2);
    }
    
  } // outtermost if
  
  timeInt++;
}
