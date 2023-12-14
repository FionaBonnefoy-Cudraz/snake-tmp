###Q1

# import pyxel

# def update():
#     if pyxel.btnp(pyxel.KEY_Q):
#         pyxel.quit()

# def draw():
#     pyxel.cls(0)
#     color = pyxel.frame_count % 16
#     pyxel.text(56, 54, "Hello, Snake!", color)

# pyxel.init(160, 120)
# pyxel.run(update, draw)



# ##Q2
# import pyxel
# import time

# def update():
#     if pyxel.btnp(pyxel.KEY_Q):
#         pyxel.quit()

# t = 0.0

# def draw():
#     global t
#     t_new = time.time()
#     dt = t_new - t
#     t = t_new
#     fps = 1.0 / dt
#     fps = int(round(fps))
#     pyxel.cls(0)
#     color = pyxel.frame_count % 16
#     pyxel.text(56, 54, "Hello, Snake!", color)
#     pyxel.text(0, 0, f"fps: {fps}", 7)

# pyxel.init(160, 120)
# pyxel.run(update, draw)



##Q3

# import pyxel

# def update():
#     if pyxel.btnp(pyxel.KEY_Q):
#         pyxel.quit()

# def draw():
#     pyxel.cls(13)
#     for i in range(30):
#         for j in range(30):
#             if (i+j) % 2 == 0:
#                 pyxel.pset(i, j, 7)

# pyxel.init(30, 30)
# pyxel.run(update, draw)



# ##Q4

# import pyxel
# import random as rd 

# def update():
#     if pyxel.btnp(pyxel.KEY_Q):
#         pyxel.quit()

# endroit = [rd.randrange(0,29,1), rd.randrange(0,29,1)]

# def draw():
#     pyxel.cls(13)
#     for i in range(30):
#         for j in range(30):
#             if (i+j) % 2 == 0:
#                 pyxel.pset(i, j, 7)
#     pyxel.pset(endroit[0], endroit[1], 8)

# pyxel.init(30, 30)
# pyxel.run(update, draw)

##Q5

import pyxel

pyxel.init(30, 30)

fruit = [pyxel.rndi(0, 29),pyxel.rndi(0, 29)]

snake_geometry = [[10, 15],[11, 15],[12, 15]]

checkerboard = False

arrow_keys = [
    pyxel.KEY_UP,
    pyxel.KEY_DOWN,
    pyxel.KEY_LEFT,
    pyxel.KEY_RIGHT
]

def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    arrow_keys_pressed = []
    for key in arrow_keys:
        if pyxel.btnp(key):
            arrow_keys_pressed.append(key)
    for key in arrow_keys_pressed:
        if key == pyxel.KEY_UP:
            print("↑")
        elif key == pyxel.KEY_DOWN:
            print("↓")
        elif key == pyxel.KEY_LEFT:
            print("←")
        elif key == pyxel.KEY_RIGHT:
            print("→")

def draw():
    pyxel.cls(7)
    for i in range(30):
        for j in range(30):
             if (i+j) % 2 == 0:
                 pyxel.pset(i, j, 7)
    pyxel.pset(fruit[0], fruit[1], 8)
    for x, y in snake_geometry[:-1]:
        pyxel.pset(x, y, 3)
    snake_head = snake_geometry[-1]
    pyxel.pset(snake_head[0], snake_head[1], 11)

pyxel.run(update, draw)
