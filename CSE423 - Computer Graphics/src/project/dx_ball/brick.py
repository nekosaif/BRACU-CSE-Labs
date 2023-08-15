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


def draw_line(
        start_vertex: [(int, int)],
        end_vertex: [(int, int)],
        pixel_size: int = 5,
        pixel_color: (int, int, int) = (255, 255, 255)
):
    vertices = MidPointLine(start_vertex, end_vertex).mid_point_calculate()
    draw_points(vertices, pixel_size, pixel_color)


def draw_brick(
        x: int, y: int,
        width: int = 10,
        height: int = 10,
        pixel_color: (int, int, int) = (255, 255, 255)
):
    x = x + height // 2
    for i in range(0, height, 9):
        draw_line(
            (x, y + i),
            (x + width, y + i),
            9, pixel_color
        )