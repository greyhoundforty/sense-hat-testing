from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.color.gain = 64
sense.color.integration_cycles = 64

while True:
    sleep(2 * sense.colour.integration_time)
    red, green, blue, clear = sense.colour.colour # readings scaled to 0-256
    print(f"R: {red}, G: {green}, B: {blue}, C: {clear}")
