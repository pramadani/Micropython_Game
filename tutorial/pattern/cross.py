from ili9341 import ILI9341
from machine import Pin, SPI
from time import sleep

spi = SPI(0, baudrate=20000000, miso=Pin(20), mosi=Pin(19), sck=Pin(18))
display = ILI9341(spi, cs=Pin(17), dc=Pin(27), rst=Pin(16), w=320, h=240, r=2)
display.erase()

center_x, center_y = 160, 120
line_length = 50

display.draw_line(center_x - line_length, center_y - line_length, center_x + line_length, center_y + line_length, 0xffff)
display.draw_line(center_x - line_length, center_y + line_length, center_x + line_length, center_y - line_length, 0xffff)
