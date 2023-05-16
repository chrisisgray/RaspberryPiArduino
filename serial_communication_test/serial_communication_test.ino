#define LED 13

void setup() {
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
}

void loop() {

  // number of bytes received
  if(Serial.available() > 0) {

    // this method assumes our message is in UTF encoding
    String input = Serial.readStringUntil('\n');
    
    if(input == "on") {
      
      Serial.println("valid");
      digitalWrite(LED, HIGH);
      
    } 
    else if(input == "off") {
      
      Serial.println("valid");
      digitalWrite(LED, LOW);
      
    } 
    else {
            Serial.println("invalid");
            digitalWrite(LED, HIGH);
            delay(100);
            digitalWrite(LED, LOW);

    }

    Serial.flush();
  }
  
  }
