from machine import Pin, PWM
from time import sleep

# set PWM constants and defaults
DUTY_MIN = 0
DUTY_MAX = 1023
DEF_DUTY = int(DUTY_MAX/2)

# set up buzzer as PWM output
BUZZER_PIN =           # enter pin number here!
pwm = PWM(Pin(BUZZER_PIN),duty=DUTY_MIN)

while True:
    for f in range(50,700,50):
        # set frequency and start buzzing
        pwm.freq(f)
        pwm.duty(DEF_DUTY)
        sleep(0.5)

        # stop buzzing
        pwm.duty(DUTY_MIN)
        sleep(0.1)
