from OpenGL.GL import *
from OpenGL.GLUT import *
from brick import *
from ball import *

from time import time_ns
import math
import sys
import random

SCR_WIDTH = 500
SCR_HEIGHT = 500
FRAMERATE = 60

current_frame = 0
current_time = 0

bricks = []
ball = None
sliders = None

px = 100
py = 0
zone = 0


# Nourin
def findZone(x, y, x1, y1):  # zone finding algo
    dx = x1 - x
    dy = y1 - y
    global zone
    if abs(dx) >= abs(dy):
        if dx >= 0 and dy >= 0:
            zone = 0
        elif dx <= 0 and dy >= 0:
            zone = 3
        elif dx <= 0 and dy <= 0:
            zone = 4
        elif dx >= 0 and dy <= 0:
            zone = 7
    else:
        if dx >= 0 and dy >= 0:
            zone = 1
        elif dx <= 0 and dy >= 0:
            zone = 2
        elif dx <= 0 and dy <= 0:
            zone = 5
        elif dx >= 0 and dy <= 0:
            zone = 6
    return zone  # zone finding a


# Nourin
def converttoZone0(x, y, zone):
    x1, y1 = 0, 0
    if zone == 0:
        x1 = x
        y1 = y
    if zone == 1:
        x1 = y
        y1 = x
    elif zone == 2:
        x1 = y
        y1 = -x
    elif zone == 3:
        x1 = -x
        y1 = y
    elif zone == 4:
        x1 = -x
        y1 = -y
    elif zone == 5:
        x1 = -y
        y1 = -x
    elif zone == 6:
        x1 = -y
        y1 = x
    elif zone == 7:
        x1 = x
        y1 = -y
    return x1, y1


# Nourin
def OriginalZone(x, y, zone):
    x1, y1 = 0, 0
    if zone == 0:
        x1 = x
        y1 = y
    if zone == 1:
        x1 = y
        y1 = x
    elif zone == 2:
        x1 = y
        y1 = -x
    elif zone == 3:
        x1 = -x
        y1 = y
    elif zone == 4:
        x1 = -x
        y1 = -y
    elif zone == 5:
        x1 = -y
        y1 = -x
    elif zone == 6:
        x1 = -y
        y1 = x
    elif zone == 7:
        x1 = x
        y1 = -y
    return x1, y1


# Nourin
def drawLine(x, y, x1, y1):
    draw_point(x, y)
    zone = findZone(x, y, x1, y1)
    x0, y0 = converttoZone0(x, y, zone)
    x1, y1 = converttoZone0(x1, y1, zone)
    dx = x1 - x0
    dy = y1 - y0
    d = (2 * dy) - dx
    toE = 2 * dy
    toNE = 2 * (dy - dx)
    x, y = x0, y0
    while x < x1:
        if d <= 0:
            d = d + toE
            x = x + 1
        else:
            d = d + toNE
            x = x + 1
            y = y + 1

        x0, y0 = OriginalZone(x, y, zone)
        draw_point(x0, y0)


# Nourin
def slider(x, y):
    drawLine(x, y, x + 200, y)
    drawLine(x, y + 5, x + 200, y + 5) #fill
    drawLine(x, y + 10, x + 200, y + 10) #fill
    drawLine(x, y + 15, x + 200, y + 15) #fill
    drawLine(x, y + 20, x + 200, y + 20)
    drawLine(x, y, x, y + 20)
    drawLine(x + 200, y, x + 200, y + 20)


# Nourin
def buttons(key, x, y):
    global px, py, sliders
    if px >= 499 - 200:
        px = 490 - 200
        sliders['x'] = 490 - 200
    if px <= 1:
        px = 10
        sliders['x'] = 5
    if key == b'a' and 1 < px < 499 - 200:
        px -= 10
        sliders['x'] = sliders['x'] - 5
    if key == b'd' and 1 < px < 499 - 200:
        px += 10
        sliders['x'] = sliders['x'] + 5
    # glutPostRedisplay()


def init():
    global bricks, ball, sliders
    ball = {
        'x': 100,
        'y': 100,
        'radius': 5,
        'color': (255, 255, 255),
        'dx': 5,
        'dy': 10
    }

    # 20 equally spaced bricks
    for i in range(0, 4):
        for j in range(0, 5):
            bricks.append(
                {
                    'x': 20 + j * 100,
                    'y': 500 - 20 - i * 20,
                    'width': 90,
                    'height': 15,
                    'color': (255, 255, 255)
                }
            )

    sliders = {
        'x': px,
        'y': py,
        'width': 200,
        'height': 20
    }


def drawObjects():
    global bricks, ball
    # draw the ball
    draw_circle_filled((ball['x'], ball['y']), ball['radius'], ball['color'])
    start_time = time_ns()
    # draw the bricks
    for brick in bricks:
        draw_brick(brick['x'], brick['y'], brick['width'], brick['height'], brick['color'])
    print((time_ns() - start_time) / 1000000000)

    # if hit the wall reflect
    if ball['x'] + ball['radius'] >= SCR_WIDTH or ball['x'] - ball['radius'] <= 0:
        ball['dx'] *= -1
    if ball['y'] + ball['radius'] >= SCR_HEIGHT or ball['y'] - ball['radius'] <= 0:
        ball['dy'] *= -1

    # if hit the brick reflect
    remove_brick = None
    for brick in bricks:
        if brick['x'] <= ball['x'] <= brick['x'] + brick['width'] and brick['y'] <= ball['y'] <= brick['y'] + brick[
            'height']:
            ball['dy'] *= -1
            bricks.remove(brick)
            break
        elif brick['x'] <= ball['x'] <= brick['x'] + brick['width'] and brick['y'] <= ball['y'] + ball['radius'] <= \
                brick['y'] + brick['height']:
            ball['dx'] *= -1
            bricks.remove(brick)
            break
        elif brick['x'] <= ball['x'] + ball['radius'] <= brick['x'] + brick['width'] and brick['y'] <= ball['y'] <= \
                brick['y'] + brick['height']:
            ball['dx'] *= -1
            bricks.remove(brick)
            break
        elif brick['x'] <= ball['x'] + ball['radius'] <= brick['x'] + brick['width'] and brick['y'] <= ball['y'] + ball[
            'radius'] <= brick['y'] + brick['height']:
            ball['dy'] *= -1
            bricks.remove(brick)
            break

    # if hit the slider reflect
    if sliders['x'] <= ball['x'] <= sliders['x'] + sliders['width'] and sliders['y'] <= ball['y'] <= sliders['y'] + \
            sliders['height']:
        ball['dy'] *= -1
    elif sliders['x'] <= ball['x'] <= sliders['x'] + sliders['width'] and sliders['y'] <= ball['y'] + ball['radius'] \
            <= sliders['y'] + sliders['height']:
        ball['dx'] *= -1

    # move the ball
    ball['x'] += ball['dx']
    ball['y'] += ball['dy']

    # hit bottom game over
    if ball['y'] <= 0:
        print('Game Over')
        exit(0)


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def show_screen():
    global current_frame, current_time

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    iterate()

    drawObjects()
    slider(px, py)


    # while not time_ns() - current_time >= 1 / FRAMERATE:
    #    pass
    # current_time = time_ns()
    # current_frame += 1
    # if current_frame % FRAMERATE == 0:
    #    current_frame = 0

    glutSwapBuffers()
    glutPostRedisplay()


def main():
    glutInit(sys.argv)
    init()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"DX Ball")
    glutDisplayFunc(show_screen)
    glutKeyboardFunc(buttons)

    glutMainLoop()


if __name__ == "__main__":
    main()
