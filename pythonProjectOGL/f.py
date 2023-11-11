import sys

from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

quadric = None

# Camera Position
angle = 0.0  # Camera angle
x = 0.0

z = 0.0  # Camera position
dX = 0.0

dZ = 0.0  # Camera direction

# mouse
xrot = 0.0
yrot = 0.0

xdiff = 0.0
ydiff = 0.0

mouseDown = False


################### CAMERA CONTROL #####################
class Camera:

    def __init__(self):
        self.position = (0, 0, 0)
        self.rotation = (0, 0, 0)

    def translate(self, dx, dy, dz):
        x, y, z = self.position
        self.position = (x + dx, y + dy, z + dz)

    def rotate(self, dx, dy, dz):
        x, y, z = self.rotation
        self.rotation = (x + dx, y + dy, z + dz)

    def apply(self):
        glTranslate(*self.position)
        glRotated(self.rotation[0], -1, 0, 0)
        glRotated(self.rotation[1], 0, -1, 0)
        glRotated(self.rotation[2], 0, 0, -1)


camera = Camera()


def idle():
    global mouseDown, xrot, yrot
    if (not mouseDown):

        if (xrot > 1):
            xrot -= 0.005 * xrot
        elif (xrot < -1):
            xrot += 0.005 * -xrot
        else:
            xrot = 0

        if (yrot > 1):
            yrot -= 0.005 * yrot
        elif (yrot < -1):
            yrot += 0.005 * -yrot
        else:
            yrot = 0


def mouse(button, state, x, y):
    global xdiff, ydiff, mouseDown
    # print(str(button) + " " + str(GLUT_LEFT_BUTTON))
    # print(str(state) + " " + str(GLUT_DOWN))
    if (button == GLUT_LEFT_BUTTON and state == GLUT_DOWN):
        mouseDown = True

        xdiff = x + yrot
        ydiff = -y - xrot
        print(str(xdiff) + " " + str(ydiff))
    else:
        mouseDown = False


def mouseMotion(x, y):
    global yrot, xrot, mouseDown
    if (mouseDown):
        yrot = - x + xdiff
        xrot = - y - ydiff
    # print(mouseDown)


def processSpecialKeys(key, xx, yy):
    global x, z, dX, dZ, angle
    fraction = 0.1
    movespeed = 1

    if (key == GLUT_KEY_LEFT):
        camera.translate(movespeed, 0, 0)
    # angle -= 0.01
    # dX = sin(angle)
    # dY = -cos(angle)
    elif (key == GLUT_KEY_RIGHT):
        camera.translate(-movespeed, 0, 0)
    # angle -= 0.01
    # dX = sin(angle)
    # dY = -cos(angle)
    elif (key == GLUT_KEY_UP):
        camera.translate(0, -movespeed, 0)
    # x += dX * fraction
    # z += dZ * fraction
    elif (key == GLUT_KEY_DOWN):
        camera.translate(0, movespeed, 0)
    # x -= dX * fraction
    # z -= dZ * fraction
    elif (key == GLUT_KEY_PAGE_UP):
        camera.translate(0, 0, movespeed)
    elif (key == GLUT_KEY_PAGE_DOWN):
        camera.translate(0, 0, -movespeed)


def processNormalKeys(key, x, y):
    if (key == 27):
        exit(0)


################### OBJECTS #####################
# Snowman
def drawSnowMan():
    glColor3f(1.0, 1.0, 1.0)

    # Draw Body
    glTranslatef(0.0, 0.75, 0.0)
    glutSolidSphere(0.75, 20, 20)

    # Draw Head
    glTranslatef(0.0, 1.0, 0.0)
    glutSolidSphere(0.25, 20, 20)

    # Draw Eyes
    glPushMatrix()
    glColor3f(0.0, 0.0, 0.0)
    glTranslatef(0.05, 0.10, 0.18)
    glutSolidSphere(0.05, 10, 10)
    glTranslatef(-0.1, 0.0, 0.0)
    glutSolidSphere(0.05, 10, 10)
    glPopMatrix()

    # Draw Nose
    glColor3f(1.0, 0.6, 0.6)
    glutSolidCone(0.08, 0.6, 10, 2)


