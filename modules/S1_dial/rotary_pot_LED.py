# this code is from Raspberry Pi:
# https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/8

from machine import ADC, PWM, Pin
import time

# set up LED as PWM output
LED_PIN = 25        # this pin controls the onboard LED!
pwm = PWM(Pin(LED_PIN))
pwm.freq(1000)

# set up rotary pot as ADC input
SENSOR_PIN =          # enter pin number here! A0 is GPIO pin 26
rot_pot = ADC(Pin(SENSOR_PIN))

while True:
    pwm.duty_u16(rot_pot.read_u16())
