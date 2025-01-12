from machine import ADC, Pin
import time

# set ADC constants and defaults
ADC_MIN = 0
ADC_MAX = 65535

# set up thermistor as ADC input
SENSOR_PIN =          # enter pin number here! A0 is GPIO pin 26
therm = ADC(Pin(SENSOR_PIN))

while True:
    percent_of_max = 100*(1 - therm.read_u16()/ADC_MAX)
    print("thermal level: {0}".format(percent_of_max))
    time.sleep(0.1)
