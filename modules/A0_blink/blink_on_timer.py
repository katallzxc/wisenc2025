# this code is from Raspberry Pi:
# https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/5

from machine import Pin, Timer

# set up LED pin as a digital output
LED_PIN = 25        # this pin controls the onboard LED!
led = Pin(LED_PIN, Pin.OUT)

# set up blink function that will run on a timer
timer = Timer()
def blink(timer):
    led.toggle()

# initialize timer to call the blink function at a frequency of BLINK_FREQ
BLINK_FREQ = 2.5
timer.init(freq=BLINK_FREQ, mode=Timer.PERIODIC, callback=blink)
