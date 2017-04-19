#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QFont

class MainWindow(QtGui.QMainWindow):  #Объявляем класс MainWindow, наследующий свойства класса QMainWindow модуля QtGui

#Внутренние процедуры класса
#------------------------------------------------------------------------------
    def _createbt(self):
        print("_createbt") #DEBUG: Отладочный вывод
        self.label2= QtGui.QLabel(u"88888888") # Создали объект надпись класса QLabel                
        self.label2.move(10, 90)

#TODO: Работать здесь!
#------------------------------------------------------------------------------

    def _select(self):
        print("_select") #DEBUG: Отладочный вывод

    def _createed(self):
        print("_createed") #DEBUG: Отладочный вывод

    def _createlb(self):
        print("_createlb") #DEBUG: Отладочный вывод

    def _delobj(self):
        print("_delobj") #DEBUG: Отладочный вывод

    def _about(self):
        print("_about") #DEBUG: Отладочный вывод

    def _create(self):
        print("_create") #DEBUG: Отладочный вывод

    def _open(self):
        print("_open") #DEBUG: Отладочный вывод

    def _save(self):
        print("_save") #DEBUG: Отладочный вывод

    def _saveas(self):
        print("_saveas") #DEBUG: Отладочный вывод

    def _saveasweb(self):
        print("_saveasweb") #DEBUG: Отладочный вывод

    def _openasweb(self):
        print("_openasweb") #DEBUG: Отладочный вывод

    def _exit(self):
        print("_exit") #DEBUG: Отладочный вывод




#------------------------------------------------------------------------------


    def __init__(self, parent=None):  #Объявляем конструктор класса MyWindow
        QtGui.QWidget.__init__(self, parent) #Сначала выполняем действия, предусмотренные конструктором родительского класса (QWidget)

        self.setFont(QFont('SansSerif', 9)) #Устанавливаем шрифт
        
# TODO: 1. Добавить скроллбары
#------------------------------------------------------------------------------
        #self.scrollLayout = QtGui.QFormLayout()

        #scrollWidget = QtGui.QWidget() # cначала создаём сам виджет
        #scrollWidget.setLayout(self.scrollLayout) # добавляем на него слой

        #scrollArea = QtGui.QScrollArea()
        #scrollArea.setWidgetResizable(True) #разрешаем проктурку
        #scrollArea.setWidget(self.scrollWidget)
        
        #-----------------------------------------
        #self.gridLayout = QGridLayout(self)        
        #self.scrollArea = QScrollView(self)        
        #self.scrollArea.setGeometry(0, 0, 369, 286)            
        #self.Form1Layout = QGridLayout(self.scrollArea.viewport()) 
        #self.gridLayout.addWidget(self.scrollArea, 0, 0)  
#------------------------------------------------------------------------------
        
# TEST: Тестовые объекты
#------------------------------------------------------------------------------
        label1 = QtGui.QLabel(u"Надпись", self) # Создали объект надпись класса QLabel                
        label1.move(120, 200)
        
        edit1 =  QtGui.QLineEdit(u"Поле", self)# Создали объект поле ввода         
        edit1.move(150, 160)
        
        button1 = QtGui.QPushButton(u"Кнопка", self) # Создали объект кнопка, экземпляр класса QPushButton
        button1.move(200, 200)
                   
        
