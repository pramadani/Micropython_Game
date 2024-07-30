from ili934xnew import ILI9341, color565
from machine import Pin, SPI
from time import sleep

spi = SPI(0, baudrate=20000000, miso=Pin(20), mosi=Pin(19), sck=Pin(18))
display = ILI9341(spi, cs=Pin(17), dc=Pin(27), rst=Pin(16), w=320, h=240, r=2)
display.erase()

blue = (0, 0, 255)
green = (0, 255, 0)

def draw_gradient(x, y, width, height, c1, c2):
    for i in range(width):
        ratio = i / width
        r = int(c1[0] * (1 - ratio) + c2[0] * ratio)
        g = int(c1[1] * (1 - ratio) + c2[1] * ratio)
        b = int(c1[2] * (1 - ratio) + c2[2] * ratio)
        color = color565(r, g, b)
        
        display.fill_rectangle(x + i, y, 1, height, color)

draw_gradient(50, 50, 100, 100, blue, green)