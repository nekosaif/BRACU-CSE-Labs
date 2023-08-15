from OpenGL.GL import *
from OpenGL.GLUT import *

# draw a point
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

# draw a list of points
def draw_points(
        vertices: [(int, int)],
        pixel_size: int = 5,
        pixel_color: (int, int, int) = (255, 255, 255)
):
    for x, y in vertices:
        draw_point(x, y, pixel_size, pixel_color)


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


def draw_circle_filled(
        center_vertex: (int, int) = (0, 0),
        radius: int = 5,
        pixel_color: (int, int, int) = (255, 255, 255)
):
    for i in range(0, radius + 1):
        draw_circle(center_vertex, i, 2, pixel_color)