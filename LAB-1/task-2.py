from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_points(x, y):
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(155, 230) #jekhane show korbe pixel
    glEnd()


def draw_lines(x, y):
    glBegin(GL_LINES)
    glColor3f(1.0, 1.0, 1.0)

    #ground
    glVertex2i(100, 200)
    glVertex2i(200, 200)
    #left
    glVertex2i(100, 300)
    glVertex2i(100, 200)

    #right
    glVertex2i(200, 200)
    glVertex2i(200, 300)


#door

    #left
    glVertex2i(140, 200)
    glVertex2i(140, 250)
    #right
    glVertex2i(160, 200)
    glVertex2i(160, 250)
    #up
    glVertex2i(140, 250)
    glVertex2i(160, 250)


    glEnd()

def draw_triangles(x, y):
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2i(100, 300)
    glVertex2i(150, 400)
    glVertex2i(200, 300)

    glEnd()


def draw_square(x, y):
    glBegin(GL_QUADS)
    glColor4f(1.0, 1.0, 1.0, 1.0)
    glVertex2i(105, 280)
    glVertex2i(120, 280)
    glVertex2i(120, 260)
    glVertex2i(105, 260)

    glEnd()



def draw_square2(x, y):
    glBegin(GL_QUADS)
    glColor4f(1.0, 1.0, 1.0, 1.0)
    glVertex2i(180, 280)
    glVertex2i(195, 280)
    glVertex2i(195, 260)
    glVertex2i(180, 260)

    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here
    draw_lines(500, 500)
    draw_points(500, 500)
    draw_square(500, 500)
    draw_square2(500, 500)
    draw_triangles(500, 500)
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()
