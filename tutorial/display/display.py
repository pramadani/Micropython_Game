from ili9341 import ILI9341
from machine import Pin, SPI
from time import sleep

spi = SPI(0, baudrate=20000000, miso=Pin(20),mosi=Pin(19), sck=Pin(18))
display = ILI9341(spi, cs=Pin(17), dc=Pin(27), rst=Pin(16), w=320, h=240, r=2)

while True:
    display.fill_rectangle(0, 0, display.width, display.height, 0xfc04)
    sleep(2)
    display.fill_rectangle(0, 0, display.width, display.height, 0)
    sleep(2)
