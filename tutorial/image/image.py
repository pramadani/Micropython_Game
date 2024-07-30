from ili9341 import ILI9341
from machine import Pin, SPI

spi = SPI(0, baudrate=20000000, miso=Pin(20), mosi=Pin(19), sck=Pin(18))
display = ILI9341(spi, cs=Pin(17), dc=Pin(27), rst=Pin(16), w=320, h=240, r=2)
display.erase()

data = b'\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00i\xa0i\xa0i\xa0i\xa0\x00\x00\x00\x00\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6\xfe\xf6'
    
display.fill_rectangle(0, 0, display.width, display.height, 0xFFFF)
display.display_block(100, 100, data, 32, 32)