#include <Servo.h>

Servo myservo;  // create servo object to control a servo

int redPin = 11;
int greenPin = 10;
int bluePin = 9;

int motorPin = 2;

int buttonPin = 5;

int red = 0;
int green = 0;
int blue = 0;
int servoPos = 0;
int buttonState = 0;
bool runState = false;

int buttonStartTime = 0;
bool buttonStarted = false;

int startTime = 0;

double totalTime = 60000;
int totalTasks = 5;

int currentTask = 0;

void setup() {
  Serial.begin(9600);
  myservo.attach(motorPin);
  
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  
  pinMode(buttonPin, INPUT);
  
  red = 0;
  green = 0;
  blue = 0;
}

void loop() {
  // button clicked
  int state = digitalRead(buttonPin);
  double elapsedTime = double(millis()-startTime);

  if (runState == 1) {
    double diff = elapsedTime/totalTime;
    double incr = 255*diff;
    red = 0;
    green = incr;
    blue = 0;
  }

  if (elapsedTime % double(totalTime/totalTasks) == 0) {
    Serial.println(2);
  }

  if (state == HIGH) {
    buttonState = 1;
    if (buttonStarted == false) {
      buttonStartTime = millis();
      buttonStarted = true;
    }
  } else {
    // button released
    if (buttonState == 1) {
      buttonState = 0;
      buttonStarted = false;
      int holdLength = millis() - buttonStartTime;
      if (holdLength > 3000) {
        runState = 0;
        Serial.println(0);
        red = 0;
        green = 0;
        blue = 0;
      } else {
        if (runState == 0) {
          runState = 1;
          Serial.println(1);
          red = 0;
          green = 255;
          blue = 0;
          startTime = millis();
        } else {
          cameraClicked();  
        }
      }
    }
  }

  setColor(red, green, blue);
  delay(100);
}
 
void setColor (int red, int green, int blue) {
  analogWrite(redPin, red);
  analogWrite(greenPin, green);
  analogWrite(bluePin, blue);  
}

void cameraClicked () {
  Serial.println(3);
  setColor(0, 0, 0);
  delay(500);
  setColor(0, 0, 255);
  delay(500);
  setColor(0, 0, 0);
  delay(500);
  setColor(0, 0, 255);
  delay(500);
  setColor(0, 0, 0);
  delay(500);
  setColor(0, 0, 255);
  delay(500);
  setColor(0, 0, 0);
  delay(500);
  currentTask += 1;
  setColor(red, green, blue);
}

