#!/usr/bin/env python
# -*- coding: utf-8 -*-


from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import Qt


class PropWindow(QWidget):
    def __init__(self):  # Конструктор класса PropWindow
        super(PropWindow, self).__init__()
        ly = QHBoxLayout()
        self.tab = QTableWidget(self)
        ly.addWidget(self.tab)
        self.tab.setColumnCount(2)
        self.tab.setRowCount(5)
        self.tab.setHorizontalHeaderLabels(['Property', 'Value'])
        self.tab.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.resize(255, 180)
        self.setWindowTitle(u"Свойства")  # Заголовок окна
        texts = ["Text", "Top", "Left", "Height", "Width"]
        for i, t in enumerate(texts):
            item = QTableWidgetItem()
            item.setText(t)
            item.setFlags((Qt.ItemIsEnabled | Qt.ItemIsSelectable))
            self.tab.setItem(i, 0, item)
        self.tab.show()


if __name__ == "__main__":
    app = QApplication([])
    test = PropWindow()
    test.show()
    app.exec_()
