from ili9341 import ILI9341
from machine import Pin, SPI

spi = SPI(0, baudrate=20000000, miso=Pin(20), mosi=Pin(19), sck=Pin(18))
display = ILI9341(spi, cs=Pin(17), dc=Pin(27), rst=Pin(16), w=320, h=240, r=2)
display.erase()

blue = (0, 0, 255)
green = (0, 255, 0)

display.draw_gradient(50, 50, 100, 100, blue, green)