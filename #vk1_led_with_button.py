#vk1_led_with_button

import time
from machine import Pin

led = Pin(19, Pin.OUT)
button = Pin(12, Pin.IN, Pin.PULL_DOWN)

while True:
    if button.value():
        led.value(True)
    else:
        led.value(False)