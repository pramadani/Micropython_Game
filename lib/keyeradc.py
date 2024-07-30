from machine import ADC
from time import sleep

def read_adc(adc_pin):
    ad_key = ADC(adc_pin)

    while True:
        value = ad_key.read_u16()
        if value <= 1000:
            return "left"
        elif value <= 3000:
            return "up"
        elif value <= 6000:
            return "down"
        elif value <= 12000:
            return "right"
        elif value <= 22000:
            return "a"
        
        sleep(0.1)
        
def test_adc(adc_pin):
    ad_key = ADC(adc_pin)
    while True:
        print(ad_key.read_u16())
        sleep(0.1)