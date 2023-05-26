#include<Arduino.h>
#include "Luminosite.hpp"

Luminosite::Luminosite(int pin)
{
    pinCaptor = pin;
}

Luminosite::~Luminosite()
{
}

void Luminosite::setup()
{
    pinMode(pinCaptor, INPUT);
}

int Luminosite::detection()
{
    lumValue = analogRead(pinCaptor);
    return lumValue;
}