from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def draw_star1():
    ##UP
    glColor3f(1, 1, 0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.1, 0.1)
    glVertex2f(0.1, 0.1)
    glVertex2f(0.0, 0.3)
    glEnd()

    ##left
    glColor3f(1, 1, 0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.1, 0.1)
    glVertex2f(-0.3, 0.1)
    glVertex2f(-0.1, -0.1)
    glEnd()

    ##Right
    glColor3f(1, 1, 0)
    glBegin(GL_TRIANGLES)
    glVertex2f(0.1, 0.1)
    glVertex2f(0.3, 0.1)
    glVertex2f(0.1, -0.1)
    glEnd()

    ##Center
    glColor3f(1, 1, 0)
    glBegin(GL_QUADS)
    glVertex2f(0.1, 0.1)
    glVertex2f(0.1, -0.1)
    glVertex2f(-0.1, -0.1)
    glVertex2f(-0.1, 0.1)
    glEnd()

    ##Right-down
    glColor3f(1, 1, 0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.05, -0.15)
    glVertex2f(0.2, -0.3)
    glVertex2f(0.11, -0.09)
    glEnd()

    ##Left-down
    glColor3f(1, 1, 0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.1, -0.05)
    glVertex2f(-0.2, -0.3)
    glVertex2f(0.1, -0.1)
    glEnd()

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

    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-0.33, 1)
    glVertex2f(-0.33, -1)
    glVertex2f(0.33, -1)
    glVertex2f(0.33, 1)
    glEnd()

    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(0.33, 1)
    glVertex2f(0.33, -1)
    glVertex2f(1, -1)
    glVertex2f(1, 1)
    glEnd()
    draw_star1()
    glFlush()



def main():
    glutInit()
    glutInitWindowPosition(500, 500)
    glutInitWindowSize(800, 600)
    glutCreateWindow("flag")
    glClear(GL_COLOR_BUFFER_BIT)
    glutDisplayFunc(draw_flag)
    glutMainLoop()


if __name__ == "__main__":
    main()
