from PyQt5.QtGui import QWheelEvent
from PyQt5.QtWidgets import QWidget

from PyQt5 import QtCore
from Ui_MainWindow import Ui_Form


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


    def on_click_create(self):
        current_size = self.le_vertex_count.text()
        print(current_size)

        try:
            size = int(current_size)
            if 1 < size < 15:
                self.openGLWidget.set_size(size)
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
        if event.key() == QtCore.Qt.Key_R:
            current_size = self.le_vertex_count.text()
            print(current_size)
            self.openGLWidget.set_size(int(current_size))

    def on_click_enable_fog(self, b):
        if b.isChecked():
            print('enable')
            self.openGLWidget.set_fog(1)
        else:
            print('disable')
            self.openGLWidget.set_fog(0)


