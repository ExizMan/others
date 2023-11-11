from OpenGL.GL import *
from OpenGL.GLUT import *


def draw_hello_world():
    glClearColor(0, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT)

    glColor(1, 1, 1)
    glRasterPos2f(-0.6, 0.0)  # Устанавливаем позицию текста
    text = "Hello, World!"

    # Отображаем текст
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ord(char))

    glFlush()


if (1):
    glutInit()
    glutInitWindowSize(400, 200)
    glutCreateWindow("Hello World with PyOpenGL")
    glutDisplayFunc(draw_hello_world)
    glutMainLoop()