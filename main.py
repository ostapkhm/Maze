import os
import sys
from PyQt5 import QtWidgets, QtCore
from MainWindow import MainWindow

os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
app = QtWidgets.QApplication(sys.argv)
app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
win = MainWindow()

win.show()
sys.exit(app.exec_())