#vk1_traffic_lights

import utime
from machine import Pin

led_green = Pin(27, Pin.OUT)
led_yellow = Pin(26, Pin.OUT)
led_red = Pin(22, Pin.OUT)
buzz = Pin(0, Pin.OUT)
button = Pin(15, Pin.IN, Pin.PULL_DOWN)

while True:
    if button.value() == 1:
        led_red.value(1)
        for i in range(10):
            buzz.value(1)
            time.sleep(0.2)
            buzz.value(0)
            time.sleep(0.2)
        led_red.value(0)
 
    led_red.value(1)
    utime.sleep(2)
    led_red.value(0)
    led_yellow.value(1)
    utime.sleep(2)
    led_red.value(0)
    led_yellow.value(0)
    led_green.value(1)
    utime.sleep(5)
    led_green.value(0)
    led_yellow.value(1)
    utime.sleep(2)
    led_yellow.value(0)
