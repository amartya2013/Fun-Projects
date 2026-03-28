from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

orientation = sense.get_orientation()

roll = orientation['roll']
pitch = orientation['pitch']
yaw = orientation['yaw']

def draw_arrow(direction, color=(255, 0, 0)):
    sense.clear()
    
    arrows = {
        "forward": [  # up ↑
            (3,1),(4,1),
            (2,2),(3,2),(4,2),(5,2),
            (3,3),(4,3),
            (3,4),(4,4),
            (3,5),(4,5),
            (3,6),(4,6)
        ],
        "back": [  # down ↓
            (3,6),(4,6),
            (2,5),(3,5),(4,5),(5,5),
            (3,4),(4,4),
            (3,3),(4,3),
            (3,2),(4,2),
            (3,1),(4,1)
        ],
        "left": [  # ←
            (1,3),(1,4),
            (2,2),(2,3),(2,4),(2,5),
            (3,3),(4,3),(5,3),(6,3),
            (3,4),(4,4),(5,4),(6,4)
        ],
        "right": [  # →
            (6,3),(6,4),
            (5,2),(5,3),(5,4),(5,5),
            (1,3),(2,3),(3,3),(4,3),
            (1,4),(2,4),(3,4),(4,4)
        ]
    }

    if direction not in arrows:
        raise ValueError("Use: forward, back, left, or right")

    for x, y in arrows[direction]:
        sense.set_pixel(x, y, color)

print(f"Roll: {roll} Pitch: {pitch} Yaw: {yaw}")


while True:
    orientation = sense.get_orientation()

    roll = orientation['roll']
    pitch = orientation['pitch']
    yaw = orientation['yaw']

    if roll > 15 and roll < 100:
        print("Forward")
        draw_arrow("back")
    if roll < 345 and roll > 260:
        print("Backward")
        draw_arrow("forward")
    if pitch > 15 and pitch < 100:
        print("Right")
        draw_arrow("left")
    if pitch < 345 and pitch > 260:
        print("left")
        draw_arrow("right")


