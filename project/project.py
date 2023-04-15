# Final Project

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time
import numpy as np
import math
import random


def draw_points(x, y):
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def FindZone(dx, dy):
    zone = 0
    if abs(dx) >= abs(dy):
        if dx >= 0 and dy >= 0:
            zone = 0
        elif dx < 0 and dy > 0:
            zone = 3
        elif dx < 0 and dy < 0:
            zone = 4
        elif dx > 0 and dy < 0:
            zone = 7
    elif abs(dx) <= abs(dy):
        if dx >= 0 and dy >= 0:
            zone = 1
        elif dx < 0 and dy > 0:
            zone = 2
        elif dx < 0 and dy < 0:
            zone = 5
        elif dx > 0 and dy < 0:
            zone = 6
    return zone


def OriginalZone(x, y, zone):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return -y, x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return y, -x
    elif zone == 7:
        return x, -y


def ConvertToZone0(x1, y1, x2, y2, zone):
    if zone == 0:
        return x1, y1, x2, y2
    elif zone == 1:
        return y1, x1, y2, x2
    elif zone == 2:
        return y1, -x1, y2, -x2
    elif zone == 3:
        return -x1, y1, -x2, y2
    elif zone == 4:
        return -x1, -y1, -x2, -y2
    elif zone == 5:
        return -y1, -x1, -y2, -x1
    elif zone == 6:
        return -y1, x1, -y2, x2
    elif zone == 7:
        return x1, -y1, x2, -y2
    return x1, y1, x2, y2


