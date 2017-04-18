#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse
from MainWindow import *

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('name', nargs='?', default='мир')
    return parser



if __name__ == "__main__" :
    app = QtGui.QApplication(sys.argv) # Создаем объект app (приложение) - экземпляр класса QApplication

    #parser = createParser()
    #namespace = parser.parse_args (sys.argv[1:]) 
    # print (namespace)
    #print ("Привет, {}!".format (namespace.name) )



    MainForm = MainWindow() # Создаем объект MainForm - экземпляр класса MainWindow()    
    MainForm.setWindowTitle(u"Editor -") #Заголовок окна
    MainForm.resize(450, 250)  #Установили размеры окна
    MainForm.show() # Отображаем окно
  
    sys.exit(app.exec_()) #Запускаем цикл обработки событий объекта app (приложение)
    