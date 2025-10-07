#weather_station_with_backend

from machine import Pin
from time import sleep
from dht import DHT22
import network
import requests

ssid = 'Wokwi-Guest'
password = ''

THIGSPEAK_API_KEY = 'AS2R4AA0I8E437QD'
THINGSPEAK_URL = 'https://api.thingspeak.com/update'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

print("Wifi connectiong...", end="")
while not wlan.isconnected():
    print(".", end="")
    sleep(0.5)

print("Connected")
print("IP address:", wlan.ifconfig()[0])  
    
sensor = DHT22(Pin(28))

def send_to_thingspeak(temp):
    if temp is None:
        print("No temperature data")
        return
    try:
        response = requests.post( THINGSPEAK_URL, data='api_key={}&field1={}'.format(THIGSPEAK_API_KEY, temp), headers={'Content-Type': 'application/x-www-form-urlencoded'})
        print("Thingspeak response", response.text) 
        response.close()
    except Exception as e:

        print("Failed to send data:", e)


while True:
    try:
        sensor.measure()
        temperature = sensor.temperature()
        print("Lämpötila:  {:.1f}°C".format(temperature))
        send_to_thingspeak(temperature) 
    except OSError as e:
        print("Sensor read error or data sending error: ", e)
    
    sleep(15)