def MidPointLine(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    zone = FindZone(dx, dy)
    x1, y1, x2, y2 = ConvertToZone0(x1, y1, x2, y2, zone)
    dx = x2 - x1
    dy = y2 - y1
    d_init = 2 * dy - dx
    del_ne = 2 * dy - 2 * dx
    del_e = 2 * dy
    x = x1
    y = y1
    while x <= x2:
        new_x, new_y = OriginalZone(x, y, zone)
        draw_points(new_x, new_y)
        x += 1
        if d_init > 0:
            y += 1
            d_init = d_init + del_ne
        else:
            d_init = d_init + del_e


def circlepoints(center_x, center_y, x, y):
    draw_points(x + center_x, y + center_y)
    draw_points(x + center_x, -y + center_y)
    draw_points(-x + center_x, -y + center_y)
    draw_points(-x + center_x, y + center_y)
    draw_points(y + center_x, x + center_y)
    draw_points(-y + center_x, x + center_y)
    draw_points(-y + center_x, -x + center_y)
    draw_points(y + center_x, -x + center_y)


def MidPointcircle(center_x, center_y, radius):
    x = 0
    y = radius
    d = 1 - radius
    circlepoints(center_x, center_y, x, y)
    while x < y:
        if d >= 0:
            d += (2 * x) - (2 * y) + 5
            x += 1
            y -= 1
        else:
            d += (2 * x) + 3
            x += 1
        circlepoints(center_x, center_y, x, y)


def circlepoints_water(center_x, center_y, x, y):
    draw_points(x + center_x, y + center_y)
    draw_points(-x + center_x, y + center_y)
    draw_points(y + center_x, x + center_y)
    draw_points(-y + center_x, x + center_y)


def MidPointcircle_water(center_x, center_y, radius):
    x = 0
    y = radius
    d = 1 - radius
    circlepoints_water(center_x, center_y, x, y)
    while x < y:
        if d >= 0:
            d += (2 * x) - (2 * y) + 5
            x += 1
            y -= 1
        else:
            d += (2 * x) + 3
            x += 1
        circlepoints_water(center_x, center_y, x, y)


def scaling(x1, y1, x2, y2, sc=0):
    v1 = np.array([[x1], [y1], [1]])
    v2 = np.array([[x2], [y2], [1]])

    s = np.array([[sc, 0, 0],
                  [0, sc, 0],  # scaling
                  [0, 0, 1]])

    t1 = np.array([[1, 0, -v1[0][0]],
                   [0, 1, -v1[1][0]],  # origin e astese
                   [0, 0, 1]])

    v11 = np.matmul(s, np.matmul(t1, v1))
    v22 = np.matmul(s, np.matmul(t1, v2))

    t1_inv = np.array([[1, 0, v1[0][0]],
                       [0, 1, v1[1][0]],
                       [0, 0, 1]])

    v11 = np.matmul(t1_inv, v11)
    v22 = np.matmul(t1_inv, v22)
    return (v11[0][0], v11[1][0], v22[0][0], v22[1][0])


def car1(pixel):
    for i in range(0, pixel, 50):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        buildings()
        flame(pixel)
        x_axis = -110 + i
        y_axis = -210 + (i * .5)
        glColor3f(1.0, 1.0, 1.0)
        for km in range(15):  # back wheel
            MidPointcircle(200 + x_axis, 270 + y_axis, km)
        glColor3f(1.0, 0, 0)
        for il in range(14):  # front wheel
            MidPointcircle(270 + x_axis, 312 + y_axis, il)

        # MidPointLine(120, 250, 170, 250)  # LOWER BACK 1
        # MidPointLine(118, 248, 168, 248)  # LOWER BACK 2
        # MidPointLine(118, 248, 120, 250)  # LOWER BACK 3
        # MidPointLine(168, 248, 170, 250)  # LOWER BACK 4

        MidPointLine(120 + x_axis, 250 + y_axis, 120 + x_axis, 300 + y_axis)  # BACK LEFT 5
        MidPointLine(170 + x_axis, 250 + y_axis, 170 + x_axis, 300 + y_axis)  # BACK RIGHT 6
        for b in range(50):  # 5-6
            MidPointLine(120 + b + x_axis, 250 + y_axis, 120 + b + x_axis, 300 + y_axis)  # BACK LEFT 5

        MidPointLine(120 + x_axis, 300 + y_axis, 170 + x_axis, 300 + y_axis)  # BACK TOP 7

        for a in range(50):  # 8-9

            MidPointLine(120 + a + x_axis, 300 + y_axis, 220 + a + x_axis, 350 + y_axis)  # TOP 8
        # MidPointLine(125, 320, 225, 370)
        for i in range(50):  # 11-9
            # MidPointLine(170, 300, 270, 350)    #TOP 9
            MidPointLine(170 + x_axis, 250 + i + y_axis, 270 + x_axis, 310 + (i * .8) + y_axis)  # BOTTOM 11

        glColor3f(1.0, 1.0, 1.0)
        # MidPointLine(220, 350, 270, 350)    #13
        glColor3f(1.0, 1.0, 1.0)
        for j in range(20):  # front low
            MidPointLine(271 + x_axis, 310 + j + y_axis, 295 + x_axis, 325 + j + y_axis)
        glColor3f(0.0, 0.0, 0.0)
        MidPointLine(271 + x_axis, 329 + y_axis, 295 + x_axis, 344 + y_axis)
        glColor3f(1.0, 0.0, 0.0)
        for k in range(20):  # front top
            MidPointLine(271 + x_axis, 330 + k + y_axis, 295 + x_axis, 345 + y_axis)
        # MidPointLine(296, 400, 270, 410)
        # MidPointLine(270, 330, 295, 345)

        glColor3f(1.0, 1.0, 1.0)

        MidPointLine(120 + x_axis, 250 + y_axis, 170 + x_axis, 250 + y_axis)  # LOWER BACK 1
        MidPointLine(118 + x_axis, 248 + y_axis, 168 + x_axis, 248 + y_axis)  # LOWER BACK 2
        MidPointLine(118 + x_axis, 248 + y_axis, 120 + x_axis, 250 + y_axis)  # LOWER BACK 3
        MidPointLine(168 + x_axis, 248 + y_axis, 170 + x_axis, 250 + y_axis)  # LOWER BACK 4

        MidPointLine(120 + x_axis, 300 + y_axis, 220 + x_axis, 350 + y_axis)  # 8
        MidPointLine(170 + x_axis, 300 + y_axis, 271 + x_axis, 351 + y_axis)  # TOP 9

        MidPointLine(270 + x_axis, 310 + y_axis, 270 + x_axis, 350 + y_axis)  # 12

        MidPointLine(120 + x_axis, 250 + y_axis, 120 + x_axis, 300 + y_axis)  # BACK LEFT 5
        MidPointLine(170 + x_axis, 250 + y_axis, 170 + x_axis, 300 + y_axis)  # BACK RIGHT 6
        MidPointLine(120 + x_axis, 300 + y_axis, 170 + x_axis, 300 + y_axis)  # BACK TOP 7
        MidPointLine(220 + x_axis, 350 + y_axis, 270 + x_axis, 350 + y_axis)  # 13
        MidPointLine(170 + x_axis, 250 + y_axis, 270 + x_axis, 310 + y_axis)  # BOTTOM 11
        MidPointLine(271 + x_axis, 350 + y_axis, 295 + x_axis, 345 + y_axis)  # front top
        glLoadIdentity()
        iterate()
        glutSwapBuffers()
        time.sleep(0.001)
        # glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(1.0, 1, 1)
    for b in range(5):
        MidPointLine(200 + (b * 2.9) + x_axis, 330 + b + y_axis, 170 + x_axis, 350 + b + y_axis)
    glColor3f(0, 1, 0.95)
    for i in range(20):
        MidPointcircle_water(100 + i + x_axis, 350 + y_axis, 70 - i)


def buildings():
    glColor3f(1.0, 1.0, 1.0)
    # road
    MidPointLine(0, 70, 250 + 520, 337 + 85)
    MidPointLine(200, 00, 250 + 600, 337 + 85)

    # building -1
    MidPointLine(60, 300, 60, 330)

    MidPointLine(30, 85, 30, 330)
    MidPointLine(30, 330, 90, 360)
    MidPointLine(90, 115, 90, 360)
    MidPointLine(90, 360, 240, 400)
    MidPointLine(240, 185, 240, 400)
    for i in range(40):
        MidPointLine(120 + i, 300 + i * .3, 120 + i, 350 + i * .3)
    for i in range(40):
        MidPointLine(180 + i, 320 + i * .3, 180 + i, 368 + i * .3)

    # building -2
    MidPointLine(310, 320, 310, 360)
    MidPointLine(320, 320, 320, 360)

    MidPointLine(300, 210, 300, 360)
    MidPointLine(300, 360, 330, 380)
    MidPointLine(330, 220, 330, 380)
    MidPointLine(330, 380, 450, 410)
    MidPointLine(450, 280, 450, 410)
    for i in range(40):
        MidPointLine(350 + i, 310 + i * .3, 350 + i, 360 + i * .3)
    for i in range(40):
        MidPointLine(400 + i, 325 + i * .3, 400 + i, 375 + i * .3)

    # building -3
    MidPointLine(30 + 470+10, 370, 30 + 470+10, 400)
    MidPointLine(30 + 470 + 20, 370, 30 + 470 + 20, 400)
    MidPointLine(30 + 470 + 30, 370, 30 + 470 + 30, 400)

    MidPointLine(30 + 470, 305, 30 + 470, 410)
    MidPointLine(30 + 470, 410, 100 + 450, 430)
    MidPointLine(100 + 450, 320, 100 + 450, 430)
    MidPointLine(100 + 450, 430, 250 + 380, 450)
    MidPointLine(250 + 380, 360, 250 + 380, 450)
    for i in range(25):
        MidPointLine(565 + i, 370 + i * .3, 565 + i, 400 + i * .3)
    for i in range(25):
        MidPointLine(600 + i, 382 + i * .3, 600 + i, 410 + i * .3)


def flame(pixel):
    glColor3f(1.0, 0, 0.0)
    if pixel == 250:
        for i in range(30, 241, 1):
            MidPointLine(i, 330 + random.randint(-100, 100), i, 450 + random.randint(-100, 100))
    elif pixel == 500:
        for i in range(300, 451, 3):
            MidPointLine(i, 350 + random.randint(-30, 30), i, 450 + random.randint(-30, 30))
    elif pixel == 700:
        for i in range(500, 631, 3):
            MidPointLine(i, 380 + random.randint(-20, 20), i, 480 + random.randint(-20, 20))


def car(pixel):
    sc = 1
    for i in range(0, pixel, 50):
        sc -= 0.01
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        buildings()
        flame(pixel)
        x_axis = -110 + i
        y_axis = -210 + (i * .54)
        origin_x = int(120 * sc)
        origin_y = int(250 * sc)
        glColor3f(1.0, 1.0, 1.0)
        for km in range(int(15 * sc)):  # back wheel
            MidPointcircle(origin_x + 80 * sc + x_axis, origin_y + 20 * sc + y_axis, km)
        glColor3f(1.0, 0, 0)
        for il in range(int(14 * sc)):  # front wheel
            MidPointcircle(origin_x + 150 * sc + x_axis, origin_y + 62 * sc + y_axis, il)

        # MidPointLine(120, 250, 170, 250)  # LOWER BACK 1
        # MidPointLine(118, 248, 168, 248)  # LOWER BACK 2
        # MidPointLine(118, 248, 120, 250)  # LOWER BACK 3
        # MidPointLine(168, 248, 170, 250)  # LOWER BACK 4

        # MidPointLine(origin_x+x_axis, origin_y+y_axis, origin_x+x_axis, origin_y+(50*sc)+y_axis)  # BACK LEFT 5
        # MidPointLine(origin_x+(50*sc)+x_axis, origin_y+y_axis, origin_x+(50*sc)+x_axis, origin_y+(50*sc)+y_axis)  # BACK RIGHT 6
        a, b, c, d = scaling(origin_x, origin_y, origin_x, origin_y + (50 * sc), sc)
        MidPointLine(a + x_axis, b + y_axis, c + x_axis, d + y_axis)  # BACK LEFT 5
        for bx in range(int(50 * sc)):  # 5-6
            # new_x,new_y,new_x1,new_y1=()
            MidPointLine(a + bx + x_axis, b + y_axis, c + bx + x_axis, d + y_axis)  # BACK LEFT 5

        a1, b1, c1, d1 = scaling(a + bx, b, c + bx, d)

        # glColor3f(1.0, 1, 1)
        # MidPointLine(a1+x_axis, b1+y_axis, c1+x_axis, d1+y_axis)  # BACK TOP 7
        MidPointLine(a + bx + x_axis, b + y_axis, c + bx + x_axis, d + y_axis)  # BACK TOP 7

        a2, b2, c2, d2 = scaling(origin_x, origin_y + (50 * sc), origin_x + (100 * sc), origin_y + (100 * sc), sc)
        for a in range(int(50 * sc)):  # 8-9
            MidPointLine(a2 + a + x_axis, d + y_axis, c2 + a + x_axis, d2 + y_axis)  # TOP 8
        # # MidPointLine(125, 320, 225, 370)
        a3, b3, c3, d3 = scaling(origin_x + 50, origin_y, origin_x + 150, origin_y + 60, sc)
        # a2, b2, c2, d2 = scaling(170, 250, 270, 310, sc)
        for i in range(int(50 * sc)):  # 11-9
            # MidPointLine(170, 300, 270, 350)    #TOP 9
            MidPointLine(a2 + a + x_axis, b + (i * 1 * sc) + y_axis, c2 + a + x_axis,
                         d3 + (i * .85 * sc) + y_axis)  # BOTTOM 11

        glColor3f(1.0, 1.0, 1.0)
        # MidPointLine(220, 350, 270, 350)    #13
        glColor3f(1.0, 1.0, 1.0)
        a4, b4, c4, d4 = scaling(origin_x + (100 * sc), origin_y + (60 * sc), origin_x + (175 * sc),
                                 origin_y + (75 * sc), sc)
        for j in range(int(20 * sc)):  # front low
            MidPointLine(c2 + a + x_axis, d3 + .8 * sc + y_axis + j, c4 + x_axis, d4 + j + y_axis)
        # glColor3f(0.0, 0.0, 0.0)
        # MidPointLine(271+x_axis, 329+y_axis, 295+x_axis, 344+y_axis)
        glColor3f(1.0, 0.0, 0.0)
        a5, b5, c5, d5 = scaling(origin_x + (100 * sc), origin_y + (60 * sc), origin_x + (175 * sc),
                                 origin_y + (75 * sc), sc)
        for k in range(int(20 * sc)):  # front top
            MidPointLine(c2 + a + x_axis, b4 + y_axis + j + k, c4 + x_axis, d4 + j + y_axis)
        # MidPointLine(296, 400, 270, 410)
        # MidPointLine(270, 330, 295, 345)

        glColor3f(1.0, 1.0, 1.0)
        a25, b25, c25, d25 = scaling(origin_x, origin_y, origin_x, origin_y)
        MidPointLine(a25 + x_axis, b25 + y_axis, c25 + 50 * sc + x_axis, d25 + y_axis)  # LOWER BACK 1
        # MidPointLine(118+x_axis, 248+y_axis, 168+x_axis, 248+y_axis)  # LOWER BACK 2
        # MidPointLine(118+x_axis, 248+y_axis, 120+x_axis, 250+y_axis)  # LOWER BACK 3
        # MidPointLine(168+x_axis, 248+y_axis, 170+x_axis, 250+y_axis)  # LOWER BACK 4

        MidPointLine(a25 + x_axis, b25 + 50 * sc + y_axis, c25 + 100 * sc + x_axis, d25 + 100 * sc + y_axis)  # 8
        MidPointLine(a25 + 50 * sc + x_axis, b25 + 50 * sc + y_axis, c25 + 151 * sc + x_axis,
                     d25 + 101 * sc + y_axis)  # TOP 9

        MidPointLine(a25 + 150 * sc + x_axis, b25 + 60 * sc + y_axis, c25 + 150 * sc + x_axis,
                     d25 + 100 * sc + y_axis)  # 12

        MidPointLine(a25 + x_axis, b25 + y_axis, c25 + x_axis, d25 + 50 * sc + y_axis)  # BACK LEFT 5

        MidPointLine(a25 + 50 * sc + x_axis, b25 + y_axis, c25 + 50 * sc + x_axis,
                     d25 + 50 * sc + y_axis)  # BACK RIGHT 6
        MidPointLine(a25 + x_axis, b25 + 50 * sc + y_axis, c25 + 50 * sc + x_axis, d25 + 50 * sc + y_axis)  # BACK TOP 7

        MidPointLine(a25 + 100 * sc + x_axis, b25 + 100 * sc + y_axis - 1, c25 + 150 * sc + x_axis,
                     d25 + 100 * sc + y_axis - 1)  # 13
        MidPointLine(a25 + 50 * sc + x_axis, b25 + y_axis, c25 + 150 * sc + x_axis, d25 + 65 * sc + y_axis)  # BOTTOM 11
        MidPointLine(a25 + 150 * sc + x_axis, b25 + 100 * sc + y_axis, c25 + 170 * sc + x_axis,
                     d25 + 95 * sc + y_axis)  # front top
        glLoadIdentity()
        iterate()
        glutSwapBuffers()
        time.sleep(0.001)
        # glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(1.0, 1, 1)
    a26, b26, c26, d26 = scaling(origin_x, origin_y, origin_x, origin_y)
    for b in range(5):
        MidPointLine(a26 + 80 * sc + (b * 2.9) + x_axis, b26 + 80 * sc + b + y_axis, c26 + 50 * sc + x_axis,
                     d25 + 100 * sc + b + y_axis)
    glColor3f(0, 1, 0.95)
    #water
    for i in range(int(20 * sc)):
        MidPointcircle_water(origin_x - 23 * sc + i + x_axis, origin_y + 100 * sc + y_axis, 70 * sc - i)
    # MidPointLine(271, 310, 295, 325)  #front low


def iterate():
    glViewport(0, 0, 1000, 1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 1000, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


global id
id = input('Input Building Number: ')


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0, 0)
    # id='3'
    # first_two()
    # car1()
    # car()
    # if id=='1':
    #     car1(250)
    # elif id=='2':
    #     car1(500)
    # elif id=='3':
    #     car1(700)
    # -------------------------------------------------
    if id == '1':
        car(250)
    elif id == '2':
        car(500)
    elif id == '3':
        car(700)
    else:
        print('Input Invalid')

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 1000)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Project Using Midpoint")
glutDisplayFunc(showScreen)

glutMainLoop()