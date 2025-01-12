# this code is from Raspberry Pi:
# https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/8

from machine import ADC, Pin
import time

# set PWM/ADC constants and defaults
DUTY_MIN = 0
DUTY_MAX = 65535

# set up rotary pot as ADC input
SENSOR_PIN =          # enter pin number here! A0 is GPIO pin 26
rot_pot = ADC(Pin(SENSOR_PIN))

while True:
    percent_of_max = (rot_pot.read_u16()/DUTY_MAX)*100
    print(percent_of_max)
    time.sleep(0.1)
