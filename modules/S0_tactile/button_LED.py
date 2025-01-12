# this code is from Raspberry Pi:
# https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/6

from machine import Pin
from time import sleep

# set up LED pin as output and button pin as input
LED_PIN = 25        # this pin controls the onboard LED!
BUTTON_PIN =          # enter pin number here!
led = Pin(LED_PIN, Pin.OUT)
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_DOWN)

while True:
    led.value(button.value())
    sleep(0.05)
