from ili934xnew import ILI9341
from machine import Pin, SPI
from time import sleep

spi = SPI(0, baudrate=20000000, miso=Pin(20), mosi=Pin(19), sck=Pin(18))
display = ILI9341(spi, cs=Pin(17), dc=Pin(27), rst=Pin(16), w=320, h=240, r=2)
display.erase()

center_x = 100
center_y = 100
radius = 50

def draw_circle(center_x, center_y, radius, color):
    x = radius
    y = 0
    p = 1 - radius

    while x >= y:
        display.pixel(center_x + x, center_y + y, color)
        display.pixel(center_x - x, center_y + y, color)
        display.pixel(center_x + x, center_y - y, color)
        display.pixel(center_x - x, center_y - y, color)
        display.pixel(center_x + y, center_y + x, color)
        display.pixel(center_x - y, center_y + x, color)
        display.pixel(center_x + y, center_y - x, color)
        display.pixel(center_x - y, center_y - x, color)

        y += 1
        if p < 0:
            p += 2 * y + 1
        else:
            x -= 1
            p += 2 * (y - x) + 1

    for y in range(center_y - radius, center_y + radius + 1):
        for x in range(center_x - radius, center_x + radius + 1):
            if (x - center_x) ** 2 + (y - center_y) ** 2 <= radius ** 2:
                display.pixel(x, y, color)

draw_circle(center_x, center_y, radius, color=0xffff)