#vk1 onboard led blink

from machine import Pin, Timer
import time 

led = Pin('LED', Pin.OUT)
timer = Timer()

def blink(timer)
    led.toggle()

timer.init(mode=Timer.PERIODIC, freq=2, callback=blink)