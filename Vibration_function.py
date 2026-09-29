const int buzzerPin = 8;

void setup() {
  pinMode(buzzerPin, OUTPUT);
}

void loop() {
  tone(buzzerPin, 500);  // Play a 1000 Hz tone
  delay(500);

  noTone(buzzerPin);      // Stop the tone
  delay(500);
}

