#define relay 8
#define button 2

bool buttonState; //to read the output of the button
bool newButtonState; //for while loop below

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(relay,OUTPUT);
  pinMode(button, INPUT);
  pinMode(6,OUTPUT);
}

void loop() {
  //int sensMax;
  float Vq; //quoscient value
  float voltage; //calculated voltage from measurement
  float current; //calulated current value from measurement
  float Power;
  float effCurrent;
  int sensorValue;
  int sensMax = 0;
  int sensMin = 513;
  int highThreshold = 2;
  float lowThreshold = -2;
  

  if(digitalRead(button))
    buttonState = !buttonState;
 // buttonState = digitalRead(button);
  if(buttonState ==HIGH){
    buttonState = 1;
    digitalWrite(relay,HIGH);
    digitalWrite(6,HIGH);
  }
  else{
    digitalWrite(relay,LOW);
    digitalWrite(6,LOW);
  }


  //reference https://www.youtube.com/watch?v=W2Pa91I6QuY&app=desktop for finding max value
  for (int i=0 ; i<=200 ; i++)  //Monitors and logs the current input for 200 cycles to determine max and min current
    {
    sensorValue = analogRead(A0);    //Reads current input
    if(sensorValue >= sensMax)
      sensMax = sensorValue;
    else if(sensorValue <= sensMin)
      sensMin = sensorValue;
    }
    //

  Vq=5.0/2; //the queiscent output voltage
  
  float raw_volt = (5.0/1024)*(sensMax);
  voltage = (raw_volt - Vq)*.707;
  String stringVoltage = String(voltage);

  current = voltage/0.066; //sensitivity is 0.066mV/A, meaning rise of 1A produces 66mV output
  String stringCurrent = String(current);

  Power = voltage*current;
  String stringPower = String(Power);

  //testing if greater than a certain threshold for safety concern
  //testing if less than a certain threshold to automatically eliminate phantom power
  //or when a laptop is full charged as a customized feature  
  delay(10);
  if(current >= highThreshold || current<=lowThreshold){
    digitalWrite(relay,LOW);
    digitalWrite(6,LOW);
    delay(10);
    while(current >=0.9*highThreshold || current<=1.15*lowThreshold){
      digitalWrite(relay,LOW);
      //send alert message
      if(digitalRead(button)){
        digitalWrite(relay,HIGH);
        digitalWrite(6,HIGH);
        buttonState=1;
        break;
      }
      
    }
  }
  
    

  //else(digitalWrite(relay,HIGH));

  String energyInfo = String(stringVoltage+ "," + stringCurrent + "," + stringPower);//to communicate this value
  Serial.println(energyInfo);

  delay(1000);
    
}
