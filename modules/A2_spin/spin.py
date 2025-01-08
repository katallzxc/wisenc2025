from machine import Pin, PWM
from time import sleep

# set PWM constants and defaults
DUTY_MIN = 0
DUTY_MAX = 1023

# set up DC motor as PWM output
MOTOR_PIN =           # enter pin number here!
pwm = PWM(Pin(MOTOR_PIN))
pwm.freq(1000)

while True:
    for duty in range(DUTY_MIN, DUTY_MAX, 1):
        pwm.duty(duty)
        sleep(0.0001)
    for duty in range(DUTY_MAX, DUTY_MIN, -1):
        pwm.duty(duty)
        sleep(0.0001)
