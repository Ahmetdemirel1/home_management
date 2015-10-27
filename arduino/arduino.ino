/* config:
digital 12, 11, 10 - blue, green, red LED
*/

byte high_time = 50;
byte incomingByte = 0;

void setup(){
  Serial.begin(9600);
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
}

void send_analog(byte analogPin)
{
  int msg = analogRead(analogPin);
  if(msg < 10) {
    Serial.print("000");
    Serial.println(msg);
  }
  if(msg < 100) {
    Serial.print("00");
    Serial.println(msg);
  }
  if(msg < 1000) {
    Serial.print("0");
    Serial.println(msg);
  }
  if(msg >= 1000) {
    Serial.println(msg);
  }
}

void loop()
{
  if(Serial.available())
  {
    incomingByte = Serial.read();
    if(incomingByte == 97) // a
        digitalWrite(10, LOW); 
    if(incomingByte == 65) // A
        digitalWrite(10, HIGH); 
    if(incomingByte == 98) // b 
        digitalWrite(11, LOW); 
    if(incomingByte == 66) // B
        digitalWrite(11, HIGH); 
    if(incomingByte == 99) // c 
        digitalWrite(12, LOW); 
    if(incomingByte == 67) // C 
        digitalWrite(12, HIGH); 
        
    if(incomingByte == 49) // 1
        send_analog(0);
    if(incomingByte == 50) // 2
        send_analog(1);
  }
}

