#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from os import listdir
 
from PyQt4 import QtCore, QtGui
 
images = listdir('/home/andrey/')
 
class Window(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
    self.setGeometry(800, 600, 350, 150)
     
    for i in images:
        if i.endswith('png'):
            img = '/home/andrey/%s' % i
            button = QtGui.QPushButton('Name', self)
            button.setGeometry(1, 1, 100, 100)
            button.setIcon(QtGui.QIcon(img))
     
 
    self.connect(button, QtCore.SIGNAL('clicked()'), QtGui.qApp, QtCore.SLOT('quit()'))
     
     
     
app = QtGui.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())