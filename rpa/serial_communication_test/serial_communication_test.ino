#define LED 7
#define lightSensor A0

void setup() {
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
  pinMode(lightSensor, INPUT);
}

void loop() {

  int lightValue = analogRead(lightSensor);
  Serial.println(lightValue);
  Serial.flush();

  while(!Serial.available()) {
    ;
  }

    String command = Serial.readStringUntil('\n');

    if(command.equals("on")) {
      digitalWrite(LED, HIGH);
    }
    else if(command.equals("off")) {
      digitalWrite(LED, LOW);
    } 

  
  
  }
