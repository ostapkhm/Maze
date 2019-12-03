# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maze_creator.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from OpenGlWidget import OpenGLWidget


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1188, 861)

        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 5, 0)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.openGLWidget = OpenGLWidget(Form)
        self.openGLWidget.setObjectName("openGLWidget")

        self.horizontalLayout.addWidget(self.openGLWidget)

        self.groupBox = QtWidgets.QGroupBox(Form)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())

        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(180, 0))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")

        self.label_vertex_count = QtWidgets.QLabel(self.groupBox)
        self.label_vertex_count.setGeometry(QtCore.QRect(10, 20, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_vertex_count.setFont(font)
        self.label_vertex_count.setObjectName("label_vertex_count")

        self.le_vertex_count = QtWidgets.QLineEdit(self.groupBox)
        self.le_vertex_count.setGeometry(QtCore.QRect(10, 70, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_vertex_count.setFont(font)
        self.le_vertex_count.setMaxLength(2)
        self.le_vertex_count.setText('2')
        self.le_vertex_count.setObjectName("le_vertex_count")

        self.btn_create = QtWidgets.QPushButton(self.groupBox)
        self.btn_create.setGeometry(QtCore.QRect(10, 110, 161, 20))
        self.btn_create.setObjectName("btn_create")

        self.btn_left = QtWidgets.QPushButton(self.groupBox)
        self.btn_left.setGeometry(QtCore.QRect(10, 200, 56, 17))
        self.btn_left.setObjectName("btn_left")
        self.btn_left.setAutoRepeat(True)

        self.btn_right = QtWidgets.QPushButton(self.groupBox)
        self.btn_right.setGeometry(QtCore.QRect(110, 200, 56, 17))
        self.btn_right.setObjectName("btn_right")
        self.btn_right.setAutoRepeat(True)

        self.btn_down = QtWidgets.QPushButton(self.groupBox)
        self.btn_down.setGeometry(QtCore.QRect(60, 220, 56, 17))
        self.btn_down.setObjectName("btn_down")
        self.btn_down.setAutoRepeat(True)

        self.btn_up = QtWidgets.QPushButton(self.groupBox)
        self.btn_up.setGeometry(QtCore.QRect(60, 180, 56, 17))
        self.btn_up.setObjectName("btn_up")
        self.btn_up.setAutoRepeat(True)

        self.ch_box_fog_enable = QtWidgets.QCheckBox(self.groupBox)
        self.ch_box_fog_enable.setGeometry(QtCore.QRect(10, 270, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ch_box_fog_enable.setFont(font)
        self.ch_box_fog_enable.setObjectName("ch_box_fog_enable")
        self.horizontalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_vertex_count.setText(_translate("Form", "Vertex number:\n"
            " 1<n<15"))
        self.btn_create.setText(_translate("Form", "Create"))
        self.btn_left.setText(_translate("Form", "Left"))
        self.btn_right.setText(_translate("Form", "Right"))
        self.btn_down.setText(_translate("Form", "Down"))
        self.btn_up.setText(_translate("Form", "Up"))
        self.ch_box_fog_enable.setText(_translate("Form", "Fog Enable"))
