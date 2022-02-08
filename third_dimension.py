import math
import numpy as np


def convert(ax, ay, az, camera_position, camera_rotation):
    # ex, ey, ez are distance from camera. ax, ay, az are object coordinates
    ex, ey, ez = (camera_position[0] - ax,
                  camera_position[1] - ay, camera_position[2] - az)

    ox, oy, oz = camera_rotation
    cx, cy, cz = camera_position
    matrix_1 = np.array(
        [[1, 0, 0], [0, -math.cos(ox), math.sin(ox)], [0, -math.sin(ox), math.cos(ox)]])
    matrix_2 = np.array([[math.cos(oy), 0, -math.sin(oy)],
                        [0, 1, 0], [math.sin(oy), 0, math.cos(oy)]])
    matrix_3 = np.array([[math.cos(oz), math.sin(oz), 0],
                        [-math.sin(oz), math.cos(oz), 0], [0, 0, 1]])
    matrix_4 = np.array([ax - cx, ay - cy, az - cz])
    d = matrix_4.dot(matrix_3.dot(matrix_2.dot(matrix_1)))

    x = (ez/d[2])*d[0]+ex
    y = (ez/d[2])*d[1]+ey
    return x, y
    


print(convert(0, 15, 16, camera_position=(20, 20, 20), camera_rotation=(0, 10, 0)))
