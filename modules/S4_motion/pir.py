from machine import Pin
from time import sleep

# Set up digital input for PIR sensor
SENSOR_PIN =          # enter pin number here!
pir = Pin(SENSOR_PIN, Pin.IN)

while True:
    print(pir.value())
    sleep(0.1)
    