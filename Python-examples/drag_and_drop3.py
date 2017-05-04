#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *

from PyQt4.QtCore import Qt


class Button(QPushButton):
    def __init__(self, title, parent):
        super(Button, self).__init__(title, parent)

    def mouseMoveEvent(self, e):
        if e.buttons() != Qt.LeftButton:
            return
        mousePosition = e.pos()
        x = e.x()
        y = e.y()
        #self.setWindowTitle(
        #print("Mouse: [" + mousePosition.x().__str__() + ", " + mousePosition.y().__str__() + "]")
        #print(str(x),str(y))
        self.move(x, y)

    def mousePressEvent(self, e):
        pass

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.button = Button('Button', self)
        self.button.move(100, 65)
        self.setWindowTitle('Click or Move')
        self.setGeometry(300, 300, 280, 150)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()