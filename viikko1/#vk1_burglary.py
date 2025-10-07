#vk1_burglary

import utime
from machine import Pin

pir = Pin(26, Pin.OUT)

while True:
    if pir.value():
        print("Liikettä havaittu!")
    utime.sleep(1)
       
