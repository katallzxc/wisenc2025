from machine import Pin, PWM
from time import sleep

# set PWM constants and defaults
DUTY_MIN = 0
DUTY_MAX = 65535
DEF_DUTY = int(2*DUTY_MAX/3)

# set up vibration motor as PWM output
MOTOR_PIN =           # enter pin number here!
pwm = PWM(Pin(MOTOR_PIN))
pwm.freq(1000)

while True:
    print("starting new round of vibration")
    for duty in range(DUTY_MIN, DEF_DUTY, 1):
        pwm.duty_u16(duty)
        sleep(0.0001)
    for duty in range(DEF_DUTY, DUTY_MIN, -1):
        pwm.duty_u16(duty)
        sleep(0.0001)
