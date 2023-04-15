from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

#student_id = [[2, 0], [3, 0], [1, 2], [6, 8]]

def draw_lines():
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_LINES)

    ## 2
    glVertex2f(50, 300)
    glVertex2f(100, 300)

    glVertex2f(100, 300)
    glVertex2f(100, 250)

    glVertex2f(50, 250)
    glVertex2f(100, 250)

    glVertex2f(50, 250)
    glVertex2f(50, 200)

    glVertex2f(50, 200)
    glVertex2f(100, 200)

    ## 0
    glVertex2f(120, 200)
    glVertex2f(170, 200)

    glVertex2f(170, 200)
    glVertex2f(170, 300)

    glVertex2f(170, 300)
    glVertex2f(120, 300)

    glVertex2f(120, 300)
    glVertex2f(120, 200)

    ## 3
    glVertex2f(190, 200)
    glVertex2f(240, 200)

    glVertex2f(240, 200)
    glVertex2f(240, 300)

    glVertex2f(240, 300)
    glVertex2f(190, 300)

    glVertex2f(190, 250)
    glVertex2f(240, 250)

    ## 0
    glVertex2f(260, 200)
    glVertex2f(310, 200)

    glVertex2f(310, 200)
    glVertex2f(310, 300)

    glVertex2f(310, 300)
    glVertex2f(260, 300)

    glVertex2f(260, 300)
    glVertex2f(260, 200)

    ## 1
    glVertex2f(330, 200)
    glVertex2f(330, 300)

    ## 2
    glVertex2f(350, 300)
    glVertex2f(400, 300)

    glVertex2f(400, 300)
    glVertex2f(400, 250)

    glVertex2f(350, 250)
    glVertex2f(400, 250)

    glVertex2f(350, 250)
    glVertex2f(350, 200)

    glVertex2f(350, 200)
    glVertex2f(400, 200)

    ## 6
    glVertex2f(420, 300)
    glVertex2f(470, 300)

    glVertex2f(420, 250)
    glVertex2f(420, 200)

    glVertex2f(420, 200)
    glVertex2f(470, 200)

    glVertex2f(470, 250)
    glVertex2f(470, 200)

    glVertex2f(420, 250)
    glVertex2f(470, 250)

    glVertex2f(420, 300)
    glVertex2f(420, 250)

    ## 8
    glVertex2f(490, 300)
    glVertex2f(540, 300)

    glVertex2f(490, 250)
    glVertex2f(490, 200)

    glVertex2f(490, 200)
    glVertex2f(540, 200)

    glVertex2f(540, 250)
    glVertex2f(540, 200)

    glVertex2f(490, 250)
    glVertex2f(540, 250)

    glVertex2f(490, 300)
    glVertex2f(490, 250)

    glVertex2f(540, 300)
    glVertex2f(540, 250)

    glEnd()


def iterate():
    glViewport(0, 0, 600, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 600, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here
    draw_lines()

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(600, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"20301268") #window name
glutDisplayFunc(showScreen)

glutMainLoop()