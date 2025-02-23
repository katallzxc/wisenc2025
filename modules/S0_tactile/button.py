# this code is from Raspberry Pi:
# https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/6

from machine import Pin
from time import sleep

BUTTON_PIN =          # enter pin number here!
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_DOWN)

while True:
    if button.value():
        print("pressed")
    else:
        print("not pressed")
    sleep(0.05)
