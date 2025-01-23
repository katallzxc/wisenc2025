from machine import Pin, PWM
from time import sleep

# set PWM constants and defaults
DUTY_MIN = 0
DUTY_MAX = 65535
DEF_DUTY = int(DUTY_MAX/2)

# set up one DC motor pin as PWM output (to pulse commands)
MOTOR_PIN_1 =           # enter pin number here!
pwm = PWM(Pin(MOTOR_PIN_1))
pwm.freq(1000)

# set up other DC motor pin as digital output to GND
MOTOR_PIN_2 =           # enter pin number here!
dir1 = Pin(MOTOR_PIN_2, Pin.OUT)
dir1.off()
dir2 = Pin(16, Pin.OUT)
dir2.on()


while True:
    for duty in range(DUTY_MIN, DUTY_MAX, 1):
        pwm.duty_u16(duty)
        sleep(0.0001)
    for duty in range(DUTY_MAX, DUTY_MIN, -1):
        pwm.duty_u16(duty)
        sleep(0.0001)
