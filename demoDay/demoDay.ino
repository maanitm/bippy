int redPin = 2;
int greenPin = 3;
int bluePin = 4;

int buttonPin = 5;

int red = 0;
int green = 0;
int blue = 0;

int buttonState = 0;
bool runState = false;

int buttonStartTime = 0;
bool buttonStarted = false;

int startTime = 0;

double totalTime = 5000;
int totalTasks = 5;

int currentTask = 0;

void setup() {
  Serial.begin(9600);
  
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  
  pinMode(buttonPin, INPUT);
}

boolean triggerColor = false;
boolean triggerColorDone = false;
boolean triggerCam = false;
boolean triggerCamDone = false;
boolean triggerSpeaker = false;
boolean triggerSpeakerDone = false;

void loop() {
  // button clicked
  int state = digitalRead(buttonPin);
  double elapsedTime = double(millis()-startTime);

  if (state == HIGH) {
    if (!triggerColor) {
      startTime = millis();
      triggerColor = true;
    } else if (!triggerCam) {
      triggerCam = true;
    } else if (!triggerSpeaker) {
      triggerSpeaker = true;
    }
  }
  if (triggerColor && !triggerColorDone) {
    if (elapsedTime < totalTime/3) {
      red = 0;
      green = 255;
      blue = 0;  
    } else if (elapsedTime < (totalTime*2)/3) {
      red = 255;
      green = 255;
      blue = 0;
    } else if (elapsedTime < totalTime) {
      red = 255;
      green = 0;
      blue = 0;
      triggerColorDone = true;
    } else {
      red = 255;
      green = 255;
      blue = 255;
    }
  }
  if (triggerCam && !triggerCamDone) {
    cameraClicked();
    triggerCamDone = true;
  }
  if (triggerSpeaker && !triggerSpeakerDone) {
    Serial.println(1);
    triggerSpeakerDone = true;
  }
  if (triggerSpeakerDone) {
    triggerColor = false;
    triggerColorDone = false;
    triggerCam = false;
    triggerCamDone = false;
    triggerSpeaker = false;
    triggerSpeakerDone = false;
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