#------------------------------------------------------------------------------

      
#Создание меню        
#------------------------------------------------------------------------------    
        menubar = self.menuBar() #Создание меню
            
        #Подменю Файл   
        a_create = QtGui.QAction(u"Созд&ать", self)
        a_create.setShortcut('Ctrl+N')
        a_create.setStatusTip(u"Создать схему размещения")    
        self.connect(a_create, QtCore.SIGNAL('triggered()'), self._create)
    
        a_open = QtGui.QAction(u"&Открыть", self)
        a_open.setShortcut('Ctrl+O')
        a_open.setStatusTip(u"Открыть схему размещения объектов")    
        self.connect(a_open, QtCore.SIGNAL('triggered()'), self._open)
    
        a_save = QtGui.QAction(u"&Сохранить", self)
        a_save.setShortcut('Ctrl+S')
        a_save.setStatusTip(u"Сохранить схему размещения объектов")    
        self.connect(a_save, QtCore.SIGNAL('triggered()'), self._save)
    
        a_saveas = QtGui.QAction(u"Сохранить &как", self)
        a_saveas.setStatusTip(u"Сохранить схему размещения объектов как...")    
        self.connect(a_saveas, QtCore.SIGNAL('triggered()'), self._saveas)
    
        a_saveasweb = QtGui.QAction(u"Сохранить как Web-страни&цу", self)        
        a_saveasweb.setStatusTip(u"Сохранить схему размещения объектов как Web-страницу")    
        self.connect(a_saveasweb, QtCore.SIGNAL('triggered()'), self._saveasweb)
    
        a_openasweb = QtGui.QAction(u"Открыть как &Web-страницу", self)        
        a_openasweb.setStatusTip(u"Открыть схему размещения объектов как Web-страницу")    
        self.connect(a_openasweb, QtCore.SIGNAL('triggered()'), self._openasweb)
        
        a_exit = QtGui.QAction(u"В&ыход", self)
        a_exit.setShortcut('Ctrl+Q')
        a_exit.setStatusTip(u"Выход из программы")
        self.connect(a_exit, QtCore.SIGNAL('triggered()'), self._exit)
        
        m_file = menubar.addMenu(u"&Файл")
        m_file.addAction(a_create)        #Строка меню
        m_file.addAction(a_open)          #Строка меню
        m_file.addSeparator()             #Разделитель меню
        m_file.addAction(a_save)          #Строка меню
        m_file.addAction(a_saveas)        #Строка меню
        m_file.addAction(a_saveasweb)     #Строка меню
        m_file.addSeparator()             #Разделитель меню
        m_file.addAction(a_openasweb)     #Строка меню
        m_file.addSeparator()             #Разделитель меню
        m_file.addAction(a_exit)          #Строка меню
        
        #Подменю Объект        
        a_createbt = QtGui.QAction(QtGui.QIcon('icons/bt.png'), u"Создать &кнопку", self)
        a_createbt.setStatusTip(u"Создать кнопку на форме")   
        self.connect(a_createbt, QtCore.SIGNAL('triggered()'), self._createbt)
                      
        a_createed = QtGui.QAction(QtGui.QIcon('icons/ed.png'), u"Создать &поле ввода", self)
        a_createed.setStatusTip(u"Создать поле ввода на форме")    
        self.connect(a_createed, QtCore.SIGNAL('triggered()'), self._createed)

        a_createlb = QtGui.QAction(QtGui.QIcon('icons/lb.png'), u"Создать &надпись", self)
        a_createlb.setStatusTip(u"Создать надпись на форме")    
        self.connect(a_createlb, QtCore.SIGNAL('triggered()'), self._createlb)

        a_delobj = QtGui.QAction(u"У&далить объект", self)
        a_delobj.setShortcut('DEL')
        a_delobj.setStatusTip(u"Удалить выбранный объект")    
        self.connect(a_delobj, QtCore.SIGNAL('triggered()'), self._delobj)
        
        m_object = menubar.addMenu(u"&Объект")        
        m_object.addAction(a_createbt)   #Строка меню
        m_object.addAction(a_createed)   #Строка меню
        m_object.addAction(a_createlb)   #Строка меню
        m_object.addSeparator()          #Разделитель меню
        m_object.addAction(a_delobj)     #Строка меню
        
        #Подменю Справка
        a_about = QtGui.QAction(u"&О программе", self)
        a_about.setShortcut('F1')
        a_about.setStatusTip(u"Сведения о программе")    
        self.connect(a_about, QtCore.SIGNAL('triggered()'), self._about)
        
        m_help = menubar.addMenu(u"&Справка")
        m_help.addAction(a_about)       #Строка меню        

#Создание тулбара
#------------------------------------------------------------------------------    
        a_select = QtGui.QAction(QtGui.QIcon('icons/obj.png'), u"Выбор объекта", self)
        a_select.setStatusTip(u"Редактировать существующий объект")    
        self.connect(a_select, QtCore.SIGNAL('triggered()'), self._select)

        toolbar = self.addToolBar(u"Панель инструментов")
        toolbar.addAction(a_select)     #Кнопка тулбара
        toolbar.addAction(a_createbt)   #Кнопка тулбара
        toolbar.addAction(a_createed)   #Кнопка тулбара
        toolbar.addAction(a_createlb)   #Кнопка тулбара

#------------------------------------------------------------------------------    
        
        self.statusBar().showMessage(u"Готов") #Первоначальная надпись в строке статуса   
        

if __name__ == "__main__" :
    print(u"------ test ------")