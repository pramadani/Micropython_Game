from ili9341 import ILI9341
from machine import Pin, SPI
import glcdfont
import tt14
import tt24
import tt32

fonts = [glcdfont,tt14,tt24,tt32]
text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'

spi = SPI(0, baudrate=20000000, miso=Pin(20), mosi=Pin(19), sck=Pin(18))
display = ILI9341(spi, cs=Pin(17), dc=Pin(27), rst=Pin(16), w=320, h=240, r=2)

display.erase()
for ff in fonts:
    display.set_font(ff)
    display.print(text)
