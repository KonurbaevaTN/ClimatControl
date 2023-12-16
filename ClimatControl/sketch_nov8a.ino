#include <ArduinoMqttClient.h>
#include <WiFi.h>
#include "Mqttconnect.h"
#include <TroykaIMU.h>
#include <TroykaMeteoSensor.h>

char ssid[] = SECRET_SSID;        
char pass[] = SECRET_PASS;    

WiFiClient wifiClient;
MqttClient mqttClient(wifiClient);
Barometer barometer;
TroykaMeteoSensor meteoSensor;
const char broker[] = "mqtt.dealgate.ru";
int        port     = 1883;
String topic1 = "12345/pressure";
String topic2 = "12345/temperature";
String topic3 = "12345/humidity";

const long interval = 8000;
unsigned long previousMillis = 0;

int count = 0;

void setup() {
  Serial.begin(9600);
  while (!Serial) {
    ; 
  }
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, HIGH);
  Serial.print("Attempting to connect to WPA SSID: ");
  Serial.println(ssid);
  while (WiFi.begin(ssid, pass) != WL_CONNECTED) {
    Serial.print(".");
    delay(5000);
  }

  Serial.println("You're connected to the network");
  Serial.println();

  Serial.print("Attempting to connect to the MQTT broker: ");
  Serial.println(broker);
  mqttClient.setId("12345");
  mqttClient.setUsernamePassword("Aad606_01", "Abaxp156");
  if (!mqttClient.connect(broker, port)) {
    Serial.print("MQTT connection failed! Error code = ");
    Serial.println(mqttClient.connectError());

    while (1);
  }

  Serial.println("You're connected to the MQTT broker!");
  Serial.println();
  barometer.begin();
  Serial.println();
  meteoSensor.begin();
  Serial.println();
  digitalWrite(LED_BUILTIN, LOW);
}

void loop() {

  mqttClient.poll();

  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;
    digitalWrite(LED_BUILTIN, HIGH);
    int parametr = meteoSensor.read();
    float pressure = barometer.readPressureMillimetersHg();
    float temperature =barometer.readTemperatureC();
    float humidity = meteoSensor.getHumidity();
    mqttClient.beginMessage(topic1);
    mqttClient.print(pressure);
    mqttClient.endMessage();
    mqttClient.beginMessage(topic2);
    mqttClient.print(temperature);
    mqttClient.endMessage();
    mqttClient.beginMessage(topic3);
    mqttClient.print(humidity);
    mqttClient.endMessage();
    Serial.println();
    digitalWrite(LED_BUILTIN, LOW);
  }
}
