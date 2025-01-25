from machine import Pin, PWM
from time import sleep

# set PWM constants and defaults
DUTY_MIN = 0
DUTY_MAX = 65535
DEF_DUTY = int(DUTY_MAX/2)

# set up one DC motor pin as PWM output (to pulse commands)
MOTOR_PIN =           # enter pin number here!
pwm = PWM(Pin(MOTOR_PIN))
pwm.freq(1000)

while True:
    for duty in range(DEF_DUTY, DUTY_MAX, 1):
        pwm.duty_u16(duty)
        sleep(0.0001)
    for duty in range(DUTY_MAX, DEF_DUTY, -1):
        pwm.duty_u16(duty)
        sleep(0.0001)
