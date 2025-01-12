from machine import Pin, PWM
from time import sleep

# set PWM constants and defaults
DUTY_MIN = 0
DUTY_MAX = 65535
DEF_DUTY = int(DUTY_MAX/4)
FREQ_MIN = 300
FREQ_MAX = 800
FREQ_STEP = 50

# set up buzzer as PWM output
BUZZER_PIN =           # enter pin number here!
pwm = PWM(Pin(BUZZER_PIN))

while True:
    for f in range(FREQ_MIN,FREQ_MAX,FREQ_STEP):
        # set frequency and start buzzing
        pwm.freq(f)
        pwm.duty_u16(DEF_DUTY)
        sleep(0.5)

        # stop buzzing
        pwm.duty_u16(DUTY_MIN)
        sleep(0.1)
        
    for f in range(FREQ_MAX,FREQ_MIN,-FREQ_STEP):
        # set frequency and start buzzing
        pwm.freq(f)
        pwm.duty_u16(DEF_DUTY)
        sleep(0.5)

        # stop buzzing
        pwm.duty_u16(DUTY_MIN)
        sleep(0.1)
