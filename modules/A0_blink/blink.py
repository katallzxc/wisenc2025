# this code is from Raspberry Pi:
# https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/5

from machine import Pin

# set up LED pin as a digital output
LED_PIN = 25        # this pin controls the onboard LED!
led = Pin(LED_PIN, Pin.OUT)

# toggle the LED state (from off to on or on to off)
led.toggle()
