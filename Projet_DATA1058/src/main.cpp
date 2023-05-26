#include <Arduino.h>
#include "Adafruit_CCS811.h"
#include <SPI.h>

#include "Humidity.hpp"
#include "Led.hpp"
#include "Luminosite.hpp"
#include "Steam.hpp"

Adafruit_CCS811 ccs;

Steam mySteamCaptor(39);
Luminosite lumCaptor(34);
Humidity myHumidity(36);
Led mesLed(19,18,17);

int niveauVap = 0;
int niveauLum = 0;
int niveauHum = 0;

void setup() {
  Serial.begin(9600);

  //capteur de CO2
  if(!ccs.begin()){
    Serial.println("Echec detection capteur CCS811");
    while(1);
  }
  // Attente que le capteur soit pret ...
  while(!ccs.available());

  //capteur de vapeur d'eau
  mySteamCaptor.setupcaptor();

  //capteur d'humidite
  myHumidity.setupSoil();

  //capteur de luminosite
  lumCaptor.setup();

  //led
  mesLed.setup();

}
void loop() {

  //capteur de vapeur d'eau
  niveauVap = mySteamCaptor.steamLecture();

  //capteur d'humidite
  niveauHum = myHumidity.humidityLecture();

  //capteur de luminosite
  niveauLum = (lumCaptor.detection() * 4095) /100;

  if(niveauHum < 2002)
  {
    mesLed.onBlue();
    mesLed.offGreen();
    mesLed.offRed();
  }else if (niveauHum < 500 && niveauHum >3003)
  {
    mesLed.onGreen();
    mesLed.offBlue();
    mesLed.offRed();
  }else if (niveauHum > 3003)
  {
    mesLed.onRed();
    mesLed.offBlue();
    mesLed.offBlue();
  }

  //capteur de CO2
  if(ccs.available()){
    if(!ccs.readData()){
      // Serial.print("CO2 : ");
      // Serial.print(ccs.geteCO2());
      // Serial.print("ppm, TVOC : ");
      // Serial.println(ccs.getTVOC());
    }
    else{
      Serial.println("Erreur !");
      while(1);
    }
  }

  // Serial.print("le niveau de vapeur d'eau degagee est : ");
  // Serial.println(niveauVap);

  // Serial.print("le niveau d'humidite du sol est : ");
  // Serial.println(niveauHum);

  Serial.print("la valeur de luminosite est : ");
  Serial.print(niveauLum);
  Serial.println(" %");

  // Serial.println("-------------------------------------");

  delay(5000);

}