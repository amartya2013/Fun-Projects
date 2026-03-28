from sense_hat import SenseHat
import time

sense = SenseHat()

colors = {
    "green": (0, 255, 0),
    "blue": (0, 153, 255),
    "red": (255, 0, 0),
    "orange": (205, 102, 0),
    "pink": (255, 0, 25),

    "yellow": (255, 255, 0),
    "purple": (128, 0, 128),
    "cyan": (0, 255, 255),
    "magenta": (255, 0, 255),
    "lime": (50, 205, 50),

    "navy": (0, 0, 128),
    "teal": (0, 128, 128),
    "maroon": (128, 0, 0),
    "olive": (128, 128, 0),
    "brown": (139, 69, 19),

    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "gray": (128, 128, 128),
    "silver": (192, 192, 192),
    "gold": (255, 215, 0)
}


while True:
    text = input("What is the text?")
    text_color = input("What color should the text be?")
    background_color = input("What color should background be?")
    if text_color in colors.keys() and background_color in colors.keys():
        sense.show_message(text, text_colour = colors[text_color], back_colour =colors[background_color])
    else:
        print("Please enter valid color inputs")
