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


def draw_points(
        vertices: [(int, int)],
        pixel_size: int = 5,
        pixel_color: (int, int, int) = (255, 255, 255)
):
    for x, y in vertices:
        draw_point(x, y, pixel_size, pixel_color)


def draw_line(
        start_vertex: [(int, int)],
        end_vertex: [(int, int)],
        pixel_size: int = 5,
        pixel_color: (int, int, int) = (255, 255, 255)
):
    vertices = MidPointLine(start_vertex, end_vertex).mid_point_calculate()
    draw_points(vertices, pixel_size, pixel_color)


class MidPointLine:
    def __init__(self,
                 start_vertex: (int, int) = (0, 0),
                 end_vertex: (int, int) = (1, 1)
                 ):
        self.x1, self.y1 = start_vertex
        self.x2, self.y2 = end_vertex

        self.original_octant = self.find_octant()

        octant_1_start_vertex, octant_1_end_vertex = self.convert_to_octant_1(
            [(self.x1, self.y1), (self.x2, self.y2)],
            self.original_octant
        )
        self.x1, self.y1, self.x2, self.y2 = *octant_1_start_vertex, *octant_1_end_vertex

        self.dx, self.dy = self.x2 - self.x1, self.y2 - self.y1
        self.d_init = 2 * self.dy - self.dx
        self.del_NE = 2 * (self.dy - self.dx)
        self.del_E = 2 * self.dy

    def find_octant(self):
        dx, dy = self.x2 - self.x1, self.y2 - self.y1
        if dx >= 0 and dy >= 0:
            if dx >= dy:
                return 1
            else:
                return 2
        elif dx < 0 < dy:
            if abs(dx) >= dy:
                return 4
            else:
                return 3
        elif dx <= 0 and dy <= 0:
            if abs(dx) >= abs(dy):
                return 5
            else:
                return 6
        elif dx > 0 > dy:
            if abs(dx) >= abs(dy):
                return 8
            else:
                return 7

    @classmethod
    def convert_to_octant_1(cls,
                            vertices: [(int, int)],
                            original_octant: int):
        conversion_dict = {
            1: lambda x, y: (x, y),
            2: lambda x, y: (y, x),
            3: lambda x, y: (-y, x),
            4: lambda x, y: (-x, y),
            5: lambda x, y: (-x, -y),
            6: lambda x, y: (-y, -x),
            7: lambda x, y: (y, -x),
            8: lambda x, y: (x, -y),
        }

        for i in range(len(vertices)):
            vertices[i] = conversion_dict[original_octant](*vertices[i])

        return vertices

    @classmethod
    def convert_to_original_octant(cls,
                                   vertices: [(int, int)],
                                   original_octant: int):
        conversion_dict = {
            1: lambda x, y: (x, y),
            2: lambda x, y: (y, x),
            3: lambda x, y: (y, -x),
            4: lambda x, y: (-x, y),
            5: lambda x, y: (-x, -y),
            6: lambda x, y: (-y, -x),
            7: lambda x, y: (-y, x),
            8: lambda x, y: (x, -y),
        }

        for i in range(len(vertices)):
            vertices[i] = conversion_dict[original_octant](*vertices[i])

        return vertices

    def mid_point_calculate(self):
        lst_points = []
        x_i, y_i, d_i = self.x1, self.y1, self.d_init
        while not (x_i == self.x2 and y_i == self.y2):
            lst_points.append((x_i, y_i))
            if d_i > 0:
                d_i += self.del_NE
                x_i += 1
                y_i += 1
            else:
                d_i += self.del_E
                x_i += 1
        return self.convert_to_octant_1(lst_points, self.original_octant)


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
        vertices = \
            get_lines_for_seven_segment_digit(int(digit),
                                              pos=(pos[0] + (size * (i + 1)) + (padding * i), pos[1]),
                                              size=size)
        for j in range(0, len(vertices) - 1, 2):
            draw_line(vertices[j], vertices[j + 1],
                      pixel_size=1)


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

    num = input("Enter a number: ")
    draw_number(num=num, pos=(150, 150), size=20, padding=10)

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice")
glutDisplayFunc(show_screen)

glutMainLoop()
