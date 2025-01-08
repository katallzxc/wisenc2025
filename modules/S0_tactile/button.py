# this code is from Raspberry Pi:
# https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/6

from machine import Pin

BUTTON_PIN =          # enter pin number here!
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_DOWN)

while True:
    print(button.value())
    