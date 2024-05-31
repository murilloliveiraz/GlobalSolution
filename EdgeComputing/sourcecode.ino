#include "LiquidCrystal.h"

// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
int cm = 0;
int buzzer = 10;

void setup()
{
  Serial.begin(9600);
  lcd.begin(16, 2);
  pinMode(buzzer,OUTPUT); 
}

void loop()
{
  lcd.clear();
  // mede o tempo em cm
  cm = 0.01723 * readUltrasonicDistance(7, 7);
  
  if (cm >= 200) { 
    lcd.setCursor(0, 0); 
    lcd.print("CUIDADO!");
    lcd.setCursor(0, 1); 
    lcd.print("MARE ALTA!"); 
    tone(buzzer,261); 
  } 
  else if (cm >= 100 && cm < 200) 
  { 
    lcd.setCursor(0, 0); 
    lcd.print("MARE OK!"); // Exibe a mensagem "MARE OK!" no LCD
  } 
  else 
  { 
    lcd.setCursor(0, 0); 
    lcd.print("CUIDADO!"); 
    lcd.setCursor(0, 1); 
    lcd.print("MARE BAIXA!"); // Exibe a mensagem "MARE BAIXA!" no LCD
  	tone(buzzer,261); 
  }
  
  delay(1000);
  lcd.clear();
  
  lcd.setCursor(0, 0);
  lcd.print("Altura da Mare:");
  lcd.setCursor(0, 1);
  lcd.print(cm);
  lcd.setCursor(3, 1);
  lcd.print(" cm");
  
  noTone(buzzer);
  
  delay(1000);
}


long readUltrasonicDistance(int triggerPin, int echoPin)
{
  pinMode(triggerPin, OUTPUT);  // Clear the trigger
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2);
  // Sets the trigger pin to HIGH state for 10 microseconds
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);
  pinMode(echoPin, INPUT);
  // Reads the echo pin, and returns the sound wave travel time in microseconds
 
  return pulseIn(echoPin, HIGH);
}


















