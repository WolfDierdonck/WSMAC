#include <Servo.h>
#define SERVO_PIN 9

//Servo control variables
Servo servo;

void thumbsUp() {
  delay(500);
  servo.write(0);
  delay(500);
}

void thumbsDown() {
  delay(500);
  servo.write(180);
  delay(500);
}

void positiveFeedbackReceived(){
  thumbsUp();
}

void negativeFeedbackReceived(){
  thumbsDown();
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
  //servo.write(0);
}

void loop() {
    thumbsUp();
    thumbsDown();
  //char feedback = Serial.read();
  //handleFeedbackReceived(feedback);
}
