# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import neopixel
from colorpallette import colors

pixel_pin = board.D0

num_pixels = 8

ORDER = neopixel.GRBW

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.07, auto_write=False, pixel_order=ORDER
)
#---- Pallete import ----#
col = [
colors.ORANGE,
colors.PEACH,
colors.CYBER,
colors.MAGENTA,
colors.CYAN,
colors.MINT,
colors.GREEN,
colors.NEON,
colors.YELLOW,

]


l = 0
k = 2


while True:
    #pixels.fill(0)
    #pixels.fill(col[l])
    for i in range(8):
        pixels[i] = (col[k])
        k+= 1
        if k  > 8:
            k = 0
        time.sleep(0.01)
        pixels.show()
    pixels.fill(0)
    time.sleep(0.4)
    pixels.show()
    k-=1
    if k  < 0:
        k = 0



    """#pixels.fill(0)
    l +=1
    k+=1
    #time.sleep(.2)
    pixels[(l-8)] = (col[k])
    if l  > 7:
        l = 0"""










    #rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step
