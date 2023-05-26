#include <Arduino.h>
#include "Led.hpp"

Led::Led(int pin1, int pin2, int pin3)
{
    pinBlueLed = pin1;
    pinGreenLed = pin2;
    pinRedLed = pin3;
}

Led::~Led()
{
}

void Led::setup()
{
    pinMode (pinBlueLed,OUTPUT);
    pinMode (pinRedLed,OUTPUT);
    pinMode (pinGreenLed,OUTPUT);
}
void Led::onBlue()
{
    digitalWrite(pinBlueLed, HIGH);
}
void Led::onGreen()
{
    digitalWrite(pinGreenLed, HIGH);
}
void Led::onRed()
{
    digitalWrite(pinRedLed, HIGH);
}

void Led::offBlue()
{
    digitalWrite(pinBlueLed, LOW);
}
void Led::offGreen()
{
    digitalWrite(pinGreenLed, LOW);
}
void Led::offRed()
{
    digitalWrite(pinRedLed, LOW);
}