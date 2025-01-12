from machine import Pin
from time import sleep

# Set up digital input for PIR sensor
SENSOR_PIN =          # enter pin number here!
pir = Pin(SENSOR_PIN, Pin.IN)

while True:
    if pir.value():
        print("motion detected!")
    else:
        print("no motion detected")
    sleep(0.1)
    