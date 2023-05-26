#include <Arduino.h>
#include "Humidity.hpp"

Humidity::Humidity(int pin)
{
    pinCaptor = pin;
}

Humidity::~Humidity()
{
}

int Humidity::humidityLecture()
{
    captorReading = analogRead(pinCaptor);
    return captorReading;
}

void Humidity::setupSoil()
{
    pinMode(pinCaptor, INPUT);
}