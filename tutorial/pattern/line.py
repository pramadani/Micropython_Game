from ili9341 import ILI9341
from machine import Pin, SPI
from time import sleep

spi = SPI(0, baudrate=20000000, miso=Pin(20), mosi=Pin(19), sck=Pin(18))
display = ILI9341(spi, cs=Pin(17), dc=Pin(27), rst=Pin(16), w=320, h=240, r=2)
display.erase()

x1, y1 = 100, 50
x2, y2 = 200, 50
x3, y3 = 150, 150

display.draw_line(x1, y1, x2, y2, 0xffff)
display.draw_line(x2, y2, x3, y3, 0xffff)
display.draw_line(x3, y3, x1, y1, 0xffff)
