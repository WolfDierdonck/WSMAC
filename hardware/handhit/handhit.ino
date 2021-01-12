#include <Servo.h>
#define SERVO_PIN 9

Servo servo;
int servoPosition;

void setup() {
  Serial.begin(9600);
  servo.attach(SERVO_PIN);
  servoPosition = 10;
  servo.write(10);
}

void loop() {
  //Proof of concept - just make it keep hitting, over and over again
  if (Serial.available() > 0) {
    Serial.read();
    Serial.write("I think it worked");
     slap();
  }
  delay(4000);
  //slap();
}

void slap() {
  //Let it sit for a little (the time accounts for the speed of the servo motor)
  for (int i = 0; i < 18; i++) {
    servoPosition += 10;
    servo.write(servoPosition);
    delay(50);
  }
  servoPosition = 10;
  servo.write(servoPosition);
}
