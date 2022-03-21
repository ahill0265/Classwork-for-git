// Mary
// gathers MF, LF, MM, HEEL data ten times to get an average for the baseline
// graphs MF, LF, MM, HEEL data continuously

//Variables
int halfWidth = 500;

// for the graphing
float MFb = random(0,150);
float LFb = random(0,150);
float MMb = random(0,150);
float HEELb = random(0,150);
float MFa = 0;
float LFa = 0;
float MMa = 0;
float HEELa = 0;
int xPos = 1;         // horizontal position of the graph
int lastxPos = 0;
float lastSec = 0;
int timeInt = 100; //interval to counting time

// for the baseline values
float MFavg = 0.0;
float LFavg = 0.0;
float MMavg = 0.0;
float HEELavg = 0.0;

void setup () {

  size(1000, 500);          // set the window size    
  
  fill(0, 102, 153);
  rect(0, 0, width/2, height);
  rect(width/2, 0, width/2, height);
  
  // calculate a 10 "second" average
  for(int i = 0; i <= 10; i++){
    MFavg = MFavg + random(0,150);
    LFavg = LFavg + random(0,150);
    MMavg = MMavg + random(0,150);
    HEELavg = HEELavg + random(0,150);
  }
  MFavg = MFavg / 10;
  LFavg = LFavg / 10;
  MMavg = MMavg / 10;
  HEELavg = HEELavg / 10;
     
}

void draw () {
  
  if (lastxPos == 0){
    clear();
    setup();
  }
  
  if(millis() - lastSec > timeInt){

        if (xPos >= 500) {  // once we get halfway, start over
          xPos = 0;         // start at the leftside of the whole graph
          fill(255);
          rect(0, 0, halfWidth, height);
        }
        else {
          // plot
          strokeWeight(1);
          stroke(255, 0, 0);
          line(lastxPos, 500 - MFb - 150, xPos, 500 - MFa - 150);
          //stroke(0, 255, 0);
          //line(lastxPos, 500 - LFb - 150, xPos, 500 - LFa - 150);
          //stroke(0, 0, 255);
          //line(lastxPos, 500 - MMb - 150, xPos, 500 - MMa - 150);
          //stroke(0);
          //line(lastxPos, 500 - HEELb - 150, xPos, 500 - HEELa - 150);
          
          lastxPos = xPos;
          xPos++;
          
          MFb = random(0,150);
          LFb = random(0,150);
          MMb = random(0,150);
          HEELb = random(0,150);
          MFa = MFb;
          LFa = LFb;
          MMa = MMb;
          HEELa = HEELb;
          
        }
        lastSec = millis();
    }   
    
    textSize(30);
    fill(255,0,0); //change text color
    text("MF Average: " + MFavg, width/2 + 20, height/2 - 100);
    text("LF Average: " + LFavg, width/2 + 20, height/2 - 50);
    text("MM Average: " + MMavg, width/2 + 20, height/2);
    text("HEEL Average: " + HEELavg, width/2 + 20, height/2 + 50);
  
}
