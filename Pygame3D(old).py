from msilib.schema import Class
import glfw
from OpenGL.GL import*
import numpy as np
import sys
import os
import time
from math import *
import matplotlib.pyplot as plt

####------Colours------####


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


####-------------------####
window = None
fig = plt.figure()
ax = plt.axes(projection='3d')
glfw.init()


class Game():
    def __init__(self, size=(640, 480), name="Pygame3D", clock=30, bg_colour=BLACK):
        self.display_center = (size[0] / 2, size[1] / 2)
        self.name = name
        self.display = size
        self.width = size[0]
        self.height = size[1]
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
        window = glfw.create_window(size[0], size[1], name, None, None)
        if not window:
            glfw.terminate()
            print("Pygame3D window can not be created")
            exit()

    def Environment(self):
        while not glfw.window_should_close(window):
            glfw.poll_events()
            glfw.swap_buffers(window)

        if not window:
            glfw.terminate()
            print("Pygame3D window can not be created")
            exit()


class Camera():
    def __init__(self, position=(0, 0, 0)):
        self.position = position
