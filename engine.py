import math
import numpy as np
import pygame
import pygame.gfxdraw


class Camera:
    def __init__(self):
        self.rotation = (0, 0, 0)
        self.position = (0, 0, 0)

    def rotate(self, x, y, z):
        self.rotation = (x, y, z)

    def move(self, x, y, z):
        self.position = (x, y, z)

    def get_rotation(self):
        return self.rotation

    def get_position(self):
        return self.position


class PY3D():
    def __init__(self, size=(800, 600)):
        self.camera = Camera()
        self.objects = []
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()

    def convert(self, ax, ay, az):
        camera_position = self.camera.get_position()
        camera_rotation = self.camera.get_rotation()
        ex, ey, ez = (camera_position[0] - ax,
                      camera_position[1] - ay, camera_position[2] - az)
        ox, oy, oz = camera_rotation
        cx, cy, cz = camera_position
        m_1 = np.array([[1, 0, 0], [0, -math.cos(ox), math.sin(ox)],
                       [0, -math.sin(ox), math.cos(ox)]])
        m_2 = np.array([[math.cos(oy), 0, -math.sin(oy)],
                       [0, 1, 0], [math.sin(oy), 0, math.cos(oy)]])
        m_3 = np.array([[math.cos(oz), math.sin(oz), 0],
                       [-math.sin(oz), math.cos(oz), 0], [0, 0, 1]])
        m_4 = np.array([ax - cx, ay - cy, az - cz])
        d = m_4.dot(m_3.dot(m_2.dot(m_1)))
        x = (ez/d[2])*d[0]+ex
        y = (ez/d[2])*d[1]+ey
        return x, y

    def add_object(self, obj):
        self.objects.append(obj)

    def get_objects(self):
        return self.objects

    def set_objects(self, objects):
        self.objects = objects

    def draw(self):
        for obj in self.objects:
            for edge in obj.get_edges():
                v1, v2 = edge
                v1x, v1y, v1z = obj.get_vertices()[v1]
                v2x, v2y, v2z = obj.get_vertices()[v2]
                x1, y1 = self.convert(
                    v1x, v1y, v1z, self.camera.get_position(), self.camera.get_rotation())
                x2, y2 = self.convert(
                    v2x, v2y, v2z, self.camera.get_position(), self.camera.get_rotation())
                pygame.draw.line(
                    self.screen, obj.get_edge_color(), (x1, y1), (x2, y2))
        for obj in self.objects:
            obj.update()


class Object(PY3D):
    def __init__(self):
        self.vertices = []
        self.edges = []
        self.sides = []
        self.edge_color = (255, 255, 255)
        self.color = (0, 0, 255)

    # vertices add, get and set
    def add_vertex(self, x, y, z):
        self.vertices.append((x, y, z))

    def get_vertices(self):
        return self.vertices

    def set_vertices(self, vertices):
        self.vertices = vertices

    # edges add, get and set
    def add_edge(self, v1, v2):
        self.edges.append((v1, v2))

    def get_edges(self):
        return self.edges

    def set_edges(self, edges):
        self.edges = edges

    # sides add, get and set
    def add_side(self, *vertices):
        self.sides.append(vertices)

    def get_sides(self):
        return self.sides

    def set_sides(self, sides):
        self.sides = sides

    # edge color get and set
    def get_edge_color(self):
        return self.edge_color

    def set_edge_color(self, color):
        self.edge_color = color

    # color get and set
    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def append(self, obj):
        PY3D.add_object(self, obj)


class Cube(Object):
    def __init__(self, x, y, z, x_len, y_len, z_len):
        Object.__init__(self)
        self.x = x
        self.y = y
        self.z = z
        self.x_len = x_len
        self.y_len = y_len
        self.z_len = z_len
        self.vertices = [(x, y, z), (x + x_len, y, z), (x + x_len, y + y_len, z), (x, y + y_len, z), (x, y,
                                                                                                      z + z_len), (x + x_len, y, z + z_len), (x + x_len, y + y_len, z + z_len), (x, y + y_len, z + z_len)]
        self.edges = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5),
                      (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7)]
        self.sides = [(0, 1, 2, 3), (4, 5, 6, 7), (0, 1, 5, 4),
                      (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7)]
        Object.append(self)

    def update(self):
        Object.append(self)
