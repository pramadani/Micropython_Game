from ili9341 import ILI9341
from machine import Pin, SPI
from time import sleep

spi = SPI(0, baudrate=20000000, miso=Pin(20), mosi=Pin(19), sck=Pin(18))
display = ILI9341(spi, cs=Pin(17), dc=Pin(27), rst=Pin(16), w=320, h=240, r=2)
display.erase()

center_x = 100
center_y = 100
radius = 50
color2 = 0xFFFF

display.draw_circle(center_x, center_y, radius, color2)