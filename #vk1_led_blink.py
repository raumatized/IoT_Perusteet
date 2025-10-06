#vk1_led_blink

from machine import Pin, Timer 
import time 

led = Pin(24, Pin.OUT)

timer = Timer()

def blink(timer)
    led.toggle()

timer.init(mode=Timer.PERIODIC, freq=10, callback=blink)