from random import randint

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_point(
        x: int, y: int,
        pixel_size: int = 5,
        pixel_color: (int, int, int) = (255, 255, 255)
):
    glPointSize(pixel_size)
    glColor3ub(*pixel_color)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def draw_points(
        vertices: [(int, int)],
        pixel_size: int = 5,
        pixel_color: (int, int, int) = (255, 255, 255)
):
    for x, y in vertices:
        draw_point(x, y, pixel_size, pixel_color)


def draw_lines(
        vertices: [(int, int)],
        line_type: GLenum = GL_LINES,
        line_width: int = 5,
        line_color: (int, int, int) = (255, 255, 255)
):
    glPointSize(line_width)
    glColor3ub(*line_color)
    glBegin(line_type)
    for x, y in vertices:
        glVertex2f(x, y)
    glEnd()


def draw_polygon(
        vertices: [(int, int)],
        line_type: GLenum = GL_LINES,
        line_width: int = 5,
        line_color: (int, int, int) = (255, 255, 255)
):
    for i in range(len(vertices)):
        draw_lines([vertices[i], vertices[(i + 1) % len(vertices)]], line_type, line_width, line_color)


def draw_square(vertex: (int, int),
                side_len: int = 50,
                line_width: int = 5,
                line_color: (int, int, int) = (255, 255, 255)
                ):
    vertices = [
        (vertex[0], vertex[1]),
        (vertex[0], vertex[1] + side_len),
        (vertex[0] + side_len, vertex[1] + side_len),
        (vertex[0] + side_len, vertex[1])
    ]
    draw_polygon(vertices, GL_LINES, line_width, line_color)


def draw_text(pos: (int, int),
              text: str,
              font: int = GLUT_BITMAP_TIMES_ROMAN_24,
              text_color: (int, int, int) = (255, 255, 255)
              ):
    glColor3ub(*text_color)
    glRasterPos2f(pos[0], pos[1])
    GLUT.glutBitmapString(font, text.encode('ascii'))


def get_lines_for_seven_segment_digit(digit: int,
                                      pos: (int, int) = (100, 100),
                                      size: int = 50):
    segment_lines = {
        0: [0, 1, 2, 3, 4, 5],
        1: [1, 2],
        2: [0, 1, 3, 4, 6],
        3: [0, 1, 2, 3, 6],
        4: [1, 2, 5, 6],
        5: [0, 2, 3, 5, 6],
        6: [0, 2, 3, 4, 5, 6],
        7: [0, 1, 2],
        8: [0, 1, 2, 3, 4, 5, 6],
        9: [0, 1, 2, 3, 5, 6]
    }

    lines_coords = {
        0: [(pos[0], pos[1] + 2 * size), (pos[0] + size, pos[1] + 2 * size)],
        1: [(pos[0] + size, pos[1] + size), (pos[0] + size, pos[1] + 2 * size)],
        2: [(pos[0] + size, pos[1]), (pos[0] + size, pos[1] + size)],
        3: [(pos[0], pos[1]), (pos[0] + size, pos[1])],
        4: [(pos[0], pos[1] + size), (pos[0], pos[1])],
        5: [(pos[0], pos[1] + 2 * size), (pos[0], pos[1] + size)],
        6: [(pos[0], pos[1] + size), (pos[0] + size, pos[1] + size)]
    }

    return [j for i in segment_lines[digit] for j in lines_coords[i]]


def draw_number(num: str,
                pos: (int, int) = (50, 50),
                size: int = 50,
                padding: int = 10):
    for i, digit in enumerate(num):
        #print(get_lines_for_seven_segment_digit(int(digit)))
        draw_lines(
            get_lines_for_seven_segment_digit(int(digit),
                                              pos=(pos[0] + (size * (i + 1)) + (padding * i), pos[1]),
                                              size=size))


def task1():
    for _ in range(50):
        x, y = randint(0, glutGet(GLUT_WINDOW_WIDTH)), randint(0, glutGet(GLUT_WINDOW_HEIGHT))
        r, g, b = randint(0, 256), randint(0, 256), randint(0, 256)
        draw_point(x, y, 5, (r, g, b))


def task2():
    draw_square((100, 20), 300)
    draw_square((100 + 25, 20 + 150 + 20), 100)
    draw_square((100 + 25 + 150, 20 + 150 + 20), 100)
    draw_square((100 + 50 + 50, 20), 100)
    draw_lines([(100 + 150, 20), (100 + 150, 20 + 100)])
    draw_point(100 + 150 - 10, 20 + 50)
    draw_point(100 + 150 + 10, 20 + 50)
    draw_polygon([(100, 20 + 300), (100 + 300, 20 + 300), (100 + 150, 20 + 300 + 150)])


def task3():
    draw_number(num='20101416', pos=(200, 350), size=10, padding=4)


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    task1()
    task2()
    task3()

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice")
glutDisplayFunc(showScreen)

glutMainLoop()
