from OpenGL.GL import *
from OpenGL.GLUT import *

"""
Mid-point line drawing algorithm
"""

digiNet = {
    0: [[200, 200, 201, 300], [150, 299, 201, 300],
        [149, 199, 150, 299], [149, 199, 200, 200]],
    1: [[200, 200, 201, 300]],
    2: [[200, 250, 201, 300], [150, 299, 201, 300],
        [149, 199, 150, 250], [149, 199, 200, 200],
        [149, 250, 200, 251]],
    3: [[150, 299, 201, 300], [149, 250, 200, 251],
        [149, 199, 200, 200], [201, 300, 200, 200]],
    4: [[150, 299, 149, 250], [149, 250, 200, 251],
        [201, 300, 200, 200]],
    5: [[200, 200, 201, 250], [150, 299, 201, 300],
        [149, 250, 150, 299], [149, 199, 200, 200],
        [149, 250, 200, 251]],
    6: [[200, 200, 201, 250], [150, 299, 201, 300],
        [149, 199, 150, 299], [149, 199, 200, 200],
        [149, 250, 200, 251]],
    7: [[200, 200, 201, 300], [150, 299, 201, 300]],
    8: [[200, 200, 201, 300], [150, 299, 201, 300],
        [149, 199, 150, 299], [149, 199, 200, 200],
        [149, 250, 200, 251]],
    9: [[200, 200, 201, 300], [150, 299, 201, 300],
        [149, 250, 150, 299], [149, 199, 200, 200],
        [149, 250, 200, 251]],
}


def drawPoints(x, y):
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def originalZone(z, x, y):
    if z == 0:
        drawPoints(x, y)
    elif z == 1:
        drawPoints(y, x)
    elif z == 2:
        drawPoints(-y, x)
    elif z == 3:
        drawPoints(-x, y)
    elif z == 4:
        drawPoints(-x, -y)
    elif z == 5:
        drawPoints(-y, -x)
    elif z == 6:
        drawPoints(y, -x)
    elif z == 7:
        drawPoints(x, -y)


def drawLines(z, x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx
    e = 2 * dy
    ne = 2 * (dy - dx)
    y = y1
    x = x1
    while x < x2:
        originalZone(z, x, y)
        if d > 0:  # next pixel: NE
            d += ne
            y += 1
        else:
            d += e  # next pixel: E
        x += 1


def convZone(z, x1, y1, x2, y2):
    if z == 0:
        return x1, y1, x2, y2
    elif z == 1:
        return y1, x1, y2, x2
    elif z == 2:
        return -y1, x1, -y2, x2
    elif z == 3:
        return -x1, y1, -x2, y2
    elif z == 4:
        return -x1, -y1, -x2, -y2
    elif z == 5:
        return -y1, -x1, -y2, -x2
    elif z == 6:
        return y1, -x1, y2, -x2
    elif z == 7:
        return x1, -y1, x2, -y2


def findZone(x1, y1, x2, y2):
    zone = 0
    dx = x2 - x1
    dy = y2 - y1
    if abs(dx) >= abs(dy):
        if dx > 0 and dy > 0:
            zone = 0
        elif dx < 0 and dy > 0:
            zone = 3
        elif dx < 0 and dy < 0:
            zone = 4
        elif dx > 0 and dy < 0:
            zone = 7
    else:
        if dx > 0 and dy > 0:
            zone = 1
        elif dx < 0 and dy > 0:
            zone = 2
        elif dx < 0 and dy < 0:
            zone = 5
        elif dx > 0 and dy < 0:
            zone = 6
    return zone


def showDigits(x1, y1, x2, y2):
    zone = findZone(x1, y1, x2, y2)
    a1, b1, a2, b2 = convZone(zone, x1, y1, x2, y2)
    drawLines(zone, a1, b1, a2, b2)


def loadDigits(n):
    for i in digiNet:
        if i == int(n[-2]):
            for k in digiNet[i]:
                showDigits(k[0], k[1], k[2], k[3])
        if i == int(n[-1]):
            for k in digiNet[i]:
                showDigits(k[0] + 80, k[1], k[2] + 80, k[3])


# ----------------------------------------------------------

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 1.0)
    loadDigits(input("Student ID: "))
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab 2 Task")
glutDisplayFunc(showScreen)

glutMainLoop()