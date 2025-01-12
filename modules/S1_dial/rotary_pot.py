# this code is from Raspberry Pi:
# https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/8

from machine import ADC, Pin
import time

# set ADC constants and defaults
ADC_MIN = 0
ADC_MAX = 65535

# set up rotary pot as ADC input
SENSOR_PIN =          # enter pin number here! A0 is GPIO pin 26
rot_pot = ADC(Pin(SENSOR_PIN))

while True:
    percent_of_max = (rot_pot.read_u16()/ADC_MAX)*100
    print(percent_of_max)
    time.sleep(0.1)
