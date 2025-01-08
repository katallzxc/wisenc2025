# this code is from Raspberry Pi:
# https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/7

from machine import Pin, PWM
from time import sleep

# set PWM constants and defaults
DUTY_MIN = 0
DUTY_MAX = 65535

# set up LED pin as a PWM output
LED_PIN = 25        # this pin controls the onboard LED!
pwm = PWM(Pin(LED_PIN))
pwm.freq(1000)

# step through duty cycle values to brighten and then dim LED
while True:
    for duty in range(DUTY_MIN, DUTY_MAX+1, 1):
        pwm.duty_u16(duty)
        sleep(0.0001)
    for duty in range(DUTY_MAX, DUTY_MIN-1, -1):
        pwm.duty_u16(duty)
        sleep(0.0001)
