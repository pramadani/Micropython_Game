from ili934xnew import ILI9341, color565
from machine import Pin, SPI, ADC
from time import sleep
import tt32

spi = SPI(0, baudrate=20000000, miso=Pin(20), mosi=Pin(19), sck=Pin(18))
display = ILI9341(spi, cs=Pin(17), dc=Pin(27), rst=Pin(16), w=320, h=240, r=2)

ad_key = ADC(28)

rows = 5
cols = 5

matrix = [[0 for _ in range(cols)] for _ in range(rows)]

pos = [rows // 2, cols // 2]
matrix[pos[0]][pos[1]] = 1

def draw_matrix():
    for i in range(rows):
        for j in range(cols):
            x = j * 20 + 20
            y = i * 20 + 20
            if matrix[i][j] == 1:
                display.fill_rectangle(x, y, 20, 20, color565(0, 255, 0))
            else:
                display.fill_rectangle(x, y, 20, 20, color565(255, 255, 255))

def read_adc():
    while True:
        value = ad_key.read_u16()
        if value <= 500:
            return "left"
        elif value <= 3000:
            return "up"
        elif value <= 6000:
            return "down"
        elif value <= 12000:
            return "right"
        elif value <= 22000:
            return "a"
        sleep(0.1)

def move(position, direction):
    if direction == 'up' and position[0] > 0:
        position[0] -= 1
    elif direction == 'down' and position[0] < rows - 1:
        position[0] += 1
    elif direction == 'left' and position[1] > 0:
        position[1] -= 1
    elif direction == 'right' and position[1] < cols - 1:
        position[1] += 1

while True:
    draw_matrix()
    move_dir = read_adc()
    if move_dir in ['up', 'down', 'left', 'right']:
        matrix[pos[0]][pos[1]] = 0
        move(pos, move_dir)
        matrix[pos[0]][pos[1]] = 1