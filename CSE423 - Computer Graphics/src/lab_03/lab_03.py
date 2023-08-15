from math import sqrt, cos, sin, pi

from OpenGL.GL import *
from OpenGL.GLUT import *


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


def draw_circle(
        center_vertex: (int, int) = (0, 0),
        radius: int = 5,
        pixel_size: int = 5,
        pixel_color: (int, int, int) = (255, 255, 255)
):
    d = 1 - radius
    x, y = 0, radius

    while x <= y:
        draw_point(x + center_vertex[0], y + center_vertex[1], pixel_size, pixel_color)
        draw_point(y + center_vertex[0], x + center_vertex[1], pixel_size, pixel_color)
        draw_point(-x + center_vertex[0], y + center_vertex[1], pixel_size, pixel_color)
        draw_point(-y + center_vertex[0], x + center_vertex[1], pixel_size, pixel_color)
        draw_point(-x + center_vertex[0], -y + center_vertex[1], pixel_size, pixel_color)
        draw_point(-y + center_vertex[0], -x + center_vertex[1], pixel_size, pixel_color)
        draw_point(x + center_vertex[0], -y + center_vertex[1], pixel_size, pixel_color)
        draw_point(y + center_vertex[0], -x + center_vertex[1], pixel_size, pixel_color)

        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1
        x += 1


def circular_rosette_with_n_petal(
        center_vertex: (int, int) = (0, 0),
        radius: int = 5,
        n: int = 5,
        pixel_size: int = 1,
        pixel_color: (int, int, int) = (255, 255, 255)
):
    circle_vertices = []
    for i in range(n):
        circle_vertices.append((
            round(center_vertex[0] + (radius/2) * cos(2 * pi * i / n)),
            round(center_vertex[1] + (radius/2) * sin(2 * pi * i / n))
        ))
    for x, y in circle_vertices:
        draw_circle((x, y), radius/2, pixel_size, pixel_color)
    draw_circle(center_vertex, radius, pixel_size, pixel_color)


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def show_screen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    circular_rosette_with_n_petal((250, 250), int(100), 100)

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice")
glutDisplayFunc(show_screen)

glutMainLoop()
