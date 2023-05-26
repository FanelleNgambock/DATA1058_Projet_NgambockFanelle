#include <Arduino.h>
#include "Steam.hpp"

Steam::Steam(int pin)
{
    pinCaptor = pin;
}

Steam::~Steam()
{
}

int Steam::steamLecture()
{
   
   sensorValue = analogRead(pinCaptor);   //connect Steam sensors to Analog 0
   return sensorValue;
}

void Steam::setupcaptor()
{
    pinMode(pinCaptor, INPUT);
}