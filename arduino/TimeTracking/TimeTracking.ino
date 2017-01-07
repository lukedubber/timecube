/*
 * MFRC522 - Library to use ARDUINO RFID MODULE KIT 13.56 MHZ WITH TAGS SPI W AND R BY COOQROBOT.
 * The library file MFRC522.h has a wealth of useful info. Please read it.
 * The functions are documented in MFRC522.cpp.
 *
 * Based on code Dr.Leong   ( WWW.B2CQSHOP.COM )
 * Created by Miguel Balboa (circuitito.com), Jan, 2012.
 * Rewritten by Søren Thing Andersen (access.thing.dk), fall of 2013 (Translation to English, refactored, comments, anti collision, cascade levels.)
 * Released into the public domain.
 *
 * Sample program showing how to read data from a PICC using a MFRC522 reader on the Arduino SPI interface.
 *----------------------------------------------------------------------------- empty_skull 
 * Aggiunti pin per arduino Mega
 * add pin configuration for arduino mega
 * http://mac86project.altervista.org/
 ----------------------------------------------------------------------------- Nicola Coppola
 * Pin layout should be as follows:
 * Signal     Pin              Pin               Pin
 *            Arduino Uno      Arduino Mega      MFRC522 board
 * ------------------------------------------------------------
 * Reset      9                5                 RST
 * SPI SS     10               53                SDA
 * SPI MOSI   11               51                MOSI
 * SPI MISO   12               50                MISO
 * SPI SCK    13               52                SCK
 *
 * The reader can be found on eBay for around 5 dollars. Search for "mf-rc522" on ebay.com. 
 */

#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN 10
#define RST_PIN 9
MFRC522 mfrc522(SS_PIN, RST_PIN);  // Create MFRC522 instance.

byte readCard[4];
//byte oldCard[4];
String currentCard;
String oldCard = "00000000"; //oldCard[8];
int redPin = 5;
int greenPin = 4;
int bluePin = 3;
int counter = 0;
long waitTime = 15;
long gaaa = 0;
int maxCounter = 5;

void setup() {
  Serial.begin(9600); // Initialize serial communications with the PC
  SPI.begin();      // Init SPI bus
  mfrc522.PCD_Init(); // Init MFRC522 card
  //Setup the LED feedback.
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  waitTime = minstosec(waitTime);
  Serial.println(gaaa);
}

void loop() {
  // Look for new cards
  if ( ! mfrc522.PICC_IsNewCardPresent()) {
    return;
  }

  // Select one of the cards
  if ( ! mfrc522.PICC_ReadCardSerial()) {
    return;
  }  
  currentCard = "";
  for (int i = 0; i < 4; i++) {  //
    readCard[i] = mfrc522.uid.uidByte[i];
    currentCard = currentCard + String(mfrc522.uid.uidByte[i], HEX);
  }
  if(currentCard != oldCard) {
    Serial.print(currentCard);
    oldCard = currentCard;
    Serial.println();
    setColor(0, 255, 0); // green, we have read data
    delay(2000);
    setColor(0, 0, 0); // off
    counter = 0;
  }
  else {
    counter++;
    //Serial.println(counter);
    //Serial.println(waitTime)
    if(counter > waitTime)
    {
      //Serial.println(counter);
      //Serial.println(waitTime);
      for(long i=0; i<=40; i++)
      {
        setColor(random(255), random(255), random(255)); // green, we have read data
        delay(100);
        Serial.println(i);
      }
      setColor(0,0,0);
      counter = 0;
    }
    delay(1000);
    
  }
}

long minstosec(long waitTimeMins)
{
  return (waitTimeMins * 60);
}

void setColor(int red, int green, int blue)
{
  analogWrite(redPin, red);
  analogWrite(greenPin, green);
  analogWrite(bluePin, blue);
}
