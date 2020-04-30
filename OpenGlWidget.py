from PyQt5.QtWidgets import QOpenGLWidget
from OpenGL.GL import *
from OpenGL.GLU import *
from math import pi, tan

from Maze import generate_maze


class OpenGLWidget(QOpenGLWidget):
    def __init__(self, parent):
        super().__init__(parent)
        print("new OpenGl")

        self.distance = 20
        self.angle_y = 0
        self.angle_x = 0

        self.maze = None

        self.fog_start = 5
        self.fog_end = 20  

    def initializeGL(self):
        print("initializeGL")
        glEnable(GL_POINT_SMOOTH)
        glEnable(GL_DEPTH_TEST)

    def resizeGL(self, p_int, p_int_1):
        print("resizeGL")
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, (p_int / p_int_1), 0.01, 1000)

    def paintGL(self):
        print("paintGL")
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(0, 0, self.distance, 0, 0, self.distance - 1, 0, 1, 0)

        glPushMatrix()
        glRotatef(self.angle_y, 0, 1, 0)
        glRotatef(self.angle_x, 1, 0, 0)

        # self.axis()
        if self.maze is not None:
            self.maze.show()
        glPopMatrix()

    # manipulation ------------------------------------
    def rotate(self, angle_x, angle_y):
        self.angle_x += angle_x
        self.angle_y += angle_y
        self.update()

    def zoom(self, distance, out=False):
        if out:
            self.distance -= distance
        else:
            self.distance += distance

        self.fog_start = self.distance - (self.size - 1)
        self.fog_end = self.distance + 1.5*(self.size - 1)

        self.makeCurrent()
        glFogf(GL_FOG_START, self.fog_start)
        glFogf(GL_FOG_END, self.fog_end)
        self.update()

    def create_maze(self, size, algorithm):
        print('set_size')
        self.makeCurrent()
        self.size = size
        self.maze = generate_maze(self.size, algorithm)
        # self.fog_start = (size-1)/tan(pi/8)
        # self.fog_end = self.fog_start + 2 * (size-1)
        self.fog_start = self.distance - (self.size - 1)
        self.fog_end = self.distance + 1.5 * (self.size - 1)
        glFogf(GL_FOG_START, self.fog_start)
        glFogf(GL_FOG_END, self.fog_end)
        self.update()

    def set_fog(self, mode):
        self.makeCurrent()
        if mode == 1:
            glEnable(GL_FOG)
            glFogi(GL_FOG_MODE, GL_LINEAR)
            glFogfv(GL_FOG_COLOR, (0.1, 0.1, 0.1, 1))
            glHint(GL_FOG_HINT, GL_DONT_CARE)
            glFogf(GL_FOG_START, self.fog_start)
            glFogf(GL_FOG_END, self.fog_end)
        else:
            glDisable(GL_FOG)
        self.update()

    # draw --------------------------------------------
    def axis(self):
        glBegin(GL_LINES)
        glVertex3f(0, 0, 0)
        glVertex3f(1, 0, 0)

        glVertex3f(0, 0, 0)
        glVertex3f(0, 1, 0)

        glVertex3f(0, 0, 0)
        glVertex3f(0, 0, 1)

        glEnd()
