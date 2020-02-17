void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

int shake = 0;
int count = 0;
int readed = 0;
void loop() {
  // put your main code here, to run repeatedly:
  if (shake == 0) {
    String counter = String(count);
    String readedconcat = String(readed);
    Serial.println("32,1,1," + counter + "," + readed);
    delay(1000);
    shake = 1;
  }

  if (shake == 1) {
    delay(1000);
    if (Serial.available()) {
      int readed = Serial.read();
      
      count++;
      shake = 0;
    }
  }
}
