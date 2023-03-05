import math
import numpy as np
import pygame


def convert(ax, ay, az, camera_position, camera_rotation):
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


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    camera_position = (0, 5, -5)
    camera_rotation = (0, 0, 0)
    # vertices and edges to create a cube
    vertices = ((-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),
                (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1))
    edges = ((0, 3), (1, 0), (2, 1), (3, 2),
             (4, 5), (5, 6), (6, 7), (7, 4),
             (0, 4), (1, 5), (2, 6), (3, 7))
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill((0, 0, 0))
        for edge in edges:
            v1 = vertices[edge[0]]
            v2 = vertices[edge[1]]
            x1, y1 = convert(v1[0], v1[1], v1[2],
                             camera_position, camera_rotation)
            x2, y2 = convert(v2[0], v2[1], v2[2],
                             camera_position, camera_rotation)
            pygame.draw.line(screen, (255, 255, 255),
                             (x1*100+400, y1*100+300), (x2*100+400, y2*100+300))
        # camera movement with keys and rotation with mouse
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            camera_position = (camera_position[0], camera_position[1],
                               camera_position[2]+0.1)
        if keys[pygame.K_s]:
            camera_position = (camera_position[0], camera_position[1],
                               camera_position[2]-0.1)
        if keys[pygame.K_a]:
            camera_position = (camera_position[0]-0.1, camera_position[1],
                               camera_position[2])
        if keys[pygame.K_d]:
            camera_position = (camera_position[0]+0.1, camera_position[1],
                               camera_position[2])
        if keys[pygame.K_SPACE]:
            camera_position = (camera_position[0], camera_position[1]+0.1,
                               camera_position[2])
        if keys[pygame.K_LSHIFT]:
            camera_position = (camera_position[0], camera_position[1]-0.1,
                               camera_position[2])
        if pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_rel()
            camera_rotation = (camera_rotation[0]+y/1000,
                               camera_rotation[1]+x/1000, camera_rotation[2])
        # display coordinates and rotation in top left corner
        text = "x: " + str(round((camera_position[0]))) + " y: " + str(
            round(camera_position[1])) + " z: " + str(round(camera_position[2]))
        text += " ox: " + str(round(camera_rotation[0])) + " oy: " + str(
            round(camera_rotation[1])) + " oz: " + str(round(camera_rotation[2]))
        font = pygame.font.SysFont("Arial", 20)
        label = font.render(text, 1, (255, 255, 255))
        screen.blit(label, (10, 10))
        # rotate
        pygame.display.flip()


if __name__ == '__main__':
    main()
