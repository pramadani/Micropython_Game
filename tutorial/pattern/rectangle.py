from ili9341 import ILI9341
from machine import Pin, SPI
from time import sleep

spi = SPI(0, baudrate=20000000, miso=Pin(20), mosi=Pin(19), sck=Pin(18))
display = ILI9341(spi, cs=Pin(17), dc=Pin(27), rst=Pin(16), w=320, h=240, r=2)
display.erase()

x_start = 50
y_start = 50
box_width = 100
box_height = 100

display.fill_rectangle(x_start, y_start, box_width, box_height, color=0xffff)