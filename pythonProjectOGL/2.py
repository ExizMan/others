from OpenGL.GL import *

from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

def draw_circle(radius, num_segments,x0,y0):
    # Вычисляем угол между сегментами
    theta = 2 * np.pi / num_segments

    # Начинаем рисовать сегменты фана
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x0, y0)  # Центр окружности

    # Рисуем вершины сегментов
    for i in range(num_segments + 1):
        x = radius * np.cos(theta * i)
        y = radius * np.sin(theta * i)
        glVertex2f(x, y)

    glEnd()
def draw_tank():

    glLoadIdentity()
    glRotate(30,0,1,0)
    glRotate(-45,1,0,0)

    glBegin(GL_QUADS)
    glColor3f(0.3, 0.3, 0.3)
    glVertex2f(0.1, -0.05)
    glColor3f(0.5, 0.5, 0.5)
    glVertex2f(0.1, 0.05)
    glColor3f(0.4, 0.4, 0.4)
    glVertex2f(-0.1, 0.05)
    glColor3f(0.2, 0.2, 0.2)
    glVertex2f(-0.1, -0.05)
    glEnd()
    glPushMatrix()
    glLoadIdentity()
    glTranslatef(0.087,0,0)
    glRotate(30,0,1,0)
    glRotate(-45,1,0,0)

    glBegin(GL_QUADS)
    glColor3f(0.3, 0.3, 0.3)
    glVertex2f(0, -0.05)
    glVertex2f(0, 0.05)
    glVertex2f(0.4, 0.05)
    glVertex2f(0.4, -0.05)
    glEnd()
    glPushMatrix()
    glLoadIdentity()
    glTranslatef(0.1, 0.05, 0)
    glBegin(GL_LINE_LOOP)
    glColor3f(0,0,0)
    glVertex2f(0, -0.1)
    glVertex2f(0, -0.05)
    glVertex2f(0.35, -0.05)
    glVertex2f(0.35, -0.1)
    glEnd()
    glTranslatef(0,-0.08,0)
    draw_circle(0.030,32,0,0)
    glTranslatef(0.06,0,0)
    draw_circle(0.030, 32, 0, 0)
    glTranslatef(0.06, 0, 0)
    draw_circle(0.030, 32, 0, 0)
    glTranslatef(0.06, 0, 0)
    draw_circle(0.030, 32, 0, 0)
    glTranslatef(0.06, 0, 0)
    draw_circle(0.030, 32, 0, 0)
    glTranslatef(0.06, 0, 0)
    draw_circle(0.030, 32, 0, 0)
    glTranslatef(0.06, 0, 0)
    draw_circle(0.030, 32, 0, 0)


    glPopMatrix()
    glTranslatef(0.2, 0.1, 0)
    glBegin(GL_QUADS)
    glColor3f(0.3, 0.3, 0.3)
    glVertex2f(0.1, -0.05)
    glColor3f(0.5, 0.5, 0.5)
    glVertex2f(0.1, 0.05)
    glColor3f(0.4, 0.4, 0.4)
    glVertex2f(-0.1, 0.05)
    glColor3f(0.2, 0.2, 0.2)
    glVertex2f(-0.1, -0.05)
    glEnd()



    glRotate(90,1,0,0)
    glTranslatef(-0.05,0,0)
    glBegin(GL_QUADS)
    glColor3f(0.3, 0.3, 0.3)
    glVertex2f(0.1, -0.05)
    glColor3f(0.5, 0.5, 0.5)
    glVertex2f(0.1, 0.05)
    glColor3f(0.4, 0.4, 0.4)
    glVertex2f(-0.1, 0.05)
    glColor3f(0.2, 0.2, 0.2)
    glVertex2f(-0.1, -0.05)
    glEnd()
    glLoadIdentity()
    glTranslatef(0.1,0.1,0)
    glBegin(GL_POLYGON)
    glColor3f(0, 0, 0)
    glVertex2f(0.1, -0.05)
    glVertex2f(0.1, 0.05)
    glVertex2f(-0.1, 0.05)
    glVertex2f(-0.1, -0.05)
    glEnd()






def draw_scene():
    glClearColor(0.5, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)




    draw_tank()

    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Isometric Tank")

      # Черный фон



    glutDisplayFunc(draw_scene)
    glutMainLoop()



main()