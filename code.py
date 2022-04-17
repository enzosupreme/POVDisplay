import time
import random
import digitalio
from digitalio import DigitalInOut, Direction, Pull
import board
import neopixel
from colorpallette import colors

pixel_pin = board.D0
hall_sensor = digitalio.DigitalInOut(board.D2)
hall_sensor.direction = digitalio.Direction.INPUT
hall_sensor.pull = Pull.UP


num_pixels = 8

ORDER = neopixel.GRBW

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.07, auto_write=False, pixel_order=ORDER
)
# ---- Pallete import ----#
col = [
    colors.CYAN,
    colors.PEACH,
    colors.CYBER,
    colors.MAGENTA,
    colors.MINT,
    colors.GREEN,
    colors.RED,
    colors.BLUE,
]


l = 3
k = 0
rainbow = random.randint(0,7)
k = rainbow
x = col[rainbow]


current_mills = 0
previous_mills = 0


letter_a = [ x,x,x,x,0,
             0,0,x,0,x,
             x,x,x,x,0
             ]
letter_b = [x,x,x,x,x,
            x,0,x,0,x,
            0,x,0,x,0,
            0,0,0,0,0
            ]
letter_c = [0,x,x,x,0,
            x,0,0,0,x,
            x,0,0,0,x,
            ]
letter_d = [x,x,x,x,x,
            x,0,0,0,x,
            0,x,x,x,0,
            ]
letter_e = [x,x,x,x,x,
            x,0,x,0,x,
            x,0,x,0,x,
            x,0,x,0,x,
            ]
letter_f = [x,x,x,x,x,
            0,0,x,0,x,
            0,0,x,0,x,
            ]
letter_g = [0,x,x,x,0,
            x,0,0,0,x,
            x,x,x,0,x,
            ]
letter_h = [x,x,x,x,x,
            0,0,x,0,0,
            x,x,x,x,x,
            ]
letter_i = [0,0,0,0,0,
            0,0,0,0,0,
            x,x,x,x,x,
            0,0,0,0,0,
            ]
letter_j = [0,x,0,0,x,
            x,0,0,0,x,
            0,x,x,x,x,
            ]
letter_k = [x,x,x,x,x,
            0,0,x,0,0,
            0,x,0,x,0,
            x,0,0,0,x
            ]
letter_l = [x,x,x,x,x,
            0,0,0,0,x,
            0,0,0,0,x,
            0,0,0,0,x,
            ]
letter_m = [x,x,x,x,x,
            0,0,x,x,0,
            x,x,x,x,x,
            ]
letter_n = [x,x,x,x,x,
            0,x,x,0,0,
            x,x,x,x,x,
            ]
letter_o = [0,x,x,x,0,
            x,0,0,0,x,
            x,0,0,0,x,
            0,x,x,x,0,
            ]
letter_p = [x,x,x,x,x,
            0,0,x,0,x,
            0,0,0,x,0,
            ]
letter_q = [0,0,x,x,0,
            0,0,x,0,x,
            0,x,x,x,x,
            ]
letter_r = [x,x,x,x,x,
            x,0,x,0,0,
            x,0,x,x,0,
            0,x,0,0,x
            ]
letter_s = [x,0,x,x,0,
            x,0,x,0,x,
            0,x,x,0,x,
            ]
letter_t = [0,0,0,0,x,
            x,x,x,x,x,
            0,0,0,0,x,
            ]
letter_u=  [x,x,x,x,x,
            x,0,0,0,0,
            x,x,x,x,x,
            ]
letter_v = [0,x,x,x,0,
            x,0,0,0,0,
            0,x,x,x,0,
            ]
letter_w = [x,x,x,x,0,
            0,x,0,0,0,
            x,x,x,x,0,
            ]
letter_x = [0,x,0,x,0,
            0,0,x,0,0,
            0,x,0,x,0,
            ]
letter_y = [x,x,x,0,0,
            0,0,x,x,x,
            0,0,x,0,0,
            x,x,0,0,0
            ]
letter_z = [x,x,x,0,x,
            x,0,x,0,x,
            x,0,0,x,x,
            ]
number_0 = [x,x,x,x,x,
            x,0,0,0,x,
            x,x,x,x,x,
            ]
number_1 = [x,0,0,x,0,
            x,x,x,x,x,
            x,0,0,0,0,
            ]
number_2 = [x,x,x,0,0,
            x,0,x,0,x,
            x,0,x,x,0,
            ]
number_3 = [0,x,0,x,0,
            x,0,x,0,x,
            x,x,0,x,x,
            ]
number_4 = [0,0,x,0,0,
            0,0,x,x,0,
            x,x,x,x,x,
            ]
number_5 = [x,0,x,x,x,
            x,0,x,0,x,
            x,x,x,0,x,
            ]
number_6= [x,x,x,x,x,
            x,0,x,0,x,
            x,x,x,0,x,
            ]
number_7 = [0,0,0,0,x,
            x,x,x,0,x,
            0,0,0,x,x,
            ]
number_8 = [x,x,x,x,x,
            x,0,x,0,x,
            x,x,x,x,x,
            ]
number_9 = [0,0,x,x,x,
            x,0,x,0,x,
            x,x,x,x,x,
            ]
y = 0

# ---- Delay between characters ----#
space = 0.4
delayTime = 0.000002
blink = 0.006
dlay = random.randint(1,20)




state = 0
lastState = 0
one_rot_time = 0
previous_mills = 0


elapse = 0
elapsed_counter = 0
previous_mills = 0
counter_1 = 0
one_rot_time = 0
time_per_deg = 0


while True:

    l = 3
    k = 0
    rainbow = random.randint(0,7)
    k = rainbow
    x = col[rainbow]



    #print(hall_sensor.value)
    tm = time.monotonic()
    current_mills = tm

    elasped_counter = current_mills - previous_mills
    delayTime = time_per_deg * 3.5
    d = (delayTime * 10)

    def print_Letter(list):
        for i in range(5):
            pixels[i] = list[i]

        pixels.show()
        pixels.fill(0)
        time.sleep(delayTime)
        pixels.show()

        for i in range(5):
            pixels[i] = list[i+5]

        pixels.show()
        pixels.fill(0)
        time.sleep(delayTime)
        pixels.show()

        for i in range(5):
            pixels[i] = list[i+10]

        pixels.show()
        pixels.fill(0)
        time.sleep(delayTime)
        pixels.show()

        for i in range(5):
            pixels[i] = list[i+15]

        pixels.show()
        pixels.fill(0)
        pixels.show()
        #time.sleep(space)

    if((elasped_counter >= time_per_deg * (90)) and (elasped_counter < time_per_deg * (91))):

        time.sleep(d)
        print_Letter(letter_r)
        time.sleep(d)
        print_Letter(letter_i)
        time.sleep(d)
        print_Letter(letter_l)
        time.sleep(d)
        print_Letter(letter_e)
        time.sleep(d)
        print_Letter(letter_y)
        time.sleep(d)


    current_count = tm
    if hall_sensor.value is True:
        counter_1 = current_count

    if hall_sensor.value is False:

        one_rot_time = current_count - counter_1
        time_per_deg = one_rot_time / 360
        previous_mills = tm
        k += 1
        if k > 7:
            k =0

    print(rainbow)



# Write your code here :-)
