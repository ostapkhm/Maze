from random import randint, choice
from OpenGL.GL import *
from OpenGL.GLU import *
import sys

sys.setrecursionlimit(6000)

TERNARY_TREE = 0
RECURSIVE_BACKTRACKING = 1
KRUSKUL_ALGORITHM = 2


def recursive_backtracking(size):
    arr_choice = []

    def possible_choice(z, y, x, size):
        arr_choice.clear()
        # directions
        # 1 - up
        # 2 - down
        # 3 - left
        # 4 - right
        # 5 - forward
        # 6 - back

        if x > 0 and arr[z][y][x - 1] == 0:
            arr_choice.append(3)

        if x < size - 1 and arr[z][y][x + 1] == 0:
            arr_choice.append(4)

        if y > 0 and arr[z][y - 1][x] == 0:
            arr_choice.append(1)

        if y < size - 1 and arr[z][y + 1][x] == 0:
            arr_choice.append(2)

        if z > 0 and arr[z - 1][y][x] == 0:
            arr_choice.append(6)

        if z < size - 1 and arr[z + 1][y][x] == 0:
            arr_choice.append(5)

        if not arr_choice:
            return -1

        return choice(arr_choice)

    def walk(z, y, x):
        # directions
        # 1 - up
        # 2 - down
        # 3 - left
        # 4 - right
        # 5 - forward
        # 6 - back

        direction = possible_choice(z, y, x, size)
        vertex = x + y*size + z * size**2

        if direction != -1:
            if direction == 1:
                next_vertex = x + (y - 1)*size + z*size**2
                res[vertex][next_vertex] = 1
                arr[z][y - 1][x] = 11
                walk(z, y - 1, x)

            if direction == 2:
                next_vertex = x + (y + 1) * size + z * size ** 2
                res[vertex][next_vertex] = 1
                arr[z][y+1][x] = 12
                walk(z, y + 1, x)

            if direction == 3:
                next_vertex = vertex - 1
                res[vertex][next_vertex] = 1
                arr[z][y][x-1] = 13
                walk(z, y, x - 1)

            if direction == 4:
                next_vertex = vertex + 1
                res[vertex][next_vertex] = 1
                arr[z][y][x+1] = 14
                walk(z, y, x + 1)

            if direction == 5:
                next_vertex = x + y * size + (z + 1) * size ** 2
                res[vertex][next_vertex] = 1
                arr[z+1][y][x] = 15
                walk(z+1, y, x)

            if direction == 6:
                next_vertex = x + y * size + (z - 1) * size ** 2
                res[vertex][next_vertex] = 1
                arr[z-1][y][x] = 16
                walk(z-1, y, x)

        else:
            if arr[z][y][x] == 11:
                walk(z, y+1, x)
            if arr[z][y][x] == 12:
                walk(z, y-1, x)
            if arr[z][y][x] == 13:
                walk(z, y, x+1)
            if arr[z][y][x] == 14:
                walk(z, y, x-1)
            if arr[z][y][x] == 15:
                walk(z-1, y, x)
            if arr[z][y][x] == 16:
                walk(z+1, y, x)

    arr = [[[0 for i in range(size)] for j in range(size)] for k in range(size)]
    res = [[0] * (size**3) for i in range(0, size**3)]
    x_start = randint(0, size-1)
    y_start = randint(0, size-1)
    z_start = randint(0, size-1)
    arr[z_start][y_start][x_start] = 10
    walk(z_start, y_start, x_start)

    return res


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


def kruskul_maze(n):
    graph = [[0] * (n**3) for i in range(0, n**3)]
    possible_edges = []

    for g in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                if j < n - 1:
                    possible_edges.append((j + i * n + g * n**2, j + 1 + i * n + g * n**2))
                if i < n - 1:
                    possible_edges.append((j + i * n + g * n**2, j + (i + 1) * n + g * n**2))
                if g < n - 1:
                    possible_edges.append((j + i * n + g * n**2, j + i * n + (g+1) * n**2))

    v_numbers = [i for i in range(0, n ** 3)]

    while len(possible_edges) != 0:
        idx = randint(0, len(possible_edges) - 1)
        edge = possible_edges.pop(idx)

        start = edge[0]
        end = edge[1]

        if v_numbers[start] != v_numbers[end]:
            digit = v_numbers[end]
            for i in range(0, len(v_numbers)):
                if v_numbers[i] == digit:
                    v_numbers[i] = v_numbers[start]

            graph[start][end] = 1
    return graph


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


def generate_maze(n, algorithm) -> Maze:
    algorithm_func = None
    if algorithm == TERNARY_TREE:
        algorithm_func = create_binary
    elif algorithm == RECURSIVE_BACKTRACKING:
        algorithm_func = recursive_backtracking
    elif algorithm == KRUSKUL_ALGORITHM:
        algorithm_func = kruskul_maze

    return Maze(algorithm_func(n), n)
