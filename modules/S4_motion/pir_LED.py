from machine import Pin
from time import sleep

# Set up LED as digital output
LED_PIN = 25        # this pin controls the onboard LED!
led = Pin(LED_PIN,Pin.OUT)

# Set up digital input for PIR sensor
SENSOR_PIN =          # enter pin number here!
pir = Pin(SENSOR_PIN, Pin.IN)

while True:
    led.value(pir.value())
    sleep(0.1)
    