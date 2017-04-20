# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *


class dlgTest(QScrollArea):
    def __init__(self, parent = None):
        QDialog.__init__(self, parent)

        # устанавливаем горизонтальные/вертикальные области прокрутки
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setVerticalScrollBarPolicy  (Qt.ScrollBarAlwaysOn)

        # создаю необходимые элементы интерфейса
        self.lblCount = QLabel()
        self.lblCount.setText(self.tr("Objects selected:"))
        self.setWindowTitle(self.tr("Interface test"))
        self.resize(500, 400)

        # размещаем виджеты
        layout = QVBoxLayout()
        layout.addWidget(self.lblCount)
        self.setLayout(layout)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    frm = dlgTest()
    frm.show()
    sys.exit(app.exec_())