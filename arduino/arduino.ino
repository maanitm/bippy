int redPin = 8;
int greenPin = 7;
int bluePin = 6;

int motorPin1 = 2;
int motorPin2 = 3;
int motorPin3 = 4;
int motorPin4 = 5;

int buttonPin = 9;

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
  
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);

  pinMode(motorPin1, OUTPUT);
  pinMode(motorPin2, OUTPUT);
  pinMode(motorPin3, OUTPUT);
  pinMode(motorPin4, OUTPUT); 
  
  pinMode(buttonPin, INPUT);
}

void loop() {
  // button clicked
  int state = digitalRead(buttonPin);
  double elapsedTime = double(millis()-startTime);

  if (stepCount < 500) {
    moveSteps(500);
    stepCount += 500;  
  }
  
  if (runState == 1 && elapsedTime <= totalTime) {
    double diff = elapsedTime/totalTime;
    double incr = 255*diff;
    if (elapsedTime < totalTime/3) {
      red = 0;
      green = 255;
      blue = 0;  
    } else if (elapsedTime < (totalTime*2)/3) {
      red = 255;
      green = 255;
      blue = 0;
    } else {
      red = 255;
      green = 0;
      blue = 0;
    }
  } else if (elapsedTime > totalTime) {
    Serial.println(4);
    runState = 0;
    red = 0;
    green = 0;
    blue = 0;
  }

  if (int(elapsedTime) % int(totalTime/totalTasks) == 0) {
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
          buttonStartTime = 0;
          buttonStarted = false;
        } else {
          cameraClicked();  
        }
      }
    }
  }
  setColor(red, green, blue);
  delay(100);
}

void moveSteps(int steps) {
  for(int x = 0; x < steps; x++) {
  for(int i = 0; i < 8; i++) {
    switch(i){ 
   case 0: 
     digitalWrite(motorPin1, LOW);  
     digitalWrite(motorPin2, LOW); 
     digitalWrite(motorPin3, LOW); 
     digitalWrite(motorPin4, HIGH); 
   break;  
   case 1: 
     digitalWrite(motorPin1, LOW);  
     digitalWrite(motorPin2, LOW); 
     digitalWrite(motorPin3, HIGH); 
     digitalWrite(motorPin4, HIGH); 
   break;  
   case 2: 
     digitalWrite(motorPin1, LOW);  
     digitalWrite(motorPin2, LOW); 
     digitalWrite(motorPin3, HIGH); 
     digitalWrite(motorPin4, LOW); 
   break;  
   case 3: 
     digitalWrite(motorPin1, LOW);  
     digitalWrite(motorPin2, HIGH); 
     digitalWrite(motorPin3, HIGH); 
     digitalWrite(motorPin4, LOW); 
   break;  
   case 4: 
     digitalWrite(motorPin1, LOW);  
     digitalWrite(motorPin2, HIGH); 
     digitalWrite(motorPin3, LOW); 
     digitalWrite(motorPin4, LOW); 
   break;  
   case 5: 
     digitalWrite(motorPin1, HIGH);  
     digitalWrite(motorPin2, HIGH); 
     digitalWrite(motorPin3, LOW); 
     digitalWrite(motorPin4, LOW); 
   break;  
     case 6: 
     digitalWrite(motorPin1, HIGH);  
     digitalWrite(motorPin2, LOW); 
     digitalWrite(motorPin3, LOW); 
     digitalWrite(motorPin4, LOW); 
   break;  
   case 7: 
     digitalWrite(motorPin1, HIGH);  
     digitalWrite(motorPin2, LOW); 
     digitalWrite(motorPin3, LOW); 
     digitalWrite(motorPin4, HIGH); 
   break;  
   default: 
     digitalWrite(motorPin1, LOW);  
     digitalWrite(motorPin2, LOW); 
     digitalWrite(motorPin3, LOW); 
     digitalWrite(motorPin4, LOW); 
   break;  
 }
    delay(stepDelay);
  }   
  }
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
