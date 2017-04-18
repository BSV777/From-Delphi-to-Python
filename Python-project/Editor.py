#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from MainWindow import *


if __name__ == "__main__" :
    app = QtGui.QApplication(sys.argv) # Создаем объект app (приложение) - экземпляр класса QApplication

    MainForm = MainWindow() # Создаем объект MainForm - экземпляр класса MainWindow()    
    MainForm.setWindowTitle(u"Editor -") #Заголовок окна
    MainForm.resize(450, 250)  #Установили размеры окна
    MainForm.show() # Отображаем окно
  
    sys.exit(app.exec_()) #Запускаем цикл обработки событий объекта app (приложение)
    