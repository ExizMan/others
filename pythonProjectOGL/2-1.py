import sys

from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

def draw_cylinder(radius, height,x0,y0,z0, num_segments):
    angle_step = 2 * np.pi / num_segments

    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(x0, y0, height)
    for i in range(num_segments + 1):
        angle = i * angle_step
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        glVertex3f(x, y, height)
    glEnd()

    glBegin(GL_QUAD_STRIP)
    for i in range(num_segments + 1):
        angle = i * angle_step
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        glVertex3f(x, y, height)
        glVertex3f(x, y, z0)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(x0, y0, z0)
    for i in range(num_segments + 1):
        angle = i * angle_step
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        glVertex3f(x, y, z0)
    glEnd()


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
    #glDepthFunc(GL_LEQUAL)
    #glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)

    #glShadeModel(GL_SMOOTH)

    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
    glEnable(GL_TEXTURE_2D)

    specReflection = [1.0, 1.0, 1.0, 1.0]
    #glMaterialfv(GL_FRONT, GL_SPECULAR, specReflection)
    #glMateriali(GL_FRONT, GL_SHININESS, 30)
    #glLightfv(GL_LIGHT0, GL_SPECULAR, specReflection)
    glLightfv(GL_LIGHT0, GL_POSITION, [0.0, 0.0, 1.0, 1.0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0,1.0,1.0,1.0])
    #glLightfv(GL_LIGHT0, GL_POSITION, [-1.0, -1.0, -1.0, -1.0])
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
    drawTank()

    idle()
    glFlush()
    glutSwapBuffers()


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


# def drawTank():
#     glColor3f(0.3, 0.3, 0.3)
#     glBegin(GL_TRIANGLE_FAN)
#     glVertex3f(-3.4, 0.25, 0.5)
#     glVertex3f(-3.4, 0.25, 0)
#     glVertex3f(-3.4, -1.0, 1)
#     glVertex3f(-3.4, -1.0, 0.3)
#     glEnd()


