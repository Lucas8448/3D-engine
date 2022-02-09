import third_dimension as td
import pyglet

pyglet.graphics.glEnable(pyglet.graphics.GL_DEPTH_TEST)
    
class colours():
    BLACK = (0,   0,   0)
    BLUE = (0,   0, 255)
    BROWN = (139,  69,  19)
    CYAN = (0, 255, 255)
    DARKBLUE = (0,   0,  64)
    DARKBROWN = (36,  18,   5)
    DARKGREEN = (0,  64,   0)
    DARKGREY = (64,  64,  64)
    DARKRED = (64,   0,   0)
    GREY = (128, 128, 128)
    GREEN = (0, 128,   0)
    LIME = (0, 255,   0)
    MAGENTA = (255,   0, 255)
    MAROON = (128,   0,   0)
    NAVYBLUE = (0,   0, 128)
    OLIVE = (128, 128,   0)
    PURPLE = (128,   0, 128)
    RED = (255,   0,   0)
    SILVER = (192, 192, 192)
    TEAL = (0, 128, 128)
    WHITE = (255, 255, 255)
    YELLOW = (255, 255,   0)

class Window():
    def __init__(self, size = (640, 480), title = "Pygame3D Window"):
        self.title = title
        self.size = size
        self.width = size[0]
        self.height = size[1]
        self.window = pyglet.window.Window(self.width, self.height, caption = title, vsync=True)
        self.batch = pyglet.graphics.Batch()

    def run(self):
        pyglet.app.run()
    
    @self.window.event
    def draw(self):
        self.window.clear()
        self.batch.draw()

    def clear(self):
        self.window.clear()

    def size(self):
        return self.size

    

class Camera(Window):
    def __init__(self, position=(0, 0, 0), rotation=(0, 0, 0)):
        self.position = position
        self.rotation = rotation
        self.x = position[0]
        self.y = position[1]
        self.z = position[2]
        self.roll = rotation[0]
        self.pitch = rotation[1]
        self.yaw = rotation[2]

    def setPosition(self, position):
        self.position = position
        self.x = position[0]
        self.y = position[1]
        self.z = position[2]

    def changePosition(self, change=(0, 0, 0)):
        self.x = + change[0]
        self.y = + change[1]
        self.z = change[2]
        self.position = (self.x, self.y, self.z)

    def setRotation(self, rotation):
        self.rotation = rotation
        self.roll = rotation[0]
        self.pitch = rotation[1]
        self.yaw = rotation[2]

    def changeRotation(self, change=(0, 0, 0)):
        self.roll = change[0]
        self.pitch = change[1]
        self.yaw = change[2]
        self.rotation = (self.roll, self.pitch, self.yaw)

    def where(self):
        return self.rotation, self.position



#class Line(Window):
#    def init(self, ax, ay, az, bx, by, bz, width):
#        self.width = width
#        self.ax = ax
#        self.ay = ay
#        self.az = az
#        self.bx = bx
#        self.by = by
#        self.bz = bz
#        self.x1, self.y1 = td.convert(ax, ay, az, camera_position=(
#            camera.position), camera_rotation=(camera.rotation))
#        self.x2, self.y2 = td.convert(bx, by, bz, camera_position=(
#            camera.position), camera_rotation=(camera.rotation))
#        self.line = shapes.line(self.x1, self.y1, self.x2, self.y2, self.width, batch=batch)
#
#    def changePosition(self, ax, ay, az, bx, by, bz):
#        self.ax =+ ax
#        self.ay =+ ay
#        self.az =+ az
#        self.bx =+ bx
#        self.by =+ by
#        self.bz =+ bz
#        self.x1, self.y1 = td.convert(ax, ay, az, camera_position=(
#            camera.position), camera_rotation=(camera.rotation))
#        self.x2, self.y2 = td.convert(bx, by, bz, camera_position=(
#            camera.position), camera_rotation=(camera.rotation))
#        
#        self.line = shapes.line(self.x1, self.y1, self.x2, self.y2, self.width, batch=batch)
#
#    def setPosition(self, ax, ay, az, bx, by, bz):
#        self.ax = ax
#        self.ay = ay
#        self.az = az
#        self.bx = bx
#        self.by = by
#        self.bz = bz
#        self.x1, self.y1 = td.convert(ax, ay, az, camera_position=(
#            camera.position), camera_rotation=(camera.rotation))
#        self.x2, self.y2 = td.convert(bx, by, bz, camera_position=(
#            camera.position), camera_rotation=(camera.rotation))
#        self.line = shapes.line(self.x1, self.y1, self.x2, self.y2, self.width, batch=batch)