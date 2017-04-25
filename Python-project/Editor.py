#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import mParserTextFile  # Импортируем модули с функциями ParserTextFile и WriteHTMLFile
import mWriteHTMLFile
from MainWindow import *

if __name__ == "__main__" :
    if len(sys.argv) > 1:  # Если переданы параметры командной строки, то работаем в консоли, форму не создаем
        inputFileName = sys.argv[1]
        if len(sys.argv) > 2:  # Выходной файл задан
            outputFileName = sys.argv[2]
        else:  # Выходной файл не задан - формируем имя на основе входного файла
            dir = os.path.dirname(inputFileName)
            name, ext = os.path.splitext(os.path.basename(inputFileName))
            outputFileName = os.path.join(dir, name + ".htm")

        if os.path.exists(inputFileName):  # Если входной файл существует вызываем парсер и формирование HTML
            array = []  # Список объектов с их свойствами. Каждый объект представлен словарем
            if mParserTextFile.ParserTextFile(inputFileName, array):  # Ошибки были записаны в лог
                print("Input file contains errors. See log file: " + os.path.join(dir, name + ".log"))
            mWriteHTMLFile.WriteHTMLFile(outputFileName, array)
        else:
            print("Can't open file: " + inputFileName)
    else:
        app = QtGui.QApplication(sys.argv)  # Создаем объект app (приложение) - экземпляр класса QApplication
        MainForm = MainWindow()  # Создаем объект MainForm - экземпляр класса MainWindow()
        MainForm.setWindowTitle(u"Editor - ")  # Заголовок окна
        MainForm.resize(450, 250)  # Установили размеры окна
        MainForm.show()  # Отображаем окно
        sys.exit(app.exec_())  # Запускаем цикл обработки событий объекта app (приложение)
