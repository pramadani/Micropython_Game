from ili9341 import ILI9341
from machine import Pin, SPI
import framebuf

spi = SPI(0, baudrate=20000000, miso=Pin(20), mosi=Pin(19), sck=Pin(18))
display = ILI9341(spi, cs=Pin(17), dc=Pin(27), rst=Pin(16), w=320, h=240, r=2)
display.erase()

buf = bytearray(128 * 128 * 2)
fb = framebuf.FrameBuffer(buf, 128, 128, framebuf.RGB565)

fb.fill(0xFFFF)

display.draw_framebuf(fb, 0, 0, 127, 127)