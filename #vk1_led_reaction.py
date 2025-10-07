#vk1_led_reaction

import utime
import urandom
from machine import Pin

led = Pin(24, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

timer_start = 0

def button_handler(pin):
    button.irq(handler=None)
    reaction_time = utime.ticks_diff(utime.ticks_ms(), timer_start)
    print("Reaktioaikasi oli:" + str(reaction_time) + " millisekuntia")
    print("Ohjelma valmis")

led.value(1)
utime.sleep(urandom.uniforms(5, 10))

led.value(0)
timer_start= utime.ticks_ms()

button.irq(trigger=Pin.IRQ_RISING, handler=button_handler)