def drawTank():
    z = 1.5

    # back window frame




    # bottom
    glColor3f(70 / 255, 20 / 255, 55 / 255)
    glBegin(GL_QUADS)
    glVertex3f(-3.4, -1.0, -z)
    glVertex3f(-3.4, -1.0, z)
    glVertex3f(3.0, -1.0, z)
    glVertex3f(3.0, -1.0, -z)
    glEnd()

    # front

    glBegin(GL_QUADS)
    glVertex3f(3.0, -1.0, -z)
    glVertex3f(3.0, 0.0, -z)
    glVertex3f(3.0, 0.0, z)
    glVertex3f(3.0, -1.0, z)
    glEnd()

    # VLD
    glBegin(GL_QUADS)

    glVertex3f(3.0, 0.0, -z)
    glVertex3f(3.0, 0.0, z)
    glVertex3f(1.0,0.4,z)
    glVertex3f(1.0,0.4,-z)
    glEnd()


    # vld 2

    glBegin(GL_QUADS)
    glVertex3f(1.0,0.4,z)
    glVertex3f(1.0,0.4,-z)
    glVertex3f(-3.4,0.4,-z)
    glVertex3f(-3.4,0.4,z)
    glEnd()

    # korma
    glBegin(GL_QUADS)
    glVertex3f(-3.4,0.4,z)
    glVertex3f(-3.4,0.4,-z)
    glVertex3f(-3.4,-1.0,-z)
    glVertex3f(-3.4,-1.0,z)
    glEnd()

    # right ld
    glBegin(GL_POLYGON)
    glVertex3f(-3.4,0.4,z)
    glVertex3f(-3.4,-1.0,z)
    glVertex3f(3.0,-1.0,z)
    glVertex3f(3.0, 0.0, z)
    glVertex3f(1.0,0.4,z)
    glEnd()

    # left ld
    glBegin(GL_POLYGON)
    glVertex3f(-3.4,0.4,-z)
    glVertex3f(-3.4,-1.0,-z)
    glVertex3f(3.0,-1.0,-z)
    glVertex3f(3.0, 0.0, -z)
    glVertex3f(1.0,0.4,-z)
    glEnd()


    #right track
    glColor3f(0.5, 0.5, 0.5)
    glTranslatef(2.7,-1.0,1.0)
    draw_cylinder(0.5,0.2,0.0,0.0,1.0,66)
    glTranslatef(-1.0, 0, 0)
    draw_cylinder(0.5, 0.2, 0.0, 0.0, 1.0, 66)
    glTranslatef(-1.0, 0, 0)
    draw_cylinder(0.5, 0.2, 0.0, 0.0, 1.0, 66)
    glTranslatef(-1.0, 0, 0)
    draw_cylinder(0.5, 0.2, 0.0, 0.0, 1.0, 66)
    glTranslatef(-1.0, 0, 0)
    draw_cylinder(0.5, 0.2, 0.0, 0.0, 1.0, 66)
    glTranslatef(-1.0, 0, 0)
    draw_cylinder(0.5, 0.2, 0.0, 0.0, 1.0, 66)
    glTranslatef(-1.0, 0, 0)
    draw_cylinder(0.5, 0.2, 0.0, 0.0, 1.0, 66)


    #left track
    glTranslatef(6.0, 0.0, -3.2)
    draw_cylinder(0.5, 0.2, 0.0, 0.0, 1.0, 66)
    glTranslatef(-1.0, 0, 0)
    draw_cylinder(0.5, 0.2, 0.0, 0.0, 1.0, 66)
    glTranslatef(-1.0, 0, 0)
    draw_cylinder(0.5, 0.2, 0.0, 0.0, 1.0, 66)
    glTranslatef(-1.0, 0, 0)
    draw_cylinder(0.5, 0.2, 0.0, 0.0, 1.0, 66)
    glTranslatef(-1.0, 0, 0)
    draw_cylinder(0.5, 0.2, 0.0, 0.0, 1.0, 66)
    glTranslatef(-1.0, 0, 0)
    draw_cylinder(0.5, 0.2, 0.0, 0.0, 1.0, 66)
    glTranslatef(-1.0, 0, 0)
    draw_cylinder(0.5, 0.2, 0.0, 0.0, 1.0, 66)

    glTranslatef(6.0-2.7,1.0,3.2-1.0)

    #это все башня
    glColor3f(60 / 255, 20 / 255, 45 / 255)
    glBegin(GL_QUADS)
    glVertex3f(-2.4, 0.4, -(-z+0.5))
    glVertex3f(-0.0, 0.4, -(-z+0.5))
    glVertex3f(-0.4, 1, -(-z+1))
    glVertex3f(-2.0, 1, -(-z+1))
    glEnd()

    glBegin(GL_QUADS)
    glVertex3f(-2.4, 0.4, -(-z+0.5))
    glVertex3f(-2.0, 1, -(-z + 1))
    glVertex3f(-2.0, 1, (-z + 1))
    glVertex3f(-2.4, 0.4, (-z + 0.5))
    glEnd()

    glBegin(GL_QUADS)
    glVertex3f(-2.4, 0.4, -z+0.5)
    glVertex3f(-0.0, 0.4, -z+0.5)
    glVertex3f(-0.4, 1, -z+1)
    glVertex3f(-2.0, 1, -z+1)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3f(-0.0, 0.4, -(-z + 0.5))
    glVertex3f(-0.4, 1, -(-z + 1))
    glVertex3f(-0.4, 1, (-z + 1))
    glVertex3f(-0.0, 0.4, (-z + 0.5))
    glEnd()

    glBegin(GL_QUADS)
    glVertex3f(-0.4, 1, -z+1)
    glVertex3f(-0.4, 1, -(-z + 1))
    glVertex3f(-2.0, 1, -(-z+1))
    glVertex3f(-2.0, 1, (-z+1))
    glEnd()
    glColor3f(0.2,0.2,0.2)
    glTranslatef(0,0.5,0)
    glRotate(90,0,1,0)
    glTranslatef(0,0.1,-1.2)
    draw_cylinder(0.1, 1.9, 0.0, 0.0, 1.0, 66)






main()