def drawCylinder(height, radius):
    glBegin(GL_QUAD_STRIP)
    for i in range(0, 360, 1):
        glColor3f(1.0, 0.6, 0.0)
        glVertex3f(radius * cos(i), height / 2.0, radius * sin(i))
        glVertex3f(radius * cos(i), -height / 2.0, radius * sin(i))
    glEnd()

    # top and bottom circles
    # reuse the currentTexture on top and bottom)
    i = -height / 2.0
    jump = height

    while (i <= height / 2.0):
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(1.0, 0.6, 0.0)
        glVertex3f(0, i, 0)
        for k in range(0, 360, 1):
            glVertex3f(radius * cos(k), i, radius * sin(k))
        glEnd()
        i += jump


def renderScene():
    global x, z, dX, dZ, angle, camera
    # Clear Color and Depth Buffers
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Reset transformations
    glLoadIdentity()
    # Set the camera
    # gluLookAt	(	x, 1.0, z,
    #			x+dX, 1.0,  z+dZ,
    #			0.0, 1.0,  0.0
    #			)

    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)

    # glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)

    glShadeModel(GL_SMOOTH)

    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
    glEnable(GL_TEXTURE_2D)

    specReflection = [1.0, 1.0, 1.0, 1.0]
    glMaterialfv(GL_FRONT, GL_SPECULAR, specReflection)
    glMateriali(GL_FRONT, GL_SHININESS, 30)
    # glLightfv(GL_LIGHT0, GL_SPECULAR, specReflection)
    glLightfv(GL_LIGHT0, GL_POSITION, [2.0, 2.0, 2.0, 1.0])
    camera.apply()

    # Draw ground

    # Draw 36 Snowmen
    # for i in range (-3,3):
    # 	for j in range(-3,3):
    # 		glPushMatrix()
    # 		glTranslatef(i*10.0,0,j * 10.0)
    # 		drawSnowMan()
    # 		glPopMatrix()

    camera.rotate(xrot * 0.001, 0.0, 0.0)
    camera.rotate(0, yrot * 0.001, 0.0)

    # drawSnowMan()
    # drawCylinder(0.6,0.25)
    drawCar()

    idle()
    glFlush()
    glutSwapBuffers()


def changeSize(w, h):
    # Prevent a divide by zero, when window is too short
    # (you cant make a window of zero width).
    if (h == 0):
        h = 1
    ratio = w * 1.0 / h

    # Use the Projection Matrix
    glMatrixMode(GL_PROJECTION)

    # Reset Matrix
    glLoadIdentity()

    # Set the viewport to be the entire window
    glViewport(0, 0, w, h)

    # Set the correct perspective.
    gluPerspective(45.0, ratio, 0.1, 100.0)

    # Get Back to the Modelview
    glMatrixMode(GL_MODELVIEW)


def main():
    # init GLUT and create window
    glutInit()
    glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowPosition(800, 600)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b'IF3260: Computer Graphics')

    glMatrixMode(GL_PROJECTION)
    gluPerspective(60, 1, 1.0, 1000.0)
    glMatrixMode(GL_MODELVIEW)

    # register callbacks
    glutDisplayFunc(renderScene)
    glutReshapeFunc(changeSize)
    glutIdleFunc(renderScene)
    # glutKeyboardFunc(processNormalKeys)
    glutSpecialFunc(processSpecialKeys)
    glutMouseFunc(mouse)
    glutMotionFunc(mouseMotion)

    # OpenGL init
    glEnable(GL_DEPTH_TEST)

    # enter GLUT event processing cycle
    glutMainLoop()


