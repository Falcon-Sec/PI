const int ledVerde = 13
const int ledVermelho = 10; // the pin that the LED is attached to
int incomingByte;      // a variable to read incoming serial data into

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  // initialize the LED pin as an output:
  pinMode(ledVermelho, OUTPUT);
  pinMode(ledVerde, OUTPUT);
}

void loop() {
  //Analisa a Serial
  if (Serial.available() > 0) {
    // Le a serial
    incomingByte = Serial.read();
   //Se G led verde
    if (incomingByte == 'G') {
      digitalWrite(ledVerde, HIGH);
    }
    //Se P desliga os leds
    if (incomingByte == 'P') {
      digitalWrite(ledVerde, LOW);
      digitalWrite(ledVermelho, LOW);
    }
    //Se R led vermelho
    if (incomingByte == 'R') {
      digitalWrite(ledVermelho, HIGH);
    }
  }
}
