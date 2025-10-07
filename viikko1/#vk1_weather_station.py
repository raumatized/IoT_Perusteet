#vk1_weather_station

from machine import Pin
from time import sleep
from dht import DHT22

sensor = DHT22(Pin(28))

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print("Lämpötila:  {:.1f}°C".format(temp))
        print("Kosteus:  {:.1f}%".format(hum)) 
    except OSError as e:
        print("Sensor read error: ", e)
    
    sleep(2)