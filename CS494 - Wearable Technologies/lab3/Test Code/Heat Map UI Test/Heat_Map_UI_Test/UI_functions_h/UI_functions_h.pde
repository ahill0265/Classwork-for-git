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
