#vk1_potentiometer

import time
from machine import ADC, PWM, Pin

led = PWM(Pin(19))
led.freq(6000)
potent = ADC(12)

while True:
    potentValue = potent.read_u16()
    led.duty_u16(potentValue)
    time.sleep(1)

