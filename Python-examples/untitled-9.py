# -*- coding:  utf-8 -*-
__author__ = 'STAVR'
from PyQt4 import QtGui, QtCore
import sys
 
class Main(QtGui.QMainWindow):
    def __init__(self, parent = None):
        super(Main, self).__init__(parent)
 
 
        self.addButton = QtGui.QPushButton('Кнопка добавления')
        # подключаем дейсвтие для добавления новой новой кнопки
        # при натажии на Кнопку добавления
        self.addButton.clicked.connect(self.addWidget)
 
        # определяем содержимое области(виджета) прокрутки
        #  - а именно слой формата (QFormLayout) - два столбца
        self.scrollLayout = QtGui.QFormLayout()
 
        # добавляем  ране созданный слой прокрутки
        # на виджет прокрутки
        self.scrollWidget = QtGui.QWidget() # cначала создаём сам виджет
        self.scrollWidget.setLayout(self.scrollLayout) # добавляем на него слой
 
        # определяем область механизм прокрутки (QScrollArea)
        self.scrollArea = QtGui.QScrollArea()
        self.scrollArea.setWidgetResizable(True) #разрешаем проктурку
        #добавляем на область виджет, с ранее добавленным на него слоем слоем
        self.scrollArea.setWidget(self.scrollWidget)
 
        # создаём главный вертикальный слой
        self.mainLayout = QtGui.QVBoxLayout()
 
        # добавляем элементы на главный слой
        self.mainLayout.addWidget(self.addButton) # добавляем основную кнопку
        self.mainLayout.addWidget(self.scrollArea) # добавляем область прокрутки
 
        # определяем "центральный виджет"
        self.centralWidget = QtGui.QWidget()
        self.centralWidget.setLayout(self.mainLayout)
 
        # устанавливаем "центральный виджет"
        self.setCentralWidget(self.centralWidget)
 
    def addWidget(self):
        self.scrollLayout.addRow(TestButton())
 
 
class TestButton(QtGui.QPushButton):
  def __init__( self, parent=None):
      super(TestButton, self).__init__(parent)
      self.setText("Это появляющаяся кнопка")
      self.clicked.connect(self.deleteLater) # подключаем действие самоудаления
 
 
app = QtGui.QApplication(sys.argv)
myWidget = Main()
myWidget.show()
app.exec_()
