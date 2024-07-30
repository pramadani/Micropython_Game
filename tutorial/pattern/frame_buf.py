from ili934xnew import ILI9341
from machine import Pin, SPI
import framebuf

# Initialize SPI and ILI9341 display
spi = SPI(0, baudrate=20000000, miso=Pin(20), mosi=Pin(19), sck=Pin(18))
display = ILI9341(spi, cs=Pin(17), dc=Pin(27), rst=Pin(16), w=320, h=240, r=2)
display.erase()

# # Define buffer dimensions
# buffer_width = 64
# buffer_height = 32

# # Create buffer for RGB565 format
# buffer = bytearray(buffer_width * buffer_height * 2)  # Each pixel is 2 bytes
# fb = framebuf.FrameBuffer(buffer, buffer_width, buffer_height, framebuf.RGB565)

# # Clear the buffer (optional)
# fb.fill(0x0000)  # Fill with black color in RGB565

# # Draw a rectangle at position (50, 50) with width 64 and height 32
# rect_x = 0
# rect_y = 0
# rect_width = 64
# rect_height = 32
# rect_color = 0xFFFF  # Red color in RGB565 format
# for y in range(rect_y, rect_y + rect_height):
#     for x in range(rect_x, rect_x + rect_width):
#         fb.pixel(x, y, rect_color)

def framebuffer_to_rgb565(fb, x0, y0, x1, y1):
    width = x1 - x0 + 1
    height = y1 - y0 + 1
    data = bytearray(width * height * 2)  # 2 bytes per pixel for RGB565
    fb_frame = framebuf.FrameBuffer(data, width, height, framebuf.RGB565)

    for y in range(height):
        for x in range(width):
            pixel_color = fb.pixel(x + x0, y + y0)
            fb_frame.pixel(x, y, pixel_color)
    
    display._writeblock(x0, y0, x1, y1, data)

def write_fb_to_display(display, fb, x0, y0, x1, y1):
    # Ambil data dari framebuffer
    data = framebuffer_to_rgb565(fb, x0, y0, x1, y1)
    
    # Tulis data ke tampilan
    display._writeblock(x0, y0, x1, y1, data)


buf = bytearray(128 * 128 * 2)  # RGB565 format
fb = framebuf.FrameBuffer(buf, 128, 128, framebuf.RGB565)

# Gambar sesuatu pada framebuffer
fb.fill(0)  # Clear with black
fb.text('Hello World!', 0, 0, 0xFFFF)  # Put white text

# Menulis framebuffer ke tampilan
write_framebuffer_to_display(display, fb, 0, 0, 127, 127)