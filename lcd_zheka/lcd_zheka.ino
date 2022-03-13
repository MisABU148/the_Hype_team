#include <Wire.h> 
#include <Adafruit_NeoPixel.h>
#include <LiquidCrystal_I2C.h>
#define PIN 5
#define NUMPIXELS 21
Adafruit_NeoPixel pixels (NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);
int R, G, B;
LiquidCrystal_I2C lcd( 0x3F , 16 , 2 );
char k;
void setup()
{

  Serial.begin(9600);  // initialize serial communications at 9600 bps
  Serial.setTimeout(5);
  lcd.init();                      // Инициализация дисплея  
  lcd.backlight();
  pixels.begin();
  lcd.setCursor(1,0); 
  lcd.print("Zheka!");
}

void loop()
{   
  if (Serial.available()) {
    k = Serial.read();
  
   lcd.setCursor(0,1);              // Установка курсора в начало первой строки
  switch (k) {   //установка нужного цвета
    case 'r':
    R = 255;
    G = 0;
    B = 0;
    lcd.print("red");
    break;
    case 'o':
    R = 110;
    G = 7;
    B = 0;
    lcd.print("orange");
    break;
    case 'y':
    R = 255;
    G = 31;
    B = 0;
    lcd.print("yellow");
    break;
    case 'g':
    R = 0;
    G = 255;
    B = 0;
    lcd.print("green");
    break;
    case 'e':
    R = 0;
    G = 40;
    B = 47;
    lcd.print("light blue");
    break;
    case 'b':
    R = 0;
    G = 0;
    B = 255;
    lcd.print("blue");
    break;
    case 'p':
    R = 10;
    G = 0;
    B = 10;
    lcd.print("purple");
    break;
    case 'd':
    R = 255;
    G = 255;
    B = 255;
    lcd.print("day");
    break;
    case 'n':
    R = 0;
    G = 0;
    B = 0;
    lcd.print("naight");
    break;
    case 't':
    R = 17;
    G = 175;
    B = 214;
    lcd.print("Turkey");
    break;
    case 'm':
    R = 97;
    G = 231;
    B = 135;
    lcd.print("Maldives");
    break;
    case 'z':
    R = 15;
    G = 0;
    B = 3;
    lcd.print("sunset");
    break;
    case 'u':
    R = 255;
    G = 0;
    B = 255;
    lcd.print("ultraviolet");
    break;
  }
  // включение нужного света на дисплее LCD
  for (int i = 0; i < NUMPIXELS; i++) {
    pixels.setPixelColor(i, pixels.Color(R, B, G));
    //вывод в монитор порта значений для ленты
    Serial.println("r = " + String(R));
    Serial.println("g = " + String(G));
    Serial.println("b = " + String(B));
    pixels.show();
}
  }
}
