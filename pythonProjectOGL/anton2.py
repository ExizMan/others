
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

angleX = 0
angleY = 0

def display():
    global angleX, angleY
    glClearColor(253, 244, 230, 250)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -5.0)

    glRotatef(angleX, 1.0, 0.0, 0.0)
    glRotatef(angleY, 0.0, 1.0, 0.0)
    glBegin(GL_QUADS) #  Левая передняя нога

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-0.9, -0.8, 0.9)
    glVertex3f(-0.8, -0.8, 0.9)
    glVertex3f(-0.8, -0.8, 1.0)
    glVertex3f(-0.9, -0.8, 1.0)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-0.9, 0.3, 0.9)
    glVertex3f(-0.8, 0.3, 0.9)
    glVertex3f(-0.8, 0.3, 1.0)
    glVertex3f(-0.9, 0.3, 1.0)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-0.9, -0.8, 0.9)
    glVertex3f(-0.8, -0.8, 0.9)
    glVertex3f(-0.8, 0.3, 0.9)
    glVertex3f(-0.9, 0.3, 0.9)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-0.9, -0.8, 0.9)
    glVertex3f(-0.8, -0.8, 0.9)
    glVertex3f(-0.8, 0.3, 0.9)
    glVertex3f(-0.9, 0.3, 0.9)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-0.9, -0.8, 1.0)
    glVertex3f(-0.8, -0.8, 1.0)
    glVertex3f(-0.8, 0.3, 1.0)
    glVertex3f(-0.9, 0.3, 1.0)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-0.8, -0.8, 1.0)
    glVertex3f(-0.8, -0.8, 0.9)
    glVertex3f(-0.8, 0.3, 0.9)
    glVertex3f(-0.8, 0.3, 1.0)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-0.9, -0.8, 1.0)
    glVertex3f(-0.9, -0.8, 0.9)
    glVertex3f(-0.9, 0.3, 0.9)
    glVertex3f(-0.9, 0.3, 1.0)

    glEnd()

    glBegin(GL_QUADS)  # Левая задняя нога

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-0.9, -0.8, -0.9)
    glVertex3f(-0.8, -0.8, -0.9)
    glVertex3f(-0.8, -0.8, -1.0)
    glVertex3f(-0.9, -0.8, -1.0)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-0.9, 0.3, -0.9)
    glVertex3f(-0.8, 0.3, -0.9)
    glVertex3f(-0.8, 0.3, -1.0)
    glVertex3f(-0.9, 0.3, -1.0)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-0.9, -0.8, -0.9)
    glVertex3f(-0.8, -0.8, -0.9)
    glVertex3f(-0.8, 0.3, -0.9)
    glVertex3f(-0.9, 0.3, -0.9)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-0.9, -0.8, -0.9)
    glVertex3f(-0.8, -0.8, -0.9)
    glVertex3f(-0.8, 0.3, -0.9)
    glVertex3f(-0.9, 0.3, -0.9)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-0.9, -0.8, -1.0)
    glVertex3f(-0.8, -0.8, -1.0)
    glVertex3f(-0.8, 0.3, -1.0)
    glVertex3f(-0.9, 0.3, -1.0)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-0.8, -0.8, -1.0)
    glVertex3f(-0.8, -0.8, -0.9)
    glVertex3f(-0.8, 0.3, -0.9)
    glVertex3f(-0.8, 0.3, -1.0)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-0.9, -0.8, -1.0)
    glVertex3f(-0.9, -0.8, -0.9)
    glVertex3f(-0.9, 0.3, -0.9)
    glVertex3f(-0.9, 0.3, -1.0)

    glEnd()

    glBegin(GL_QUADS)  # Правая задняя нога

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.9, -0.8, -0.9)
    glVertex3f(0.8, -0.8, -0.9)
    glVertex3f(0.8, -0.8, -1.0)
    glVertex3f(0.9, -0.8, -1.0)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.9, 0.3, -0.9)
    glVertex3f(0.8, 0.3, -0.9)
    glVertex3f(0.8, 0.3, -1.0)
    glVertex3f(0.9, 0.3, -1.0)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.9, -0.8, -0.9)
    glVertex3f(0.8, -0.8, -0.9)
    glVertex3f(0.8, 0.3, -0.9)
    glVertex3f(0.9, 0.3, -0.9)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.9, -0.8, -0.9)
    glVertex3f(0.8, -0.8, -0.9)
    glVertex3f(0.8, 0.3, -0.9)
    glVertex3f(0.9, 0.3, -0.9)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.9, -0.8, -1.0)
    glVertex3f(0.8, -0.8, -1.0)
    glVertex3f(0.8, 0.3, -1.0)
    glVertex3f(0.9, 0.3, -1.0)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.8, -0.8, -1.0)
    glVertex3f(0.8, -0.8, -0.9)
    glVertex3f(0.8, 0.3, -0.9)
    glVertex3f(0.8, 0.3, -1.0)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.9, -0.8, -1.0)
    glVertex3f(0.9, -0.8, -0.9)
    glVertex3f(0.9, 0.3, -0.9)
    glVertex3f(0.9, 0.3, -1.0)

    glEnd()

    glBegin(GL_QUADS)  # Правая передняя нога

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.9, -0.8, 0.9)
    glVertex3f(0.8, -0.8, 0.9)
    glVertex3f(0.8, -0.8, 1.0)
    glVertex3f(0.9, -0.8, 1.0)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.9, 0.3, 0.9)
    glVertex3f(0.8, 0.3, 0.9)
    glVertex3f(0.8, 0.3, 1.0)
    glVertex3f(0.9, 0.3, 1.0)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.9, -0.8, 0.9)
    glVertex3f(0.8, -0.8, 0.9)
    glVertex3f(0.8, 0.3, 0.9)
    glVertex3f(0.9, 0.3, 0.9)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.9, -0.8, 0.9)
    glVertex3f(0.8, -0.8, 0.9)
    glVertex3f(0.8, 0.3, 0.9)
    glVertex3f(0.9, 0.3, 0.9)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.9, -0.8, 1.0)
    glVertex3f(0.8, -0.8, 1.0)
    glVertex3f(0.8, 0.3, 1.0)
    glVertex3f(0.9, 0.3, 1.0)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.8, -0.8, 1.0)
    glVertex3f(0.8, -0.8, 0.9)
    glVertex3f(0.8, 0.3, 0.9)
    glVertex3f(0.8, 0.3, 1.0)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.9, -0.8, 1.0)
    glVertex3f(0.9, -0.8, 0.9)
    glVertex3f(0.9, 0.3, 0.9)
    glVertex3f(0.9, 0.3, 1.0)

    glEnd()

    glBegin(GL_QUADS)  # Поверхность стола

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-0.9, 0.3, -1.0)
    glVertex3f(0.9, 0.3, -1.0)
    glVertex3f(0.9, 0.3, 1.0)
    glVertex3f(-0.9, 0.3, 1.0)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-0.9, 0.33, -1.0)
    glVertex3f(0.9, 0.33, -1.0)
    glVertex3f(0.9, 0.33, 1.0)
    glVertex3f(-0.9, 0.33, 1.0)

    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(-0.9, 0.3, -1.0)
    glVertex3f(0.9, 0.3, -1.0)
    glVertex3f(0.9, 0.33, -1.0)
    glVertex3f(-0.9, 0.33, -1.0)

    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(-0.9, 0.3, 1.0)
    glVertex3f(0.9, 0.3, 1.0)
    glVertex3f(0.9, 0.33, 1.0)
    glVertex3f(-0.9, 0.33, 1.0)

    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(-0.9, 0.3, -1.0)
    glVertex3f(-0.9, 0.33, -1.0)
    glVertex3f(-0.9, 0.33, 1.0)
    glVertex3f(-0.9, 0.3, 1.0)

    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(0.9, 0.3, -1.0)
    glVertex3f(0.9, 0.33, -1.0)
    glVertex3f(0.9, 0.33, 1.0)
    glVertex3f(0.9, 0.3, 1.0)


    glEnd()
    glutSwapBuffers()


def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, w / h, 1.0, 100.0)
    glMatrixMode(GL_MODELVIEW)

def idle():
    global angleX, angleY
    angleX += 0.1
    angleY += 0.1
    glutPostRedisplay()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow("3D Cube")
    glEnable(GL_DEPTH_TEST)
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutIdleFunc(idle)
    glutMainLoop()

main()