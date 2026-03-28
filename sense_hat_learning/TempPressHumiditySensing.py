from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

info = {'pressure': sense.get_pressure(), 'temperature': sense.get_temperature(),'humidity' : sense.get_humidity()}

while True:
    asking = input('What information about the environment do you want?')
    if asking in info.keys():
        print(info[asking])
    elif asking = 'quit':
        break
    else:
        print("Please enter 'pressure', 'temperature', or 'humidity'")
