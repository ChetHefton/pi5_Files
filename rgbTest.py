from gpiozero import RGBLED
from time import sleep

led = RGBLED(red=17, green=27, blue=22)

colors = [
    (1, 0, 0),   # red
    (0, 1, 0),   # green
    (0, 0, 1),   # blue
    (1, 1, 0),   # yellow
    (0, 1, 1),   # cyan
    (1, 0, 1),   # magenta
    (1, 1, 1),   # white
    (0, 0, 0)    # off
]

while True:
    for color in colors:
        led.color = color
        sleep(1)
