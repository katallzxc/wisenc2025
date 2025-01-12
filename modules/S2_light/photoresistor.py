from machine import ADC, Pin
import time

# set ADC constants and defaults
ADC_MIN = 0
ADC_MAX = 65535

# set up photoresistor as ADC input
SENSOR_PIN =          # enter pin number here! A0 is GPIO pin 26
photores = ADC(Pin(SENSOR_PIN))

while True:
    percent_of_max = 100*(1 - photores.read_u16()/ADC_MAX)
    print("brightness level: {0}".format(percent_of_max))
    time.sleep(0.1)