def drawCar():
    z = 1.5

    # back window frame
    glColor3f(206 / 255, 20 / 255, 55 / 255)
    glBegin(GL_QUADS)
    glVertex3f(-3.0, 0.25, -z)
    glVertex3f(-3.0, 0.25, z)
    glVertex3f(-3.0, -1.0, z)
    glVertex3f(-3.0, -1.0, -z)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3f(-3.0, 1.5, -z)
    glVertex3f(-3.0, 1.5, z)
    glVertex3f(-3.0, 1.0, z)
    glVertex3f(-3.0, 1.0, -z)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3f(-3.0, 0.25, -z)
    glVertex3f(-3.0, 0.25, -z + 0.5)
    glVertex3f(-3.0, 1.0, -z + 0.5)
    glVertex3f(-3.0, 1.0, -z)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3f(-3.0, 0.25, z - 0.5)
    glVertex3f(-3.0, 0.25, z)
    glVertex3f(-3.0, 1.0, z)
    glVertex3f(-3.0, 1.0, z - 0.5)
    glEnd()

    # top
    glColor3f(240 / 255, 20 / 255, 55 / 255)
    glBegin(GL_QUADS)
    glVertex3f(-3.0, 1.5, -z)
    glVertex3f(-3.0, 1.5, z)
    glVertex3f(0.6, 1.5, z)
    glVertex3f(0.6, 1.5, -z)
    glEnd()

    # bottom
    glColor3f(190 / 255, 20 / 255, 55 / 255)
    glBegin(GL_QUADS)
    glVertex3f(-3.0, -1.0, -z)
    glVertex3f(-3.0, -1.0, z)
    glVertex3f(3.0, -1.0, z)
    glVertex3f(3.0, -1.0, -z)
    glEnd()

    # front
    glColor3f(206 / 255, 20 / 255, 55 / 255)
    glBegin(GL_QUADS)
    glVertex3f(3.0, -1.0, -z)
    glVertex3f(3.0, 0.15, -z)
    glVertex3f(3.0, 0.15, z)
    glVertex3f(3.0, -1.0, z)

    # lampu
    glColor3f(0.9, 0.9, 0.9)
    glVertex3f(3.006, -0.65, -z + 0.101)
    glVertex3f(3.006, -0.35, -z + 0.101)
    glVertex3f(3.006, -0.35, -z + 0.601)
    glVertex3f(3.006, -0.65, -z + 0.601)

    glVertex3f(3.006, -0.65, z - 0.101)
    glVertex3f(3.006, -0.35, z - 0.101)
    glVertex3f(3.006, -0.35, z - 0.601)
    glVertex3f(3.006, -0.65, z - 0.601)

    glColor3f(0, 0, 0)
    glVertex3f(3.006, -0.6, -z + 1)
    glVertex3f(3.006, -0.37, -z + 1)
    glVertex3f(3.006, -0.37, z - 1)
    glVertex3f(3.006, -0.6, z - 1)
    # lampu2
    glColor3f(0.6, 0.6, 0.6)
    glVertex3f(3.005, -0.7, -z)
    glVertex3f(3.005, -0.3, -z)
    glVertex3f(3.005, -0.3, z)
    glVertex3f(3.005, -0.7, z)

    glVertex3f(2.9, -0.3, -z - 0.0014)
    glVertex3f(3.0, -0.3, -z - 0.0014)
    glVertex3f(3.0, -0.7, -z - 0.0014)
    glVertex3f(2.9, -0.7, -z - 0.0014)

    glVertex3f(2.9, -0.3, z + 0.0014)
    glVertex3f(3.0, -0.3, z + 0.0014)
    glVertex3f(3.0, -0.7, z + 0.0014)
    glVertex3f(2.9, -0.7, z + 0.0014)

    glColor3f(226 / 255, 152 / 255, 22 / 255)
    glVertex3f(2.95, -0.35, z + 0.0015)
    glVertex3f(2.985, -0.35, z + 0.0015)
    glVertex3f(2.985, -0.65, z + 0.0015)
    glVertex3f(2.95, -0.65, z + 0.0015)

    glVertex3f(2.95, -0.35, -z - 0.0015)
    glVertex3f(2.985, -0.35, -z - 0.0015)
    glVertex3f(2.985, -0.65, -z - 0.0015)
    glVertex3f(2.95, -0.65, -z - 0.0015)
    glEnd()

    # front cover
    glColor3f(230 / 255, 20 / 255, 55 / 255)
    glBegin(GL_QUADS)
    glVertex3f(3.0, 0.15, -z)
    glVertex3f(1.2, 0.25, -z)
    glVertex3f(1.2, 0.25, z)
    glVertex3f(3.0, 0.15, z)
    glEnd()

    # front window frame
    glColor3f(235 / 255, 20 / 255, 55 / 255)
    glBegin(GL_QUADS)
    glVertex3f(0.6, 1.5, -z)
    glVertex3f(0.6, 1.5, z)
    glVertex3f(0.65, 1.42, z)
    glVertex3f(0.65, 1.42, -z)

    glVertex3f(1.15, 0.34, -z)
    glVertex3f(1.15, 0.34, -z + 0.1)
    glVertex3f(0.65, 1.42, -z + 0.1)
    glVertex3f(0.65, 1.42, -z)

    glVertex3f(1.15, 0.34, z)
    glVertex3f(1.15, 0.34, z - 0.1)
    glVertex3f(0.65, 1.42, z - 0.1)
    glVertex3f(0.65, 1.42, z)

    glVertex3f(1.15, 0.34, -z)
    glVertex3f(1.15, 0.34, z)
    glVertex3f(1.2, 0.25, z)
    glVertex3f(1.2, 0.25, -z)
    glEnd()

    # left above (window frame part)
    glColor3f(206 / 255, 20 / 255, 55 / 255)
    glBegin(GL_QUADS)
    glVertex3f(-3.0, 1.5, -z)
    glVertex3f(0.6, 1.5, -z)
    glVertex3f(0.696, 1.3, -z)
    glVertex3f(-3.0, 1.3, -z)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3f(-3.0, 1.3, -z)
    glVertex3f(-3.0, 0.25, -z)
    glVertex3f(-2.5, 0.25, -z)
    glVertex3f(-2.5, 1.3, -z)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3f(-1.2, 1.3, -z)
    glVertex3f(-1.2, 0.25, -z)
    glVertex3f(-1.0, 0.25, -z)
    glVertex3f(-1.0, 1.3, -z)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3f(1.2, 0.25, -z)
    glVertex3f(0.696, 1.3, -z)
    glVertex3f(0.496, 1.3, -z)
    glVertex3f(1.0, 0.25, -z)
    glEnd()

    # left front
    glBegin(GL_POLYGON)
    glVertex3f(1.2, 0.25, -z)
    glVertex3f(3.0, 0.15, -z)
    glVertex3f(3.0, -1.0, -z)
    glVertex3f(1.2, -1.0, -z)
    glEnd()

    # left back
    glBegin(GL_POLYGON)
    glVertex3f(1.2, 0.25, -z)
    glVertex3f(1.2, -1.0, -z)
    glVertex3f(-3.0, -1.0, -z)
    glVertex3f(-3.0, 0.25, -z)
    glEnd()

    # right back
    glBegin(GL_POLYGON)
    glVertex3f(1.2, 0.25, z)
    glVertex3f(1.2, -1.0, z)
    glVertex3f(-3.0, -1.0, z)
    glVertex3f(-3.0, 0.25, z)
    glEnd()

    # right front
    glBegin(GL_POLYGON)
    glVertex3f(1.2, 0.25, z)
    glVertex3f(3.0, 0.15, z)
    glVertex3f(3.0, -1.0, z)
    glVertex3f(1.2, -1.0, z)
    glEnd()

    # right above (window frame part)
    glBegin(GL_QUADS)
    glVertex3f(-3.0, 1.5, z)
    glVertex3f(0.6, 1.5, z)
    glVertex3f(0.696, 1.3, z)
    glVertex3f(-3.0, 1.3, z)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3f(-3.0, 1.3, z)
    glVertex3f(-3.0, 0.25, z)
    glVertex3f(-2.5, 0.25, z)
    glVertex3f(-2.5, 1.3, z)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3f(-1.2, 1.3, z)
    glVertex3f(-1.2, 0.25, z)
    glVertex3f(-1.0, 0.25, z)
    glVertex3f(-1.0, 1.3, z)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3f(1.2, 0.25, z)
    glVertex3f(0.696, 1.3, z)
    glVertex3f(0.496, 1.3, z)
    glVertex3f(1.0, 0.25, z)
    glEnd()

    # side bottom
    glColor3f(165 / 255, 8 / 255, 37 / 255)
    glBegin(GL_QUADS)
    glVertex3f(-3.0, -0.3, -z - 0.0013)
    glVertex3f(3.0, -0.3, -z - 0.0013)
    glVertex3f(3.0, -0.7, -z - 0.0013)
    glVertex3f(-3.0, -0.7, -z - 0.0013)

    glVertex3f(-3.0, -0.3, z + 0.0013)
    glVertex3f(3.0, -0.3, z + 0.0013)
    glVertex3f(3.0, -0.7, z + 0.0013)
    glVertex3f(-3.0, -0.7, z + 0.0013)
    glEnd()

    # left mirror
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_BLEND)
    glColor4f(190 / 255, 190 / 255, 190 / 255, 0.6)
    glBegin(GL_QUADS)
    glVertex3f(0.85, 0.5, -z - 0.4)
    glVertex3f(0.85, 0.5, -z)
    glVertex3f(0.85, 0.25, -z)
    glVertex3f(0.85, 0.25, -z - 0.4)
    glEnd()
    glDisable(GL_BLEND)

    glColor3f(180 / 255, 30 / 255, 30 / 255)
    glBegin(GL_QUADS)
    glVertex3f(0.85, 0.5, -z - 0.4)
    glVertex3f(1, 0.5, -z - 0.4)
    glVertex3f(1, 0.25, -z - 0.4)
    glVertex3f(0.85, 0.25, -z - 0.4)

    glVertex3f(0.85, 0.5, -z - 0.4)
    glVertex3f(0.85, 0.5, -z)
    glVertex3f(1, 0.5, -z)
    glVertex3f(1, 0.5, -z - 0.4)

    glVertex3f(1, 0.5, -z - 0.4)
    glVertex3f(1, 0.5, -z)
    glVertex3f(1, 0.25, -z)
    glVertex3f(1, 0.25, -z - 0.4)

    glVertex3f(0.85, 0.5, -z)
    glVertex3f(1, 0.5, -z)
    glVertex3f(1, 0.25, -z)
    glVertex3f(0.85, 0.25, -z)

    glVertex3f(0.85, 0.25, -z - 0.4)
    glVertex3f(0.85, 0.25, -z)
    glVertex3f(1, 0.25, -z)
    glVertex3f(1, 0.25, -z - 0.4)

    glEnd()

    # right mirror
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_BLEND)
    glColor4f(190 / 255, 190 / 255, 190 / 255, 0.6)
    glBegin(GL_QUADS)
    glVertex3f(0.85, 0.5, z + 0.4)
    glVertex3f(0.85, 0.5, z)
    glVertex3f(0.85, 0.25, z)
    glVertex3f(0.85, 0.25, z + 0.4)
    glEnd()
    glDisable(GL_BLEND)

    glColor3f(180 / 255, 30 / 255, 30 / 255)
    glBegin(GL_QUADS)
    glVertex3f(0.85, 0.5, z + 0.4)
    glVertex3f(1, 0.5, z + 0.4)
    glVertex3f(1, 0.25, z + 0.4)
    glVertex3f(0.85, 0.25, z + 0.4)

    glVertex3f(1, 0.5, z + 0.4)
    glVertex3f(1, 0.5, z)
    glVertex3f(1, 0.25, z)
    glVertex3f(1, 0.25, z + 0.4)

    glVertex3f(0.85, 0.5, z + 0.4)
    glVertex3f(0.85, 0.5, z)
    glVertex3f(1, 0.5, z)
    glVertex3f(1, 0.5, z + 0.4)

    glVertex3f(0.85, 0.5, z)
    glVertex3f(1, 0.5, z)
    glVertex3f(1, 0.25, z)
    glVertex3f(0.85, 0.25, z)

    glVertex3f(0.85, 0.25, z + 0.4)
    glVertex3f(0.85, 0.25, z)
    glVertex3f(1, 0.25, z)
    glVertex3f(1, 0.25, z + 0.4)
    glEnd()

    # left window glass
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_BLEND)
    glColor4f(90 / 255, 90 / 255, 90 / 255, 0.3)
    glBegin(GL_QUADS)
    glVertex3f(-3.0, 1.5, -z + 0.01)
    glVertex3f(0.5, 1.5, -z + 0.01)
    glVertex3f(1.2, 0.25, -z + 0.01)
    glVertex3f(-3.0, 0.25, -z + 0.01)
    glEnd()
    glDisable(GL_BLEND)

    # right window glass
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_BLEND)
    glColor4f(90 / 255, 90 / 255, 90 / 255, 0.3)
    glBegin(GL_QUADS)
    glVertex3f(-3.0, 1.5, z - 0.01)
    glVertex3f(0.5, 1.5, z - 0.01)
    glVertex3f(1.2, 0.25, z - 0.01)
    glVertex3f(-3.0, 0.25, z - 0.01)
    glEnd()
    glDisable(GL_BLEND)

    # front window glass
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_BLEND)
    glColor4f(90 / 255, 90 / 255, 90 / 255, 0.3)
    glBegin(GL_QUADS)
    glVertex3f(0.5, 1.5, -z)
    glVertex3f(0.5, 1.5, z)
    glVertex3f(1.2, 0.25, z)
    glVertex3f(1.2, 0.25, -z)
    glEnd()
    glDisable(GL_BLEND)

    # back window glass
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_BLEND)
    glColor4f(90 / 255, 90 / 255, 90 / 255, 0.3)
    glBegin(GL_QUADS)
    glVertex3f(-2.99, 0.25, -z + 0.5)
    glVertex3f(-2.99, 0.25, z - 0.5)
    glVertex3f(-2.99, 1.0, z - 0.5)
    glVertex3f(-2.99, 1.0, -z + 0.5)
    glEnd()
    glDisable(GL_BLEND)

    # Car's Wheel
    glColor3f(0.0, 0.0, 0.0)
    quadric = gluNewQuadric()
    gluQuadricNormals(quadric, GLU_SMOOTH)
    gluQuadricTexture(quadric, GL_TRUE)
    glTranslatef(1.7, -1.0, -1.7)
    gluCylinder(quadric, 0.6, 0.6, 0.2, 15, 15)
    gluDisk(quadric, 0, 0.6, 15, 15)
    glTranslatef(0.0, 0.0, 0.2)
    gluDisk(quadric, 0, 0.6, 15, 15)

    glTranslatef(0.0, 0.0, -0.2)
    glTranslatef(-3.3, 0.0, 0.0)
    gluCylinder(quadric, 0.6, 0.6, 0.2, 15, 15)
    gluDisk(quadric, 0, 0.6, 15, 15)
    glTranslatef(0.0, 0.0, 0.2)
    gluDisk(quadric, 0, 0.6, 15, 15)

    glTranslatef(0.0, 0.0, -0.2)
    glTranslatef(0.0, 0.0, 3.2)
    gluCylinder(quadric, 0.6, 0.6, 0.2, 15, 15)
    gluDisk(quadric, 0, 0.6, 15, 15)
    glTranslatef(0.0, 0.0, 0.2)
    gluDisk(quadric, 0, 0.6, 15, 15)

    glTranslatef(0.0, 0.0, -0.2)
    glTranslatef(3.3, 0.0, 0.0)
    gluCylinder(quadric, 0.6, 0.6, 0.2, 15, 15)
    gluDisk(quadric, 0, 0.6, 15, 15)
    glTranslatef(0.0, 0.0, 0.2)
    gluDisk(quadric, 0, 0.6, 15, 15)

    glColor3f(1.0, 1.0, 1.0)
    gluDisk(quadric, 0.2, 0.4, 15, 15)
    glTranslatef(-3.3, 0.0, 0.0)
    gluDisk(quadric, 0.2, 0.4, 15, 15)
    glTranslatef(0.0, 0.0, -0.2)
    glTranslatef(0.0, 0.0, -3.2)
    gluDisk(quadric, 0.2, 0.4, 15, 15)
    glTranslatef(+3.3, 0.0, 0.0)
    gluDisk(quadric, 0.2, 0.4, 15, 15)

main()