const int led = 13; // the pin that the LED is attached to
int incomingByte;      // a variable to read incoming serial data into
#include "Adafruit_NeoPixel.h"
#define LED_COUNT 117
#define LED_PIN 8
#define left_fwd 12
#define left_bck 11
#define right_fwd 10
#define right_bck 9
Adafruit_NeoPixel strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);
void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  // initialize the LED pin as an output:
  pinMode(led, OUTPUT);
  strip.begin();
  pinMode(left_fwd,OUTPUT);
  pinMode(left_bck,OUTPUT);
  pinMode(right_fwd,OUTPUT);
  pinMode(right_bck,OUTPUT);
}

void loop() {
  int value = analogRead(A0);
  Serial.println(value);
  // see if there's incoming serial data:
  if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();
    // if it's a capital H (ASCII 72), turn on the LED:
    if (incomingByte == 'B') {
      digitalWrite(led, HIGH);
        for (int i = 0; i < LED_COUNT; i++){
          strip.setPixelColor(i, strip.Color(255, 0, 0)); // Красный цвет.
          strip.show();

        }
    }
    // if it's an L (ASCII 76) turn off the LED:
    if (incomingByte == 'N') {
      digitalWrite(led, LOW);
        for (int i = 0; i < LED_COUNT; i++){
          strip.setPixelColor(i, strip.Color(0, 0, 255)); // null
          strip.show();
        }
    }
    if (incomingByte == 'Z') {
        digitalWrite(led, LOW);
        for (int i = 0; i < LED_COUNT; i++){
          strip.setPixelColor(i, strip.Color(200, 160, 11)); // null
          strip.show();
        }
    }
    if (incomingByte == 'R') {
        digitalWrite(left_fwd,LOW);
        digitalWrite(left_bck,HIGH);
        digitalWrite(right_fwd,LOW);
        digitalWrite(right_bck,HIGH);
    }
    if (incomingByte == 'L'){
        digitalWrite(left_fwd,LOW);
        digitalWrite(left_bck,HIGH);
        digitalWrite(right_fwd,HIGH);
        digitalWrite(right_bck,LOW);            
    }    
    if (incomingByte == 'B'){
        digitalWrite(left_fwd,HIGH);
        digitalWrite(left_bck,LOW);
        digitalWrite(right_fwd,LOW);
        digitalWrite(right_bck,HIGH);
    }        
    if (incomingByte == 'F'){
        digitalWrite(left_fwd,LOW);
        digitalWrite(left_bck,HIGH);
        digitalWrite(right_fwd,HIGH);
        digitalWrite(right_bck,LOW);
    }
    if (incomingByte == 'S'){
        digitalWrite(left_fwd,LOW);
        digitalWrite(left_bck,LOW);
        digitalWrite(right_fwd,LOW);
        digitalWrite(right_bck,LOW);

    }
    }
  
}      
