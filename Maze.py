from random import randint, choice
from OpenGL.GL import *
from OpenGL.GLU import *

# генерирует лабиринт размером n и возвращает массив


def create_binary(n):
    arr = [[0] * (n**3) for i in range(0, n**3)]

    for g in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                vertex = j + i*n + g*n**2
                res = choice([1, 2, 3])

                # 1 - up
                # 2 - left
                # 3 - forward

                if res == 1:
                    if i != 0:
                        # up
                        next_vertex = j + (i-1)*n + g*n**2
                        arr[vertex][next_vertex] = 1
                    else:
                        res = choice([2, 3])

                        if res == 2:
                            if j != 0:
                                # left
                                arr[vertex][vertex - 1] = 1
                            elif g != n - 1:
                                # forward
                                next_vertex = j + i * n + (g + 1) * n ** 2
                                arr[vertex][next_vertex] = 1

                        elif res == 3:
                            if g != n-1:
                                    # forward
                                    next_vertex = j + i * n + (g + 1) * n ** 2
                                    arr[vertex][next_vertex] = 1
                            elif j != 0:
                                # left
                                arr[vertex][vertex - 1] = 1

                elif res == 2:
                    if j != 0:
                        # left
                        arr[vertex][vertex - 1] = 1
                    else:
                        res = choice([1, 3])

                        if res == 1:
                            if i != 0:
                                # up
                                next_vertex = j + (i - 1) * n + g * n ** 2
                                arr[vertex][next_vertex] = 1

                            elif g != n-1:
                                # forward
                                next_vertex = j + i * n + (g + 1) * n ** 2
                                arr[vertex][next_vertex] = 1

                        elif res == 3:
                            if g != n - 1:
                                # forward
                                next_vertex = j + i * n + (g + 1) * n ** 2
                                arr[vertex][next_vertex] = 1
                            elif i != 0:
                                # up
                                next_vertex = j + (i - 1) * n + g * n ** 2
                                arr[vertex][next_vertex] = 1

                elif res == 3:
                    if g != n - 1:
                        # forward
                        next_vertex = j + i * n + (g + 1) * n ** 2
                        arr[vertex][next_vertex] = 1
                    else:
                        res = choice([1, 2])
                        if res == 1:
                            if i != 0:
                                # up
                                next_vertex = j + (i - 1) * n + g * n ** 2
                                arr[vertex][next_vertex] = 1
                            elif j != 0:
                                # left
                                arr[vertex][vertex - 1] = 1
                        elif res == 2:
                            if j != 0:
                                # left
                                arr[vertex][vertex - 1] = 1
                            elif i != 0:
                                # up
                                next_vertex = j + (i - 1) * n + g * n ** 2
                                arr[vertex][next_vertex] = 1
    return arr


class Maze:
    def __init__(self, state, n):
        self.edges = self.gen_edges(state)
        self.vertices = self.gen_vertices(n)

    def gen_edges(self, state):
        edges = []
        length = len(state)

        for i in range(0, length):
            for j in range(0, length):
                if state[i][j] == 1:
                    edges.append((i, j))

        return edges

    def gen_vertices(self, n):
        vertices = []

        for g in range(1 - n, n, 2):
            for i in range(n - 1, -n, -2):
                for j in range(1 - n, n, 2):
                    vertices.append((j, i, g))

        return vertices

    def show(self):
        print('show')

        glColor3f(1, 1, 1)
        glPointSize(10)
        glBegin(GL_POINTS)
        for vertex in self.vertices:
            glVertex3fv(vertex)
        glEnd()


        glLineWidth(2)
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])

        glEnd()

        glPointSize(12)
        glColor3f(1, 0, 0)
        glBegin(GL_POINTS)
        glVertex3fv(self.vertices[0])
        glEnd()

        glPointSize(12)
        glColor3f(1, 0, 1)
        glBegin(GL_POINTS)
        glVertex3fv(self.vertices[-1])
        glEnd()


def generate_maze(n) -> Maze:
    return Maze(create_binary(n), n)
