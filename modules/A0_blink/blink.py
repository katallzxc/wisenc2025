# this code is from Raspberry Pi:
# https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/5

from machine import Pin, Timer
led = Pin(25, Pin.OUT)
led.toggle()
