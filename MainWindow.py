from PyQt5.QtGui import QWheelEvent
from PyQt5.QtWidgets import QWidget

from PyQt5 import QtCore
from Ui_MainWindow import Ui_Form
from Maze import TERNARY_TREE, KRUSKUL_ALGORITHM, RECURSIVE_BACKTRACKING


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_create.clicked.connect(self.on_click_create)
        self.btn_left.clicked.connect(self.on_click_left)
        self.btn_right.clicked.connect(self.on_click_right)
        self.btn_up.clicked.connect(self.on_click_up)
        self.btn_down.clicked.connect(self.on_click_down)
        self.ch_box_fog_enable.toggled.connect(lambda: self.on_click_enable_fog(self.ch_box_fog_enable))
        self.le_vertex_count.textChanged.connect(self.on_txt_changed)

    def on_click_create(self):
        current_size = self.le_vertex_count.text()
        print(current_size)

        try:
            size = int(current_size)
            if 1 < size <= 10:
                if self.radioButton.isChecked():
                    self.openGLWidget.create_maze(size, TERNARY_TREE)
                elif self.radioButton_2.isChecked():
                    self.openGLWidget.create_maze(size, RECURSIVE_BACKTRACKING)
                elif self.radioButton_3.isChecked():
                    self.openGLWidget.create_maze(size, KRUSKUL_ALGORITHM)

        except Exception:
            pass

    def on_click_left(self):
        self.openGLWidget.rotate(0, -5)

    def on_click_right(self):
        self.openGLWidget.rotate(0, 5)

    def on_click_up(self):
        self.openGLWidget.rotate(-5, 0)

    def on_click_down(self):
        self.openGLWidget.rotate(5, 0)

    def wheelEvent(self, event: QWheelEvent):
        angle = event.angleDelta().y()

        if angle < 0:
            self.openGLWidget.zoom(1, True)
        else:
            self.openGLWidget.zoom(1, False)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_S:
            self.openGLWidget.rotate(-5, 0)
        if event.key() == QtCore.Qt.Key_W:
            self.openGLWidget.rotate(5, 0)
        if event.key() == QtCore.Qt.Key_D:
            self.openGLWidget.rotate(0, 5)
        if event.key() == QtCore.Qt.Key_A:
            self.openGLWidget.rotate(0, -5)
        if event.key() == QtCore.Qt.Key_Return:
            self.on_click_create()

    def on_click_enable_fog(self, b):
        if b.isChecked():
            print('enable')
            self.openGLWidget.set_fog(1)
        else:
            print('disable')
            self.openGLWidget.set_fog(0)

    def on_txt_changed(self):
        txt = self.le_vertex_count.text()

        try:
            value = int(txt)
            if 1 < value <= 10:
                self.le_vertex_count.setStyleSheet("color: rgb(0, 0, 0);")
            else:
                self.le_vertex_count.setStyleSheet("color: rgb(255, 0, 0);")

        except ValueError:
            self.le_vertex_count.setStyleSheet("color: rgb(255, 0, 0);")



