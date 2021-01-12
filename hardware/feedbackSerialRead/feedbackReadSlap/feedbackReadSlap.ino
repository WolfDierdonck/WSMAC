#include <Servo.h>
#define SERVO_PIN 9

//Servo control variables
Servo servo;

//Makes the servo (and the hand attached to it) sweep down 180 deg and back up
void slap() {
  servo.write(0);
  delay(500);
  servo.write(180);
  delay(500);
  servo.write(0);
}

void positiveFeedbackReceived(){
  
}

void negativeFeedbackReceived(){
  slap();
}

void handleFeedbackReceived(char feedback){
  if(feedback == 'P'){
      positiveFeedbackReceived();
  } else if(feedback == 'N'){
      negativeFeedbackReceived();
  }
}

void setup() {
  Serial.begin(9600);
  servo.attach(SERVO_PIN);
  servo.write(0);
}

void loop() {
  //char feedback = Serial.read();
  //handleFeedbackReceived(feedback);
}
