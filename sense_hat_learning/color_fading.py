from sense_hat import SenseHat
import time

sense = SenseHat()
while True:
    for i in range(255):
        sense.clear((255,i,0))
        time.sleep(0.01)

    for i in range(255):
        sense.clear((255,255 - i,0))
        time.sleep(0.01)
sense.clear()
