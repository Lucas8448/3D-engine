from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Engine():
    def __init__(self, width = 640, height = 640, title = "Engine"):
        self.window = None
        self.width = width
        self.height = height
        self.title = title
        self.init()
    
    def init(self):
        glutInit()
        glutInitDisplayMode(GLUT_RGBA)
        glutInitWindowSize(self.width, self.height)
        glutInitWindowPosition(0, 0)
        self.window = glutCreateWindow(self.title)
        glutDisplayFunc(self.run)
        glutIdleFunc(self.run)
        glutMainLoop()
        
    def run(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glutSwapBuffers()
        
