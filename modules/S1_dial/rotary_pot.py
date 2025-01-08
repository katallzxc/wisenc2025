# this code is from Raspberry Pi:
# https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/8

from machine import ADC, Pin
import time

SENSOR_PIN =          # enter pin number here! A0 is GPIO pin 26
rot_pot = ADC(Pin(SENSOR_PIN))

while True:
    print(rot_pot.read_u16())
    time.sleep(1)