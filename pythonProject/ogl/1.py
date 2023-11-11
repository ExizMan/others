from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from turtle import *

def draw_flag():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(0.0, 0.5, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-1, 1)
    glVertex2f(-1, -1)
    glVertex2f(-0.33, -1)
    glVertex2f(-0.33, 1)
    glEnd()

    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-0.33, 1)
    glVertex2f(-0.33, -1)
    glVertex2f(0.33, -1)
    glVertex2f(0.33, 1)
    glEnd()

    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(0.33, 1)
    glVertex2f(0.33, -1)
    glVertex2f(1, -1)
    glVertex2f(1, 1)
    glEnd()
    draw_star()
    glFlush()

def draw_star():
    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 0.5, 0.0)
    glVertex2f(0.0, 0.4)
    glVertex2f(-0.1, 0.1)
    glVertex2f(0.1, 0.1)

    glVertex2f(-0.1, 0.1)
    glVertex2f(0.1, 0.1)
    glVertex2f(0.0, -0.2)

    glVertex2f(0.0, -0.2)
    glVertex2f(0.1, 0.1)
    glVertex2f(0.2, -0.1)

    glVertex2f(0.2, -0.1)
    glVertex2f(0.1, 0.1)
    glVertex2f(0.4, 0.0)

    glVertex2f(0.4, 0.0)
    glVertex2f(0.1, 0.1)
    glVertex2f(0.2, 0.2)

    glVertex2f(0.2, 0.2)
    glVertex2f(0.1, 0.1)
    glVertex2f(0.0, 0.4)
    glEnd()


def main():
    glutInit()
    glutInitWindowPosition(500, 500)
    glutInitWindowSize(800, 600)
    glutCreateWindow("flag")
    glClear(GL_COLOR_BUFFER_BIT)
    glutDisplayFunc(draw_flag)
    glutMainLoop()


main()