#include <Wire.h> 
#include <Adafruit_NeoPixel.h>
#include <LiquidCrystal_I2C.h>
#define PIN 5
#define NUMPIXELS 50
Adafruit_NeoPixel pixels (NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);
int R, G, B;
LiquidCrystal_I2C lcd( 0x27 , 16 , 2 );
char k;
bool flag_ind = 0;
unsigned long indTime;
void setup()
{

  Serial.begin(9600);  // initialize serial communications at 9600 bps
  Serial.setTimeout(5);
  /*lcd.init();                      // Инициализация дисплея  
  lcd.backlight();
  
  lcd.setCursor(1,0); 
  lcd.print("Zheka!");*/
  pixels.begin();
  delay(1000);
  pinMode(13, OUTPUT);
}

void loop()
{   
  Serial.flush();
  if (Serial.available()) {
    k = Serial.read();
  //k  = 'b';
   //lcd.setCursor(0,1);              // Установка курсора в начало первой строки
  switch (k) {   //установка нужного цвета
    case 'r':
    R = 255;
    G = 0;
    B = 0;
    //lcd.print("red");
    break;
    case 'o':
    R = 255;
    G = 50;
    B = 0;
    //lcd.print("orange");
    break;
    case 'y':
    R = 255;
    G = 84;
    B = 0;
    //lcd.print("yellow");
    break;
    case 'g':
    R = 0;
    G = 255;
    B = 0;
    //lcd.print("green");
    break;
    case 'e':
    R = 0;
    G = 140;
    B = 147;
    //lcd.print("light blue");
    break;
    case 'b':
    R = 0;
    G = 0;
    B = 255;
    //lcd.print("blue");
    break;
    case 'p':
    R = 100;
    G = 0;
    B = 100;
    //lcd.print("purple");
    break;
    case 'd':
    R = 255;
    G = 255;
    B = 255;
    //lcd.print("day");
    break;
    case 'n':
    R = 0;
    G = 0;
    B = 0;
    //lcd.print("naight");
    break;
    case 't':
    R = 17;
    G = 175;
    B = 214;
    //lcd.print("Turkey");
    break;
    case 'm':
    R = 97;
    G = 231;
    B = 135;
    //lcd.print("Maldives");
    break;
    case 'z':
    R = 255;
    G = 31;
    B = 3;
    //lcd.print("sunset");
    break;
    case 'u':
    R = 255;
    G = 0;
    B = 255;
    //lcd.print("ultraviolet");
    break;
    case 'f':
    flag_ind = 1;
    indTime = millis();
    //lcd.print("indicatia");
    break;
    case 'a':
    R = 255;
    G = 100;
    B = 30;
    //lcd.print("read");
    break;
    case 'x':
    R = 30;
    G = 30;
    B = 30;
    //lcd.print("relax");
    break;
  }
  /*R = 30;
  G = 30;
  B = 30;*/
  // включение нужного света на дисплее LCD
  for (int i = 0; i < NUMPIXELS; i++) {
    pixels.setPixelColor(i, pixels.Color(R, G, B));
    //вывод в монитор порта значений для ленты
    Serial.println("b = " + String(B));
    Serial.println("r = " + String(R));
    Serial.println("g = " + String(G));
    
    pixels.show();
}
if (flag_ind == 1 && millis()-indTime < 500) digitalWrite(13,1);
else digitalWrite(13,0);
  }
}
