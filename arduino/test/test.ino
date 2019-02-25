//int redPin = 8;
//int greenPin = 7;
//int bluePin = 6;

//int motorPin1 = 2;
//int motorPin2 = 3;
//int motorPin3 = 4;
//int motorPin4 = 5;

#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
  #include <avr/power.h>
#endif

int buttonPin = 3;
Adafruit_NeoPixel pixels = Adafruit_NeoPixel(12, 5, NEO_GRB + NEO_KHZ800);

int red = 0;
int green = 0;
int blue = 0;

int buttonState = 0;
bool runState = false;

int buttonStartTime = 0;
bool buttonStarted = false;

int halfStep = 8;

int stepCount = 0;
int stepDelay = 1;

int startTime = 0;

double totalTime = 5000;
int totalTasks = 5;

int currentTask = 0;

void setup() {
  Serial.begin(9600);
  pixels.begin();
  
//  pinMode(redPin, OUTPUT);
//  pinMode(greenPin, OUTPUT);
//  pinMode(bluePin, OUTPUT);
//
//  pinMode(motorPin1, OUTPUT);
//  pinMode(motorPin2, OUTPUT);
//  pinMode(motorPin3, OUTPUT);
//  pinMode(motorPin4, OUTPUT); 
  
  pinMode(buttonPin, INPUT);
}

String received = "";

void loop() {
  if (Serial.available() > 0) {
    char receivedChar = Serial.read();
    
    if (receivedChar == ';') {
      if (received[0] == 'r') {
        red = int(received[1]) * 100 + int(received[2]) * 10 + int(received[3]);
      } else if (received[0] == 'g') {
        green = int(received[1]) * 100 + int(received[2]) * 10 + int(received[3]);
      } else if (received[0] == 'b') {
        blue = int(received[1]) * 100 + int(received[2]) * 10 + int(received[3]);
      } else if (received[0] == 'm') {
        int stepVal = int(received[1]) * 100 + int(received[2]) * 10 + int(received[3]);
//        moveSteps(stepVal);
      }
      setColor(red, green, blue);
      received = "";
    } else {
      received = received + receivedChar;
    }
  }
  // button clicked
  int state = digitalRead(buttonPin);
  double elapsedTime = double(millis()-startTime);

  if (state == HIGH) {
    buttonState = 1;
    if (buttonStarted == false) {
      buttonStartTime = millis();
      buttonStarted = true;
    } else {
      int holdLength = millis() - buttonStartTime;
      if (holdLength > 2250) {
        if (red == 0 && blue == 0 && green == 0) {
          red = 0;
          blue = 255;
          green = 0;
          setColor(red, green, blue);  
          Serial.println(1);
        } else {
          red = 0;
          blue = 0;
          green = 0;
          setColor(red, green, blue);
          Serial.println(0);
        }
        buttonStarted = false;
      }
    }
  } else {
    // button released
    if (buttonState == 1) {
      buttonState = 0;
      buttonStarted = false;
      int holdLength = millis() - buttonStartTime;

      if (holdLength < 2250) {
        Serial.println(2);
      }
    }
  }
  
  delay(100);
}

//void moveSteps(int steps) {
//  for(int x = 0; x < steps; x++) {
//    for(int i = 0; i < 8; i++) {
//      switch(i) { 
//        case 0: 
//          digitalWrite(motorPin1, LOW);  
//          digitalWrite(motorPin2, LOW); 
//          digitalWrite(motorPin3, LOW); 
//          digitalWrite(motorPin4, HIGH); 
//        break;  
//        case 1: 
//          digitalWrite(motorPin1, LOW);  
//          digitalWrite(motorPin2, LOW); 
//          digitalWrite(motorPin3, HIGH); 
//          digitalWrite(motorPin4, HIGH); 
//        break;  
//        case 2: 
//          digitalWrite(motorPin1, LOW);  
//          digitalWrite(motorPin2, LOW); 
//          digitalWrite(motorPin3, HIGH); 
//          digitalWrite(motorPin4, LOW); 
//        break;  
//        case 3: 
//          digitalWrite(motorPin1, LOW);  
//          digitalWrite(motorPin2, HIGH); 
//          digitalWrite(motorPin3, HIGH); 
//          digitalWrite(motorPin4, LOW); 
//        break;  
//        case 4: 
//          digitalWrite(motorPin1, LOW);  
//          digitalWrite(motorPin2, HIGH); 
//          digitalWrite(motorPin3, LOW); 
//          digitalWrite(motorPin4, LOW); 
//        break;  
//        case 5: 
//          digitalWrite(motorPin1, HIGH);  
//          digitalWrite(motorPin2, HIGH); 
//          digitalWrite(motorPin3, LOW); 
//          digitalWrite(motorPin4, LOW); 
//        break;  
//          case 6: 
//          digitalWrite(motorPin1, HIGH);  
//          digitalWrite(motorPin2, LOW); 
//          digitalWrite(motorPin3, LOW); 
//          digitalWrite(motorPin4, LOW); 
//        break;  
//        case 7: 
//          digitalWrite(motorPin1, HIGH);  
//          digitalWrite(motorPin2, LOW); 
//          digitalWrite(motorPin3, LOW); 
//          digitalWrite(motorPin4, HIGH); 
//        break;  
//        default: 
//          digitalWrite(motorPin1, LOW);  
//          digitalWrite(motorPin2, LOW); 
//          digitalWrite(motorPin3, LOW); 
//          digitalWrite(motorPin4, LOW); 
//        break;  
//      }
//      delay(stepDelay);
//    }   
//  }
//}
 
void setColor (int red, int green, int blue) {
  for(int i=0;i<12;i++){
    pixels.setPixelColor(i, pixels.Color(red,green,blue));
    pixels.show();
  }
}
